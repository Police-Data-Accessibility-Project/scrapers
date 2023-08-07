import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper2

save_url = [
    [
        "police_incidents/2021/",
        "https://opendata.arcgis.com/datasets/cb6a8b1d01b74feea5d3f96fa79bb6bf_0.csv",
    ],
    [
        "stop_data/",
        "https://opendata.arcgis.com/datasets/215b4b543d894750aef86c725b56ee2a_0.csv",
    ],
    [
        "shots_fired/",
        "https://opendata.arcgis.com/datasets/f9ae3bef2ccd4792b1835e2744de017f_0.csv",
    ],
]

save_folder = "./data/"

# Optional argument `sleep_time` should be set to the site's crawl-delay,
# which can be found in their robots.txt file_name, default time is 1
opendata_scraper2(save_url, save_folder, sleep_time=60)
