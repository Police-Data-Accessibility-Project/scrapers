import sys
import os
import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import time
from datetime import date
from pathlib import Path

# This is a hack that loads that root common folder like a module (without you expressly needing to install it).
# I'm going to be honest, I have no clue why it uses parents[1] while the list_pdf scrapesr use parents[3]
p = Path(__file__).resolve().parents[1]
sys.path.insert(1, str(p))

# import hash_comparer, page_hasher, and page_update from common/utils/website_hasher/page_update.py
from common.utils import hash_comparer, page_hasher, page_update

# this function is used for gathering time stats
def function_timer(stats):
    if stats != False:
        return time.perf_counter()


# this function simply calculates and prints the difference between the end and start times
def time_dif(stats, string, start, end):
    if stats != False:
        print(f"{string}: {end - start} seconds")


# stats default to False
def crimegraphics_clery(configs, save_dir, stats=False, configs_file=False):
    if not configs_file:  # Default setting
        department_code = configs["department_code"]
        url = configs["url"]
        list_header = configs["list_header"]
    else:
        department_code = configs.department_code
        url = configs.url
        list_header = configs.list_header

    # automatically have the CLERYMenu clicked for daily crime data
    payload = {
        "MYAGCODE": configs.department_code,
        "__EVENTTARGET": "MainMenu$CLERYMenu",
        "__EVENTARGUMENT": "CLERYMenu",
    }

    # initialize "data" table (a table called data, not a datatable)
    data = []

    print("Receiving Data... Please wait...")

    # used for stats, mark beginning of request
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

    # Use BeautifulSoup4 (bs4)'s find_all method to find all html table rows (tr)
    rows = table.find_all("tr")
    for row in tqdm(rows):
        # Use BeautifulSoup4 (bs4)'s find_all method to find all html tags for table data (td)
        td = row.find_all("td")
        table_data = []
        for actual_data in td:
            table_data.append(actual_data.get_text())
        data.append(table_data)

    date_name = date.today()
    file_name = "_" + str(date_name).replace("-", "_")  # + "_"

    dataframe = pd.DataFrame(data=data, columns=configs.list_header)

    dataframe.to_csv(save_dir + configs.department_code + file_name + "_daily_bulletin")
