import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper

# Change to what you need (remove what you don't)
url_table = [
    "https://data.cincinnati-oh.gov/resource/4v9f-u3ia.csv",
]

# Change to what you need (remove what you don't)
save_table = [
    "cfs/archive_2014-2016/",
]

save_folder = "./data/"

opendata_scraper(url_table, save_table, save_folder, save_subfolder=True)
