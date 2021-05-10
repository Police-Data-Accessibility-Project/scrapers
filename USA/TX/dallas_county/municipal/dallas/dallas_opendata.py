import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper

# Change to what you need (remove what you don't)
url_table = [
    "https://www.dallasopendata.com/resource/4gmt-jyx2.csv",
    "https://www.dallasopendata.com/resource/qv6i-rri7.csv",
    "https://www.dallasopendata.com/resource/9fxf-t2tr.csv",
    "https://www.dallasopendata.com/resource/sdr7-6v3j.csv",
]

# Change to what you need (remove what you don't)
save_table = [
    "officer_involved_shootings/",
    "police_incidents/",
    "active_calls/",
    "arrests/",
]
save_folder = "./data/"

opendata_scraper(url_table, save_table, save_folder)
