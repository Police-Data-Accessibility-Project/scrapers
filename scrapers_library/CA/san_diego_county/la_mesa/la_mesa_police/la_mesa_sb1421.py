import requests
import m3u8
import shutil
import re
import os
from concurrent.futures import as_completed, ThreadPoolExecutor
from tqdm import tqdm
from bs4 import BeautifulSoup
from pytube import YouTube
from content import yt_videos, ts_videos, pdfs


def get_youtube_video(youtube_url, savedir):
    progress_callback = lambda stream, data_chunk, bytes_remaining: progress_bar.update(
        len(data_chunk)
    )

    yt = YouTube(youtube_url, on_progress_callback=progress_callback)

    if os.path.exists(savedir + yt.title + ".mp4"):
        return

    stream = yt.streams.get_highest_resolution()
    progress_bar = tqdm(
        total=stream.filesize, unit="iB", unit_scale=True, desc=yt.title
    )
    stream.download(output_path=savedir)


def get_ts_stream(m3u8_url, savedir, filename):
    if os.path.exists(savedir + filename):
        return

    r = requests.get(m3u8_url)
    m3u8_master = m3u8.loads(r.text)
    m3u8_file = m3u8_url.split("/")[-1]
    url = m3u8_url[: len(m3u8_url) - len(m3u8_file)]

    TS_DIR = "./ts_files/"
    shutil.rmtree(TS_DIR, ignore_errors=True)

    results = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_to_url = [
            executor.submit(download_file, url + seg["uri"], TS_DIR)
            for seg in m3u8_master.data["segments"]
        ]

        for future in tqdm(
            as_completed(future_to_url), total=len(future_to_url), desc=filename
        ):
            data = future.result()
            results.append(data)

    os.makedirs(savedir, exist_ok=True)

    with open(savedir + filename, "wb") as video:
        dir_list = os.listdir(TS_DIR)
        dir_list.sort(key=lambda f: int("".join(filter(str.isdigit, f))))

        for ts_file in tqdm(dir_list, desc="Merging segments"):
            with open(TS_DIR + ts_file, "rb") as mergefile:
                shutil.copyfileobj(mergefile, video)

    shutil.rmtree(TS_DIR)


def get_case_media():
    url = "https://www.sandiego.gov/police/data-transparency/mandated-disclosures/case?id=07-25-2017%204300%20Altadena%20Ave&cat=Officer%20Involved%20Shootings"
    r = requests.get(url)

    soup = BeautifulSoup(r.content, from_encoding="utf-8")
    a_list = soup.find(class_="view-content").find_all("a")

    for a in a_list:
        dowlnoad_url = a["href"].replace("\n", "")
        download_file(
            download_url,
            savedir="./data/CR 17-0042912/",
            filename=a.text,
            show_status=True,
        )


def download_file(url, savedir, filename=None, show_status=False):
    if filename is None:
        filename = url.split("/")[-1]

    if os.path.exists(savedir + filename):
        return

    os.makedirs(savedir, exist_ok=True)

    r = requests.get(url, stream=True)

    if show_status:
        total = int(r.headers.get("content-length", 0))
        progress_bar = tqdm(total=total, unit="iB", unit_scale=True, desc=filename)

    with open(savedir + filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if show_status:
                progress_bar.update(len(chunk))
            f.write(chunk)

    if show_status:
        progress_bar.close()


def main():
    print("Retrieving YouTube videos...")
    for video in yt_videos:
        get_youtube_video(video["url"], video["dir"])

    print("\nRetrieving video files...")
    for video in ts_videos:
        get_ts_stream(video["url"], video["dir"], video["name"])
    video_url = "https://www.cityoflamesa.us/DocumentCenter/View/16962/Witness-2_Cell_Phone_Video"
    download_file(
        video_url,
        savedir="./data/IA #2020-02/",
        filename="Witness Video 2.mov",
        show_status=True,
    )

    print("\nRetrieving PDF files...")
    for pdf in pdfs:
        download_file(pdf["url"], pdf["dir"], pdf["name"], show_status=True)

    print("\nRetrieving CR 17-0042912 media...")
    get_case_media()

    print()
    audio_url = "https://www.cityoflamesa.us/DocumentCenter/View/16964/RadioRedacted"
    download_file(
        audio_url,
        savedir="./data/IA #2020-02/",
        filename="RadioRedacted.wav",
        show_status=True,
    )


if __name__ == "__main__":
    main()
