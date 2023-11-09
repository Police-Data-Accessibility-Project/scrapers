import requests
import m3u8
import shutil
import re
import os
from concurrent.futures import as_completed, ThreadPoolExecutor
from tqdm import tqdm
from content import videos, pdfs

'''
def strip_end(text, suffix):
    if not text.endswith(suffix):
        return text
    return text[:len(text)-len(suffix)]
'''

def get_ts_stream(m3u8_url, savedir, filename):
    if os.path.exists(savedir + filename):
        return

    r = requests.get(m3u8_url)
    m3u8_master = m3u8.loads(r.text)
    m3u8_file = m3u8_url.split("/")[-1]
    url = m3u8_url[:len(m3u8_url)-len(m3u8_file)]

    TS_DIR = "./ts_files/"
    shutil.rmtree(TS_DIR, ignore_errors=True)

    results = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_to_url = [executor.submit(download_file, url + seg["uri"], TS_DIR) for seg in m3u8_master.data["segments"]]

        for future in tqdm(as_completed(future_to_url), total=len(future_to_url), desc=filename):
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


def download_file(url, savedir, filename=None, show_status=False):
    if filename is None:
        filename = url.split("/")[-1]
    
    if os.path.exists(savedir + filename):
        return

    os.makedirs(savedir, exist_ok=True)

    r = requests.get(url, stream=True)

    if show_status:
        total = int(r.headers.get('content-length', 0))
        progress_bar = tqdm(total=total, unit='iB', unit_scale=True, desc=filename)

    with open(savedir + filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if show_status:
                progress_bar.update(len(chunk))
            f.write(chunk)
    
    if show_status:
        progress_bar.close()


def main():
    print("Retrieving video files...")
    for video in videos:
        get_ts_stream(video["url"], video["dir"], video["name"])

    print("Retrieving PDF files...")
    for pdf in pdfs:
        download_file(pdf["url"], pdf["dir"], pdf["name"], show_status=True)


if __name__ == "__main__":
    main()
