import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper2

# Change to what you need (remove what you don't)
url_save = [
    ["cfs/archive_2014-2016/", "https://data.cincinnati-oh.gov/resource/4v9f-u3ia.csv"],
]

# Change to what you need (remove what you don't)

save_folder = "./data/"

opendata_scraper2(url_save, save_folder, save_subfolder=True)
