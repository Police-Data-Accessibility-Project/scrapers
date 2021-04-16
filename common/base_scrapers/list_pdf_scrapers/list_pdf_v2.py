import requests
import os
from bs4 import BeautifulSoup
import urllib
import re
import time
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/common")
from list_pdf_utils import get_files
from list_pdf_utils import extract_info


def list_pdf_v2(
    configs,
    save_dir,
    name_in_url=True,
    extract_name=False,
    add_date=False,
    try_overwite=False,
    no_overwrite=False,
):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    html_page = requests.get(configs.webpage).text
    soup = BeautifulSoup(html_page, "html.parser")

    url_name = []

    try:
        os.remove("url_name.txt")
    except FileNotFoundError:
        pass
    extract_info(soup, configs, extract_name=extract_name)
    get_files(save_dir, configs.sleep_time, name_in_url=name_in_url, add_date=add_date)

    # import etl.py
