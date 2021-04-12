import sys
import os
import configs
import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import time
from pathlib import Path

p = Path(__file__).resolve().parents[1]
sys.path.insert(1, str(p) + "/crimegraphics")

from utils.page_update import hash_comparer, page_hasher, page_update


def function_timer(stats):
    if stats != False:
        return time.perf_counter()


def time_dif(stats, string, start, end):
    if stats != False:
        print(f"{string}: {end - start} seconds")


def crimegraphics_scraper(configs, save_dir, stats=False):
    # automatically have the CLERYMenu clicked for daily crime data
    payload = {
        "MYAGCODE": configs.department_code,
        "__EVENTTARGET": "MainMenu$CLERYMenu",
        "__EVENTARGUMENT": "CLERYMenu",
    }
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
    parse_end = function_timer(stats)
    time_dif(stats, "Parse time", parse_start, parse_end)

    search_start = function_timer(stats)
    # this website has a bunch of empty tables with the same name
    # the 6th index has the data we need
    table = soup.find_all("table", {"class": "ob_gBody"})[6]
    search_end = function_timer(stats)
    time_dif(stats, "Search time", search_start, search_end)

    hash_start = function_timer(stats)
    # Checks if the page has been updated
    page_update(table)

    hash_end = function_timer(stats)
    time_dif(stats, "Hash time", hash_start, hash_end)

    rows = table.find_all("tr")
    for row in tqdm(rows):
        td = row.find_all("td")
        table_data = []
        for actual_data in td:
            table_data.append(actual_data.get_text())
        data.append(table_data)

    dataframe = pd.DataFrame(data=data, columns=configs.list_header)

    dataframe.to_csv(save_dir + configs.department_code + "_daily_bulletin")
