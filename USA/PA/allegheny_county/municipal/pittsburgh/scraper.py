import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper2

save_url = [
#    [
#        "incident_blotter_archive/2005-2015/", 
#        "https://data.wprdc.org/dataset/5e6711a3-90e5-457d-8c73-445fb5f363e2/resource/391942e2-25ef-43e4-8263-f8519fa8aada/download/archive-police-blotter.csv"
#    ],
#    [
#        "incident_blotter_archive/2016-present/",
#        "https://data.wprdc.org/datastore/dump/044f2016-1dfd-4ab0-bc1e-065da05fca2e"
#    ],
#    [
#        "incident_blotter_30day/",
#        "https://data.wprdc.org/datastore/dump/1797ead8-8262-41cc-9099-cbc8a161924b"
#    ],
#    [
#        "officer_training/",
#        "https://data.wprdc.org/datastore/dump/1f047ff9-c2ae-45cf-af7e-7eb6d33babd7"
#    ],
#    [
#        "arrest_data/",
#        "https://data.wprdc.org/datastore/dump/e03a89dd-134a-4ee8-a2bd-62c40aeebc6f"
#    ],
    [
        "firearm_seizures/",
        "https://data.wprdc.org/datastore/dump/e967381d-d7e9-48e3-a2a2-39262f7fa5c4"
    ]
]

save_folder = "./data/"

opendata_scraper2(save_url, save_folder, sleep_time=15)

import etl