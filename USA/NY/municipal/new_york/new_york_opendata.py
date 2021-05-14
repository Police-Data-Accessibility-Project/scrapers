import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[4]
sys.path.insert(1, str(p))

from common import opendata_scraper2

# Change to what you need (remove what you don't)
save_url = [
    [
        "crime_data/",
        "https://data.cityofnewyork.us/api/views/5uac-w243/rows.csv?accessType=DOWNLOAD",
    ],
    [
        "crime_data/historic",
        "https://data.cityofnewyork.us/api/views/57mv-nv28/rows.csv?accessType=DOWNLOAD",
    ],
]
save_folder = "./data/"

# Crawl-delay is 1, so no need to set it.
opendata_scraper2(save_url, save_folder, save_subfolder=True)
