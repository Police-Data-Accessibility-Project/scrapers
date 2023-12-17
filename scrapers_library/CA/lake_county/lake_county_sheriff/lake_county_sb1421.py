import os
import sys

import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from from_root import from_root

p = from_root("CONTRIBUTING.md").parent
sys.path.insert(1, str(p))

from utils.video.video_downloaders import youtube_downloader


def get_case_media(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")
    title = soup.find("h1", id="versionHeadLine").text.strip()
    a_list = soup.find(class_="moduleContentNew").find_all("a")

    print(f"Retrieving {title} media...")

    for a in a_list:
        filename = a.text
        savedir = f"./data/{title}/"

        if "YouTube" in filename:
            youtube_downloader(a["href"], savedir)
            continue
        elif "Photo Gallery" in filename:
            get_photo_gallery(savedir)
            continue
        
        filetype = ""
        if filename.endswith("(PDF)") or filename.endswith("(MP4)") or filename.endswith("(MP3)") or filename.upper().endswith("(WAV)"):
            filetype = "." + filename[len(filename)-4:len(filename)-1].lower()
        elif filename.endswith("(VID)"):
            if "IA 2018-0023" in title:
                filetype = ".mp4"
            else:
                filetype = ".vob"
        elif filename.endswith("(audio only)"):
            filename = filename + ".mp3"
        else:
            webpage_url = a["href"]
            filename = filename + ".html"
            download_file(webpage_url, savedir=savedir, filename=filename)
            continue
        
        if not filename.endswith("(audio only).mp3"):
            filename = filename[:len(filename)-6] + filetype
        
        download_url = "https://www.lakesheriff.com" + a["href"]

        download_file(
            download_url,
            savedir=savedir,
            filename=filename
        )


def get_photo_gallery(savedir):
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
    
    for a in a_list:
        url = "https://www.lakesheriff.com" + a["href"]
        get_case_media(url)
        print()


if __name__ == "__main__":
    main()