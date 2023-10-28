import os
import sys

import requests
from tqdm import tqdm
from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_scrapers import list_pdf_v3
from utils.pdf.list_pdf_scrapers.single_pdf_scraper import single_pdf_scraper


def get_case():
    save_folder = "./data/ECPD Case 15-22851/"

    if not os.path.exists(save_folder):
       os.makedirs(save_folder)

    print("\nRetrieving ECPD Case 15-22851 media files...")
    for x in tqdm(range(11541, 11638)):
        url = f"https://www.el-cerrito.org/DocumentCenter/View/{x}/"
        r = requests.get(url)

        if not r.ok:
            continue

        file_name = r.url.rsplit("/", 1)[-1]
        file_name = file_name.replace("?bidId=", "")
        file_path = save_folder + file_name

        if os.path.exists(file_path):
            continue

        with open(file_path, "wb") as fd:
            for chunk in r.iter_content():
                fd.write(chunk)


def main():  
    save_dir = "./data/Administrative Investigation 12-21/"
    configs = {
        "webpage": "https://www.el-cerrito.org/1343/Administrative-Investigation-12-21",
        "web_path": "/DocumentCenter/View/",
        "domain_included": False,
        "domain": "https://www.el-cerrito.org/",
        "sleep_time": 5,
    }
    list_pdf_v3(configs, save_dir)

    get_case()

    url = "https://www.el-cerrito.org/DocumentCenter/View/11676/Public-Record-2003"
    save_dir = "./data/Public Record 2003/"
    single_pdf_scraper(save_dir, url)

    url = "https://www.el-cerrito.org/DocumentCenter/View/14043/UAS-Policy-04062020"
    save_dir = "./data/UAS Policy/"
    single_pdf_scraper(save_dir, url)

if __name__ == "__main__":
    main()