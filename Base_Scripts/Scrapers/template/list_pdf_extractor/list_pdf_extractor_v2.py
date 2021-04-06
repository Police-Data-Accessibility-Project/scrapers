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
from bs_scrapers.extract_info import extract_info

cur_dir = os.getcwd()
save_dir = cur_dir + "/data/"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

html_page = requests.get(configs.webpage).text
soup = BeautifulSoup(html_page, "html.parser")

url_name = []

try:
    os.remove("url_name.txt")
except FileNotFoundError:
    pass
extract_info(soup, configs)
get_files(save_dir, configs.sleep_time)
