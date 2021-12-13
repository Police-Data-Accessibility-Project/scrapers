import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper

save_url = [
    [
        "arrests/",
        "https://data.cityofberkeley.info/resource/xi7q-nji6.csv"
    ],
    [
        "jail_bookings/",
        "https://data.cityofberkeley.info/resource/7ykt-c32j.csv"
    ],
]
save_folder = "./data/daily/"

opendata_scraper(url_table, save_table, save_folder, save_subfolder=True)
