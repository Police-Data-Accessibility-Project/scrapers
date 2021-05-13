import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper

# Change to what you need (remove what you don't)
url_table = [
    "https://data.austintexas.gov/resource/fdj4-gpfu.csv",
    "https://data.austintexas.gov/resource/4bxg-n3iv.csv",
    "https://data.austintexas.gov/resource/dmxv-zsfa.csv",
]

# Change to what you need (remove what you don't)
save_table = [
    "crime_reports/",
    "crime_reports/2017/",
    "hate_crimes/2021/"
]
save_folder = "./data/"

# Optional argument `save_subfolder` allows saving in a subfolder
opendata_scraper(url_table, save_table, save_folder)
