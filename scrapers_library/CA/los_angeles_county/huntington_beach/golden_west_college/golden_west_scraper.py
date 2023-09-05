import os
import re
import sys
import time
import urllib

import requests
from bs4 import BeautifulSoup
from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_utils.get_files import get_files

webpage = "https://www.goldenwestcollege.edu/public-safety/statistics/index.html"
"""
Click the links that lead to the files, and copy their paths. **NOTE:** Ensure that files all match paths, otherwise remove a level until they match
Also ensure that domain stays the same
Verify on page that the href to the file contains the domain, if it doesn't, uncomment domain
"""
web_path = "../../Links/pdf/"
domain = "https://www.goldenwestcollege.edu/"
sleep_time = 5  # Set to desired sleep time
# Are there any links on the page that you do not want? Put a word found in them in this table
non_important = ["emergency", "training", "guidelines"]

cur_dir = os.getcwd()
save_dir = cur_dir + "/data/"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

html_page = requests.get(webpage).text
soup = BeautifulSoup(html_page, "html.parser")

url_name = []


def extract_info(soup):
    for link in soup.findAll("a"):
        if link.get("href") is None:
            continue
        if not link["href"].startswith(web_path):
            continue

        print(link.get("href"))
        url = str(link["href"].lstrip("../"))  # Custom bit here.
        name = url[url.rindex("/") :]

        with open("url_name.txt", "a") as output:
            # output.write(url + ", " + name.strip("/") +"\n")
            # Uncomment following line if domain is not in href, and comment out line above
            output.write(domain + url + ", " + name.strip("/") + "\n")
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
get_files(save_dir, sleep_time)
