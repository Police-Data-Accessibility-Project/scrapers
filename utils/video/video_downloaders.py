import os
import shutil
from concurrent.futures import as_completed, ThreadPoolExecutor

import requests
import m3u8
from inputimeout import inputimeout, TimeoutOccurred
from tqdm import tqdm
import pytube
from pytube import YouTube
from pytube.innertube import InnerTube


def youtube_downloader(youtube_url, savedir, disable_progressbar=False):
    """Downloads a YouTube video to a given directory.

    Args:
        youtube_url (str): YouTube video url to download.
        savedir (str): Directory where the video will be saved.
        disable_progressbar (bool, optional): Whether to disable the progress bar in the command line. Default is False.
    """
    """Callaback function used to update the download progress bar."""
    progress_callback = lambda stream, data_chunk, bytes_remaining: progress_bar.update(len(data_chunk))

    yt = YouTube(youtube_url, on_progress_callback=progress_callback)

    filename = savedir + yt.title + ".mp4"
    if os.path.exists(filename):
        return

    try:
        stream = yt.streams.get_highest_resolution()
    except pytube.exceptions.AgeRestrictedError:
        # Attempt to override YouTube's age restriction
        yt = YouTube_Override(youtube_url, on_progress_callback=progress_callback)

        try:
            stream = yt.streams.get_highest_resolution()
        except KeyError:
            # Some video's age restriction is unable to be overridden and requires a sign in
            print("This YouTube video is age restricted and requires that you sign in to YouTube to access it.")
            print("Login will only be required once and will be cached for later.")
            try:
                signin = inputimeout(prompt="Would you like to sign in? (y/n): ", timeout=30)
            except TimeoutOccurred:
                signin = "n"
                return

            if signin.lower() == "y":
                yt = YouTube_Override(youtube_url, on_progress_callback=progress_callback, use_oauth=True)
                stream = yt.streams.get_highest_resolution()
            else:
                return

    progress_bar = tqdm(total=stream.filesize, unit="iB", unit_scale=True, desc=yt.title, disable=disable_progressbar)

    retries = 0
    while retries < 5:
        try:
            stream.download(output_path=savedir)
            break
        except Exception as e:
            print("Download failed, retrying...")
            os.remove(filename.replace("#", ""))
            retries = retries + 1


class YouTube_Override(YouTube):
    """Fixes an issue with PyTube that would fail to bypass age restrictions"""

    def bypass_age_gate(self):
        """Attempt to update the vid_info by bypassing the age gate."""
        innertube = InnerTube(client="ANDROID", use_oauth=self.use_oauth, allow_cache=self.allow_oauth_cache)
        innertube_response = innertube.player(self.video_id)

        playability_status = innertube_response["playabilityStatus"].get("status", None)

        # If we still can't access the video, raise an exception
        # (tier 3 age restriction)
        if playability_status == "UNPLAYABLE":
            raise pytube.exceptions.AgeRestrictedError(self.video_id)

        self._vid_info = innertube_response


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
            executor.submit(download_file, url + seg["uri"], TS_DIR) for seg in m3u8_master.data["segments"]
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
