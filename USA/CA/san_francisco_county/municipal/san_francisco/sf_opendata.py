import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper

# Change to what you need (remove what you don't)
url_table = [
    "https://data.sfgov.org/resource/wg3w-h783.csv",
    "https://data.sfgov.org/resource/hz9m-tj6z.csv",
    "https://data.sfgov.org/api/views/hz9m-tj6z/files/b60ee24c-ae7e-4f0b-a8d5-8f4bd29bf1de?download=true&filename=Radio%20Codes%202016.xlsx",
    "https://data.sfgov.org/resource/tmnf-yvry.csv",
    "https://data.sfgov.org/resource/ci9u-8awy.csv",
]

# Change to what you need (remove what you don't)
save_table = [
    "incident_reports/",
    "cfs/",
    "cfs/radio_codes/",
    "incident_reports/historical_2003-may_2018/",
    "incident_codes/",
]
save_folder = "./data/"

opendata_scraper(
    url_table, save_table, save_folder, save_subfolder=True, dictionary=False
)
