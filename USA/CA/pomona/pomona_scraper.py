import requests
import os
from bs4 import BeautifulSoup
import urllib
import re
import time
import sys
import configs
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/common")
from bs_scrapers.get_files import get_files

__noted__ = "fixes shamelessly stolen from dunnousername without credit"  # Just don't delete this

cur_dir = os.getcwd()
save_dir = cur_dir + "/data/"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

html_page = requests.get(configs.webpage).text
soup = BeautifulSoup(html_page, "html.parser")
# print(soup)

url_name = []


def extract_info(soup):
    for link in soup.findAll("a"):
        if link.get("href") is None:
            continue
        if not link["href"].startswith(configs.web_path):
            continue
        print(link.get("href"))
        url = str(link["href"])
        name = url[url.rindex("/") :]
        # name = name[:name.rindex('.')]

        with open("url_name.txt", "a+") as output:
            if url not in output.read():
                if configs.domain_included == True:
                    output.write(url + ", " + name.strip("/") + "\n")
                elif configs.domain_included == False:
                    output.write(configs.domain + url + ", " + name.strip("/") + "\n")
    print("Done")

extract_info(soup)
get_files(save_dir, configs.sleep_time, debug=True)
