import requests
import m3u8
import shutil
import re
import os
from concurrent.futures import as_completed, ThreadPoolExecutor
from tqdm import tqdm

'''
def strip_end(text, suffix):
    if not text.endswith(suffix):
        return text
    return text[:len(text)-len(suffix)]
'''

def get_ts_stream():
    m3u8_url = "https://wms.civplus.tikiliveapi.com/rokuvod_civplus/145062/smil:civplus/encoded_streams/0/385/145062.smil/chunklist_w1492225134_b4589629.m3u8"
    r = requests.get(m3u8_url)
    m3u8_master = m3u8.loads(r.text)
    m3u8_file = m3u8_url.split("/")[-1]
    url = m3u8_url[:len(m3u8_url)-len(m3u8_file)]

    if not os.path.exists("ts_files"):
        os.makedirs("ts_files")

    results = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_to_url = [executor.submit(download_file, url + seg["uri"]) for seg in m3u8_master.data["segments"]]

        for future in tqdm(as_completed(future_to_url), total=len(future_to_url), desc="Clip11Knudson1221Protest.ts"):
            data = future.result()
            results.append(data)

    TS_DIR = "./ts_files"
    with open("Clip11Knudson1221Protest.ts", "wb") as video:
        dir_list = os.listdir(TS_DIR)
        dir_list.sort(key=lambda f: int("".join(filter(str.isdigit, f))))

        for ts_file in tqdm(dir_list, desc="Merging segments"):
            with open(f"{TS_DIR}/{ts_file}", "rb") as mergefile:
                shutil.copyfileobj(mergefile, video)

    shutil.rmtree(TS_DIR)


def download_file(url):
    local_filename = url.split("/")[-1]
    r = requests.get(url, stream=True)

    with open(f"ts_files/{local_filename}", "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)


def main():
    get_ts_stream()


if __name__ == "__main__":
    main()
