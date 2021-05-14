import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper

# Change to what you need (remove what you don't)
url_table = [
    "URL1",
    "URL2",
]

# Change to what you need (remove what you don't)
save_table = [
    "URL1_name/",
    "arrests/",
]
save_folder = "./data/"

# Optional argument `save_subfolder` allows saving in a subfolder
opendata_scraper(url_table, save_table, save_folder)
