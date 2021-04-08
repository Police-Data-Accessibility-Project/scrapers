import requests
import os
from bs4 import BeautifulSoup
import urllib
import re
import time
import sys
import configs
from configs import non_important
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/common")
from bs_scrapers.get_files import get_files

save_dir =  "./data/"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

html_page = requests.get(configs.webpage).text
soup = BeautifulSoup(html_page, "html.parser")

url_name = []


def extract_info(soup):
    for link in soup.findAll("a"):
        if link.get("href") is None:
            continue
        if not link["href"].startswith(configs.web_path):
            continue

        print(link.get("href"))
        url = str(link["href"].lstrip("../"))
        name = url[url.rindex("/") :]

        with open("url_name.txt", "a") as output:
            if configs.domain_included == True:
                output.write(url + ", " + name.strip("/") + "\n")
            elif configs.domain_included == False:
                # Uncomment following line if domain is not in href, and comment out line above
                output.write(configs.domain + url + ", " + name.strip("/") + "\n")
            else:
                # This section is mostly just to teach the user
                print("ERROR: Booleans must be capitalized, either True or False")
    print("Done")


try:
    os.remove("url_name.txt")
except FileNotFoundError:
    pass
extract_info(soup)

with open("url_name.txt", "r") as og_file, open("2url_name.txt", "w") as new_file:
    for line in og_file:
        if not any(non_important in line.lower() for non_important in non_important):
            new_file.write(line)

try:
    os.remove("url_name.txt")
except FileNotFoundError:
    pass
os.rename("2url_name.txt", "url_name.txt")
get_files(save_dir, configs.sleep_time)
