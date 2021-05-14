import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[4]
sys.path.insert(1, str(p))

from common import opendata_scraper

# Change to what you need (remove what you don't)
url_table = [
    "https://data.cityofnewyork.us/api/views/5uac-w243/rows.csv?accessType=DOWNLOAD",
    "https://data.cityofnewyork.us/api/views/57mv-nv28/rows.csv?accessType=DOWNLOAD",

]

# Change to what you need (remove what you don't)
save_table = [
    "crime_data/", # called "complaints" on website
    "crime_data/historic",
]
save_folder = "./data/"

opendata_scraper(url_table, save_table, save_folder, save_subfolder=True)
