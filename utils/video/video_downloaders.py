import os
import shutil
from concurrent.futures import as_completed, ThreadPoolExecutor

import requests
import m3u8
from tqdm import tqdm
from pytube import YouTube


def youtube_downloader(youtube_url, savedir, disable_progressbar=False):
    """Downloads a YouTube video to a given directory.

    Args:
        youtube_url (str): YouTube video url to download.
        savedir (str): Directory where the video will be saved.
        disable_progressbar (bool, optional): Whether to disable the progress bar in the command line. Default is False.
    """
    """Callaback function used to update the download progress bar."""
    progress_callback = lambda stream, data_chunk, bytes_remaining: progress_bar.update(
        len(data_chunk)
    )

    yt = YouTube(youtube_url, on_progress_callback=progress_callback, disable=disable_progressbar)

    if os.path.exists(savedir + yt.title + ".mp4"):
        return

    stream = yt.streams.get_highest_resolution()
    
    progress_bar = tqdm(
        total=stream.filesize, unit="iB", unit_scale=True, desc=yt.title
    )

    stream.download(output_path=savedir)


def ts_downloader(m3u8_url, savedir, filename, disable_progressbar=False):
    """Downloads ts stream segments and merges them into one video file.

    Args:
        m3u8_url (str): Url of the relevant m3u8 file listing all of the segment locations.
        savedir (str): Directory where the video will be saved.
        filename (str): Name the video file will be saved as.
        disable_progressbar (bool): Whether to disable the progress bar in the command line. Default is False.
    """
    if os.path.exists(savedir + filename):
        return

    r = requests.get(m3u8_url)
    m3u8_master = m3u8.loads(r.text)
    m3u8_file = m3u8_url.split("/")[-1]
    url = m3u8_url[: len(m3u8_url) - len(m3u8_file)]

    TS_DIR = "./ts_files/"
    shutil.rmtree(TS_DIR, ignore_errors=True)

    results = []
    # Download the individual segments
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_to_url = [
            executor.submit(download_file, url + seg["uri"], TS_DIR)
            for seg in m3u8_master.data["segments"]
        ]

        for future in tqdm(
            as_completed(future_to_url), total=len(future_to_url), desc=filename, disable=disable_progressbar
        ):
            data = future.result()
            results.append(data)

    os.makedirs(savedir, exist_ok=True)

    # Merge the segments into one file
    with open(savedir + filename, "wb") as video:
        dir_list = os.listdir(TS_DIR)
        dir_list.sort(key=lambda f: int("".join(filter(str.isdigit, f))))

        for ts_file in tqdm(dir_list, desc="Merging segments", disable=disable_progressbar):
            with open(TS_DIR + ts_file, "rb") as mergefile:
                shutil.copyfileobj(mergefile, video)

    shutil.rmtree(TS_DIR)
