import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from scrapers_library.data_portals.opendata.opendata_scraper import opendata_scraper

save_url = [
    [
        "cfs/",
        "https://data.cityofberkeley.info/resource/k2nh-s5h5.csv"
    ]
]
save_folder = "./data/"

opendata_scraper(url_table, save_table, save_folder, save_subfolder=True)
