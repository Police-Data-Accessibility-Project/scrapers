import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper

# Change to what you need (remove what you don't)
url_table = [
    "https://opendata.howardcountymd.gov/resource/aas5-u28t.csv",
    "URL2",
]

# Change to what you need (remove what you don't)
save_table = [
    "uof_stats/",
    "arrests/",
]
save_folder = "./data/"

opendata_scraper(url_table, save_table, save_folder)
