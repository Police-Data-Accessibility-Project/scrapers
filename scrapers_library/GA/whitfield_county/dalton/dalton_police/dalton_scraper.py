import os
import re
import sys
import time
import urllib

import requests
from bs4 import BeautifulSoup
from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_utils.get_files import get_files

cur_dir = os.getcwd()
save_dir = cur_dir + "/data/"
sleep_time = 5

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

html_page = requests.get("http://daltonpd.com/statistics/").text
soup = BeautifulSoup(html_page, "html.parser")


url_name = []


def extract_info(soup):
    for link in soup.findAll("a"):
        if link.get("href") is None:
            continue
        if not link["href"].startswith("http://daltonpd.com/wp-content/uploads/"):
            continue
        url = str(link["href"])
        name = url[url.rindex("/") :]
        # name = name[:name.rindex('.')]
        with open("url_name.txt", "a") as output:
            output.write(url + ", " + name + "\n")
    print("Done")


try:
    os.remove("url_name.txt")
except FileNotFoundError:
    pass

extract_info(soup)
get_files(save_dir, sleep_time)
