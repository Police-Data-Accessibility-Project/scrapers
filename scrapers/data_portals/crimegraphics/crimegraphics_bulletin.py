import sys
import os
import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import time
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p))
print(sys.path)
from utils.website_hasher.page_update import hash_comparer, page_hasher, page_update
from scrapers.data_portals.crimegraphics.data_parser import data_parser

# this function is used for gathering time stats
def function_timer(stats):
    if stats:
        return time.perf_counter()


# this function simply calculates and prints the difference between the end and start times
def time_dif(stats, string, start, end):
    if stats:
        print(f"{string}: {end - start} seconds")


# configs = {
#     "url": "",
#     "department_code": "",
# }

# Stats default to False
def crimegraphics_bulletin(configs, save_dir, stats=False, configs_file=False):
    """
    Scrape a crimegraphics [daily] bulletins
    :param configs: dictionary of configuration.
    :param save_dir: directory to save data to
    :param stats: whether you want execution stats (default false)
    :param configs_file: for backwards compatibility, leave it alone (default False)
    """
    if not configs_file:  # Default setting
        department_code = configs["department_code"]
        url = configs["url"]
    else:
        department_code = configs.department_code
        url = configs.url

    # Automatically have the CLERYMenu clicked for daily crime data
    payload = {
        "MYAGCODE": configs.department_code,
        "__EVENTTARGET": "MainMenu$BulletinMenu",
        "__EVENTARGUMENT": "BulletinMenu",
    }

    # Initialize "data" table (a table called data, not a datatable)
    data = []

    print("Receiving Data... Please wait...")
    request_start = function_timer(stats)

    # Send a POST request to the url with our headers
    response = requests.request("POST", configs.url, data=payload)
    request_end = function_timer(stats)
    time_dif(stats, "Request Time", request_start, request_end)

    print("Data received.")
    parse_start = function_timer(stats)

    # Parse the response using bs4
    soup = BeautifulSoup(response.text, "html.parser")
    # with open("html.html", 'wb') as output:
    #     output.write(str(soup).encode('utf-8'))
    # output.close()
    parse_end = function_timer(stats)
    time_dif(stats, "Parse time", parse_start, parse_end)

    search_start = function_timer(stats)

    table = soup.find("span", id="Bull")
    # Send "table" to page_update to be hashed and compared.
    page_update(table)
    search_end = function_timer(stats)
    time_dif(stats, "Search time", search_start, search_end)

    # Import the parser
    data_parser(configs, save_dir, table)
