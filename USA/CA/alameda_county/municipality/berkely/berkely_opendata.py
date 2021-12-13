import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper

save_url = [
    [
        "cfs/",
        "https://data.cityofberkeley.info/resource/k2nh-s5h5.csv"
    ],
    [
        "arrests/",
        "https://data.cityofberkeley.info/resource/xi7q-nji6.csv"
    ],
    [
        "jail_bookings/",
        "https://data.cityofberkeley.info/resource/7ykt-c32j.csv"
    ],
    [
        "stop_data/",
        "https://data.cityofberkeley.info/resource/ysvs-bcge.csv"
    ],
    [
        "stop_data/action_taken/",
        "https://data.cityofberkeley.info/api/views/ysvs-bcge/files/d446295a-fe8f-4574-b22f-a8b4d097c977?download=true&filename=Action_Taken.xlsx"
    ]
]
save_folder = "./data/"

opendata_scraper(url_table, save_table, save_folder, save_subfolder=True)
