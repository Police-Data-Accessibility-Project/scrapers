import json
import os
import sys
import time
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup
from from_root import from_root
from tqdm import tqdm

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from utils.website_hasher.page_update import hash_comparer, page_hasher, page_update


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


# stats default to False
def crimegraphics_arrest(configs, save_dir, stats=False, configs_file=False):
    if not configs_file:  # Default setting
        department_code = configs["department_code"]
        url = configs["url"]

    else:
        department_code = configs.department_code
        url = configs.url

    # automatically have the ArrestsMenu clicked for daily crime data
    # txtArrestStartDate and txtArrestEndDate are blank by default, which we may want to be the case here as well.
    payload = {
        "MYAGCODE": configs.department_code,
        "__EVENTTARGET": "MainMenu$ArrestsMenu",
        "__EVENTARGUMENT": "ArrestsMenu",
        "txtArrestStartDate": "02/05/2021",
        "txtArrestEndDate": "04/12/2021",
        "cmdSearchArrests": "Search",
    }

    # Initialize "data" table (a table called data, not a datatable)
    data = []

    print("Receiving Data... Please wait...")

    # Used for stats, mark beginning of request
    request_start = function_timer(stats)

    # Send a POST request to the url with our headers
    response = requests.request("POST", configs.url, data=payload)
    request_end = function_timer(stats)
    time_dif(stats, "Request Time", request_start, request_end)

    print("Data received.")
    parse_start = function_timer(stats)

    # Parse the response using bs4
    soup = BeautifulSoup(response.text, "html.parser")
    with open("html.html", "wb") as output:
        output.write(str(soup).encode("utf-8"))
    output.close()
    parse_end = function_timer(stats)
    time_dif(stats, "Parse time", parse_start, parse_end)

    search_start = function_timer(stats)
    # This website has a bunch of empty tables with the same name
    # The 6th index has the data we need
    table = soup.find_all("table", {"class": "ob_gBody"})[6]
    search_end = function_timer(stats)
    time_dif(stats, "Search time", search_start, search_end)

    hash_start = function_timer(stats)
    # Checks if the page has been updated
    page_update(table)

    hash_end = function_timer(stats)
    time_dif(stats, "Hash time", hash_start, hash_end)

    # Use BeautifulSoup4 (bs4)'s find_all method to find all html table rows (tr)
    rows = table.find_all("tr")
    for row in tqdm(rows):
        # Use BeautifulSoup4 (bs4)'s find_all method to find all html tags for table data (td)
        td = row.find_all("td")
        table_data = []
        for actual_data in td:
            table_data.append(actual_data.get_text())
        data.append(table_data)

    dataframe = pd.DataFrame(data=data, columns=configs.list_header)

    dataframe.to_csv(save_dir + configs.department_code + "_daily_bulletin")
