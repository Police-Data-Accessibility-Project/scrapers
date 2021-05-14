import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper

# Change to what you need (remove what you don't)
url_table = [
    "https://data.cityofberkeley.info/resource/k2nh-s5h5.csv",
    "https://data.cityofberkeley.info/resource/xi7q-nji6.csv",
    "https://data.cityofberkeley.info/resource/7ykt-c32j.csv",
    "https://data.cityofberkeley.info/resource/ysvs-bcge.csv",
    "https://data.cityofberkeley.info/api/views/ysvs-bcge/files/d446295a-fe8f-4574-b22f-a8b4d097c977?download=true&filename=Action_Taken.xlsx",
]

# Change to what you need (remove what you don't)
save_table = [
    "cfs/",
    "arrests/",
    "jail_bookings/",
    "stop_data/",
    "stop_data/action_taken/",
]
save_folder = "./data/"

opendata_scraper(url_table, save_table, save_folder, save_subfolder=True)
