import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from scrapers.data_portals.opendata.opendata_scraper_2 import opendata_scraper2
from common.utils import get_xls

save_url = [
    [
        "incident_blotter_archive/2005-2015/", 
        "https://data.wprdc.org/dataset/5e6711a3-90e5-457d-8c73-445fb5f363e2/resource/391942e2-25ef-43e4-8263-f8519fa8aada/download/archive-police-blotter.csv"
    ],
    [
        "incident_blotter_archive/2016-present/",
        "https://data.wprdc.org/datastore/dump/044f2016-1dfd-4ab0-bc1e-065da05fca2e"
    ],
    [
        "incident_blotter_30day/",
        "https://data.wprdc.org/datastore/dump/1797ead8-8262-41cc-9099-cbc8a161924b"
    ],
    [
        "officer_training/",
        "https://data.wprdc.org/datastore/dump/1f047ff9-c2ae-45cf-af7e-7eb6d33babd7"
    ],
    [
        "arrest_data/",
        "https://data.wprdc.org/datastore/dump/e03a89dd-134a-4ee8-a2bd-62c40aeebc6f"
    ],
    [
        "firearm_seizures/",
        "https://data.wprdc.org/datastore/dump/e967381d-d7e9-48e3-a2a2-39262f7fa5c4"
    ],
    [
        "non_traffic_citations/",
        "https://data.wprdc.org/datastore/dump/6b11e87d-1216-463d-bbd3-37460e539d86"
    ]
]

save_folder = "./data/"

opendata_scraper2(save_url, save_folder, sleep_time=15)

save_dir = "./data/officer_training/"
file_name = "training-report-hours-total.xls"
url = "https://data.wprdc.org/dataset/8a7d1d09-c8d3-4a0b-9812-11f72bb22103/resource/8c810512-007e-4d10-bfb9-a027a4fd682c/download/training-report-hours-total.xls"

get_xls(save_dir, file_name, url, sleep_time=15)
