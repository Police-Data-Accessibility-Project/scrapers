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
            get_photo_gallery()
            continue

        download_url = "https://www.lakesheriff.com" + a["href"]
        
        filetype = ""
        if filename.endswith("(PDF)") or filename.endswith("(MP4)"):
            filetype = "." + filename[len(filename)-4:len(filename)-1].lower()
        elif filename.endswith("(VID)"):
            filetype = ".vob"
        
        filename = filename[:len(filename)-6] + filetype

        download_file(
            download_url,
            savedir=savedir,
            filename=filename
        )


def get_photo_gallery():
    savedir = "./data/Case 14110123/Images/"

    for p in range(2573, 2876):
        image_url = f"https://www.lakesheriff.com/ImageRepository/Document?documentID={p}"
        filename = f"Image {p}.jpg"

        download_file(image_url, savedir, filename)


def download_file(url, savedir, filename=None):
    """Downloads a file to a given directory.

    Args:
        url (str): Url of the file to download.
        savedir (str): Directory where the file will be saved.
        filename (str, optional): Name the file will be saved as. Defaults to last part of url.
    """
    if filename is None:
        filename = url.split("/")[-1]

    if os.path.exists(savedir + filename):
        return

    os.makedirs(savedir, exist_ok=True)

    r = requests.get(url, stream=True)

    total = int(r.headers.get("content-length", 0))
    progress_bar = tqdm(total=total, unit="iB", unit_scale=True, desc=filename)

    with open(savedir + filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            progress_bar.update(len(chunk))
            f.write(chunk)

    progress_bar.close()


def main():
    urls = [
        "https://www.lakesheriff.com/970/Case-14110123",
        "https://www.lakesheriff.com/1463/Case-01070402",
        "https://www.lakesheriff.com/1499/Case-08020293",
        "https://www.lakesheriff.com/1465/Case-10080048",
        "https://www.lakesheriff.com/1500/Case-14010032",
    ]

    for url in urls:
        get_case_media(url)
        print()


if __name__ == "__main__":
    main()