import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper2

save_url = [
    [
        "police_incidents/2018/",
        "https://opendata.arcgis.com/datasets/58e6f399e0f04c568b3ba45086d15818_0.csv",
    ],
    [
        "police_incidents/2016/",
        "https://opendata.arcgis.com/datasets/0b12e290edb64816a7cd5270fdd6bacb_0.csv",
    ],
    [
        "police_incidents/2019/",
        "https://opendata.arcgis.com/datasets/8cd15449ac344aa5a55be7840d67c52d_0.csv",
    ],
    [
        "police_incidents/2015/",
        "https://opendata.arcgis.com/datasets/08ff2c3bec594dd2a7a8566b2a81d452_0.csv",
    ],
]

save_folder = "./data/"

# Optional argument `sleep_time` should be set to the site's crawl-delay,
# which can be found in their robots.txt file_name, default time is 1
opendata_scraper2(save_url, save_folder, sleep_time=1)
