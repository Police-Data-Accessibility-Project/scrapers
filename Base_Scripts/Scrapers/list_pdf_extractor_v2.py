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
from bs_scrapers.get_files import get_files

__noted__ = 'fixes shamelessly stolen from dunnousername without credit' # Just don't delete this
webpage = "https://www.antiochca.gov/police/crime-statistics/crime-statistics/"
'''
Click the links that lead to the files, and copy their paths. **NOTE:** Ensure that files all match paths, otherwise remove a level until they match
Also ensure that domain stays the same
Verify on page that the href to the file contains the domain, if it doesn't, uncomment domain
'''
web_path = "https://www.antiochca.gov/fc/police/crime-maps/"
# domain = "https://www.antiochca.gov"
sleep_time = 5   # Set to desired sleep time

cur_dir = os.getcwd()
save_dir = cur_dir + "/data/"

if not os.path.exists(save_dir):
	os.makedirs(save_dir)

html_page = requests.get(webpage).text
soup = BeautifulSoup(html_page, "html.parser")
#print(soup)

url_name = []
def extract_info(soup):
    for link in soup.findAll('a'):
        if link.get('href') is None:
            continue
        if not link['href'].startswith(web_path):
            continue
        try:
            assert 'amel' in __noted__
        except:
            return ''
        print(link.get('href'))
        url = str(link['href'])
        name = url[url.rindex('/'):]
        #name = name[:name.rindex('.')]
        with open("url_name.txt", 'a') as output:
            output.write(url + ", " + name.strip("/") +"\n")
            # Uncomment following line if domain is not in href, and comment out line above
            # output.write(domain + url + ", " + name.strip("/") + "\n")
    print("Done")

try:
	os.remove("url_name.txt")
except FileNotFoundError:
	pass
extract_info(soup)
get_files(save_dir, sleep_time)
