import requests
import os
from bs4 import BeautifulSoup
import urllib
import re
import time
import sys
from pathlib import Path
p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + '/common')
from base_scrapers.get_files import get_files
from base_scrapers.extract_info import extract_info

def list_pdf_v3(configs, save_dir):

    if not os.path.exists(save_dir):
    	os.makedirs(save_dir)

    html_page = requests.get(configs.webpage).text
    soup = BeautifulSoup(html_page, "html.parser")

    try:
    	os.remove("url_name.txt")
    except FileNotFoundError:
    	pass
    extract_info(soup, configs)
    non_important = configs.non_important
    with open("url_name.txt", 'r') as og_file, open('2url_name.txt', "w") as new_file:
    	for line in og_file:
            if not any(non_important in line.lower() for non_important in non_important):
                new_file.write(line)

    try:
    	os.remove("url_name.txt")
    except FileNotFoundError:
    	pass

    os.rename("2url_name.txt",'url_name.txt')
    get_files(save_dir, configs.sleep_time)
