from concurrent.futures import as_completed, ThreadPoolExecutor
import os
import shutil

from inputimeout import inputimeout, TimeoutOccurred
import pytube
from pytube.innertube import InnerTube
from tqdm import tqdm


"""Callaback function used to update the download progress bar."""
progress_callback = lambda stream, data_chunk, bytes_remaining: progress_bar.update(len(data_chunk))


def youtube_sign_in():
    print("This YouTube video is age restricted and requires that you sign in to YouTube to access it.")
    print("Login will only be required once and will be cached for later.")
    try:
        signin = inputimeout(prompt="Would you like to sign in? (y/n): ", timeout=30)
    except TimeoutOccurred:
        signin = "n"
        return False

    if signin.lower() == "y":
        yt = YouTube_Override(youtube_url, on_progress_callback=progress_callback, use_oauth=True)
        stream = yt.streams.get_highest_resolution()
        print(type(stream))
        return stream
    else:
        return False


class YouTube_Override(YouTube):
    """Fixes an issue with PyTube that would fail to bypass age restrictions"""

    def bypass_age_gate(self) -> None:
        """Attempt to update the vid_info by bypassing the age gate."""
        innertube = InnerTube(client="ANDROID", use_oauth=self.use_oauth, allow_cache=self.allow_oauth_cache)
        innertube_response = innertube.player(self.video_id)

        playability_status = innertube_response["playabilityStatus"].get("status", None)

        # If we still can't access the video, raise an exception
        # (tier 3 age restriction)
        if playability_status == "UNPLAYABLE":
            raise pytube.exceptions.AgeRestrictedError(self.video_id)

        self._vid_info = innertube_response


def download_segments(url: str, m3u8_master, filename: str, disable_progressbar: bool, ts_dir: str) -> None:
    results = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_to_url = [
            executor.submit(download_file, url + seg["uri"], ts_dir) for seg in m3u8_master.data["segments"]
        ]

        for future in tqdm(
            as_completed(future_to_url), total=len(future_to_url), desc=filename, disable=disable_progressbar
        ):
            data = future.result()
            results.append(data)

def merge_segments(filename: str, ts_dir: str, disable_progressbar: bool) -> None:
    with open(filename, "wb") as video:
        dir_list = os.listdir(ts_dir)
        dir_list.sort(key=lambda f: int("".join(filter(str.isdigit, f))))

        for ts_file in tqdm(dir_list, desc="Merging segments", disable=disable_progressbar):
            with open(ts_dir + ts_file, "rb") as mergefile:
                shutil.copyfileobj(mergefile, video)