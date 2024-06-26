import os
import sys

from bs4 import BeautifulSoup
from from_root import from_root
import requests
from tqdm import tqdm

p = from_root("CONTRIBUTING.md").parent
sys.path.insert(1, str(p))

from utils.video.video_downloaders import youtube_downloader


def get_case_media(url):
    """Downloads all media files linked on a case's page.

    Args:
        url (str): Url of the page where the case media is linked.
    """
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")
    title = soup.find("h1", id="versionHeadLine").text.strip()
    a_list = soup.find(class_="moduleContentNew").find_all("a")

    print(f"\nRetrieving {title} media...")

    for a in a_list:
        filename = a.text
        savedir = f"./data/{title}/"
        webpage_url = a["href"]

        if "youtu.be" in webpage_url:
            youtube_downloader(webpage_url, savedir)
            continue
        elif "Photo Gallery" in filename:
            get_photo_gallery(savedir)
            continue

        filetype = ""
        if (
            filename.endswith("(PDF)")
            or filename.endswith("(MP4)")
            or filename.endswith("(MP3)")
            or filename.upper().endswith("(WAV)")
        ):
            # Grab the last part of the filename to be used as the file extention
            filetype = "." + filename[len(filename) - 4 : len(filename) - 1].lower()
        elif filename.endswith("(VID)"):
            if "IA 2018-0023" in title:
                filetype = ".mp4"
            else:
                filetype = ".vob"
        elif filename.endswith("(audio only)"):
            filename = filename + ".mp3"
        else:
            if "Case 23110157" in title:
                get_case_23110157_media(download_url=a["href"], savedir=savedir, filename=filename)
                continue

            # Retrieve webpage as an html
            filename = filename + ".html"
            download_file(webpage_url, savedir=savedir, filename=filename)
            continue

        if not filename.endswith("(audio only).mp3"):
            # Remove the file extension from the last part of the filename
            filename = filename[: len(filename) - 6] + filetype

        download_url = "https://www.lakesheriff.com" + a["href"]

        download_file(download_url, savedir=savedir, filename=filename)


def get_case_23110157_media(download_url: str, savedir: str, filename: str) -> None:
    filetype = ""
    if "Video" in filename or "Camera" in filename:
        filetype = ".mov"
    elif "Interview" in filename or "Statement" in filename:
        filetype = ".mp3"
    else:
        filetype = ".pdf"
    
    filename = filename + filetype
    download_url = "https://www.lakesheriff.com" + download_url
    download_file(download_url, savedir=savedir, filename=filename)


def get_photo_gallery(savedir):
    """Retrieves all images from a photo gallery.

    Args:
        savedir (str): Directory where the images will be saved.
    """
    savedir = savedir + "Images/"

    if "18020066" in savedir:
        start = 3753
        end = 3783
    elif "14110123" in savedir:
        start = 2573
        end = 2876
    else:
        return

    for p in tqdm(range(start, end), desc="Downloading image files"):
        image_url = f"https://www.lakesheriff.com/ImageRepository/Document?documentID={p}"
        filename = f"Image {p}.jpg"

        download_file(image_url, savedir, filename, disable=True)


def download_file(url, savedir, filename=None, disable=False):
    """Downloads a file to a given directory.

    Args:
        url (str): Url of the file to download.
        savedir (str): Directory where the file will be saved.
        filename (str, optional): Name the file will be saved as. Defaults to last part of url.
        disable (bool, optional): Whether or not to disable the progress bar in the command line. Defaults to False.
    """
    if filename is None:
        filename = url.split("/")[-1]

    if os.path.exists(savedir + filename):
        if not disable:
            print("File already exists: " + filename)
        return

    os.makedirs(savedir, exist_ok=True)

    r = requests.get(url, stream=True)

    total = int(r.headers.get("content-length", 0))
    progress_bar = tqdm(total=total, unit="iB", unit_scale=True, desc=filename, disable=disable)

    with open(savedir + filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            progress_bar.update(len(chunk))
            f.write(chunk)

    progress_bar.close()


def main():
    homepage_url = "https://www.lakesheriff.com/969/Use-of-Force"
    download_file(homepage_url, savedir="./data/", filename="Use of Force.html", disable=True)

    r = requests.get(homepage_url)
    soup = BeautifulSoup(r.content, "html.parser")
    a_list = soup.find(class_="fr-alternate-rows").find_all("a")
    a_list.reverse()

    for a in a_list:
        url = "https://www.lakesheriff.com" + a["href"]
        get_case_media(url)
        print()


if __name__ == "__main__":
    main()
