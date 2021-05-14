import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p))

from common import opendata_scraper

# Change to what you need (remove what you don't)
url_table = [
    "https://opendata.howardcountymd.gov/resource/aas5-u28t.csv",
    "https://opendata.howardcountymd.gov/resource/qccx-65fg.csv",
    "https://opendata.howardcountymd.gov/resource/hrwk-c83k.csv",
]

# Change to what you need (remove what you don't)
save_table = ["uof_stats/", "cfs/", "crime_by_type/"]
save_folder = "./data/"

opendata_scraper(url_table, save_table, save_folder, dictionary=False)
