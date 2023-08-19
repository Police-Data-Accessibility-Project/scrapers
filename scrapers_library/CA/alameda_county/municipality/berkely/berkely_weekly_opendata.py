import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from scrapers_library.data_portals.opendata.opendata_scraper import opendata_scraper

save_url = [
    [
        "stop_data/weekly/",
        "https://data.cityofberkeley.info/resource/4tbf-3yt8.csv"
    ],
]
save_folder = "./data/"

opendata_scraper(url_table, save_table, save_folder, save_subfolder=True)
