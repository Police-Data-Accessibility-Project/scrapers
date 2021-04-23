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

p = Path(__file__).resolve().parents[1]
sys.path.insert(1, str(p))

from common.utils import hash_comparer, page_hasher, page_update
from crimegraphics.utils import data_parser


def function_timer(stats):
    if stats != False:
        return time.perf_counter()


def time_dif(stats, string, start, end):
    if stats != False:
        print(f"{string}: {end - start} seconds")


def crimegraphics_bulletin(configs, save_dir, stats=False):
    # automatically have the CLERYMenu clicked for daily crime data
    payload = {
        "MYAGCODE": configs.department_code,
        "__EVENTTARGET": "MainMenu$BulletinMenu",
        "__EVENTARGUMENT": "BulletinMenu",
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
    # with open("html.html", 'wb') as output:
    #     output.write(str(soup).encode('utf-8'))
    # output.close()
    parse_end = function_timer(stats)
    time_dif(stats, "Parse time", parse_start, parse_end)

    search_start = function_timer(stats)

    table = soup.find("span", id="Bull")
    page_update(table)
    search_end = function_timer(stats)
    time_dif(stats, "Search time", search_start, search_end)

    # Import the parser
    data_parser(configs, save_dir, table)
