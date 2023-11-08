import requests
import m3u8
import shutil
import re
import os

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

    for seg in m3u8_master.data["segments"]:
        download_url = url + seg["uri"]
        print(f"downloading {seg['uri']}")
        download_file(download_url)

    TS_DIR = "./ts_files"
    with open("Clip11Knudson1221Protest.ts", "wb") as video:
        dir_list = os.listdir(TS_DIR)
        dir_list.sort(key=lambda f: int("".join(filter(str.isdigit, f))))

        for ts_file in dir_list:
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



