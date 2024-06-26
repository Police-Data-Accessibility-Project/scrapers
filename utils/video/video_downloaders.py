import os
import shutil
import urllib

import m3u8
import pytubefix
import requests

from .video_downloader_utils import *


signin = None

def youtube_downloader(youtube_url: str, savedir: str, disable_progressbar: bool = False) -> None:
    """Downloads a YouTube video to a given directory.

    Args:
        youtube_url (str): YouTube video url to download.
        savedir (str): Directory where the video will be saved.
        disable_progressbar (bool, optional): Whether to disable the progress bar in the command line. Default is False.
    """
    ytVideo = YouTubeVideo(youtube_url, disable_progressbar)

    filename = savedir + ytVideo.title + ".mp4"
    filename = filename.replace("#", "")
    if os.path.exists(filename):
        print("File already exists: " + ytVideo.title + ".mp4")
        return

    try:
        ytVideo.get_stream()
        ytVideo.set_progress_bar()
    except (pytubefix.exceptions.AgeRestrictedError, KeyError):
        try:
            # Attempt to override YouTube's age restriction
            ytVideo.override_age_restriction()
            ytVideo.set_progress_bar()
        except (pytubefix.exceptions.AgeRestrictedError, KeyError, urllib.error.HTTPError):
            # Some video's age restriction is unable to be overridden and requires a sign in
            global signin
            while True: 
                if signin is False:
                    print("Age restricted (download skipped): " + ytVideo.title)
                    return
                elif signin is None:
                    signin = ytVideo.youtube_sign_in(signin)
                else:
                    ytVideo.youtube_sign_in(signin)
                    break
    
    ytVideo.set_progress_bar()
    retries = 0
    while retries < 5:
        try:
            ytVideo.stream.download(output_path=savedir)
            break
        except Exception as e:
            print("Download failed, retrying...")
            ytVideo.set_progress_bar()
            os.remove(filename)
            retries = retries + 1


def ts_downloader(m3u8_url: str, savedir: str, filename: str, disable_progressbar: bool = False) -> None:
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
    print(type(m3u8_master))
    m3u8_file = m3u8_url.split("/")[-1]
    url = m3u8_url[: len(m3u8_url) - len(m3u8_file)]

    TS_DIR = "./ts_files/"
    shutil.rmtree(TS_DIR, ignore_errors=True)

    download_segments(url, m3u8_master, filename, disable_progressbar, TS_DIR)
    '''utils/results = []
    # Download the individual segments
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_to_url = [
            executor.submit(download_file, url + seg["uri"], TS_DIR) for seg in m3u8_master.data["segments"]
        ]

        for future in tqdm(
            as_completed(future_to_url), total=len(future_to_url), desc=filename, disable=disable_progressbar
        ):
            data = future.result()
            results.append(data)'''

    os.makedirs(savedir, exist_ok=True)

    filename = savedir + filename
    merge_segments(filename, TS_DIR, disable_progressbar)
    # Merge the segments into one file
    '''with open(savedir + filename, "wb") as video:
        dir_list = os.listdir(TS_DIR)
        dir_list.sort(key=lambda f: int("".join(filter(str.isdigit, f))))

        for ts_file in tqdm(dir_list, desc="Merging segments", disable=disable_progressbar):
            with open(TS_DIR + ts_file, "rb") as mergefile:
                shutil.copyfileobj(mergefile, video)'''

    shutil.rmtree(TS_DIR)
