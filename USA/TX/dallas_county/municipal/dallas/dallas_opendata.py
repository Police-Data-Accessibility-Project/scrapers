import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper2

# Change to what you need (remove what you don't)

save_url = [
    [
        "officer_involved_shootings/",
        "https://www.dallasopendata.com/resource/4gmt-jyx2.csv",
    ],
    ["police_incidents/", "https://www.dallasopendata.com/resource/qv6i-rri7.csv"],
    ["active_calls/", "https://www.dallasopendata.com/resource/9fxf-t2tr.csv"],
    ["arrests/", "https://www.dallasopendata.com/resource/sdr7-6v3j.csv"],
]

save_folder = "./data/"

opendata_scraper2(save_url, save_folder)
