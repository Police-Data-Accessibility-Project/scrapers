import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from scrapers_library.data_portals.opendata.opendata_scraper_2 import opendata_scraper2

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
    [
        "police_incidents/2014/",
        "https://opendata.arcgis.com/datasets/f0279f3673394c66a96c03e6e42287f4_0.csv",
    ],
    [
        "police_incidents/2013/",
        "https://opendata.arcgis.com/datasets/944cbb45a5fd4f6dbee2f7136f166184_0.csv",
    ],
    [
        "police_incidents/2012/",
        "https://opendata.arcgis.com/datasets/83508d169ebb48199273d21fef90fb30_0.csv",
    ],
    [
        "police_incidents/2011/",
        "https://opendata.arcgis.com/datasets/657ebd6b1af14af296e1004ed02080d8_0.csv",
    ],
    [
        "police_incidents/2010/",
        "https://opendata.arcgis.com/datasets/6d08a19ce96b42ab844bcf08c70e5480_0.csv",
    ],
    [
        "police_incidents/2018/pims/",
        "https://opendata.arcgis.com/datasets/055e662af18c4488b54dcbd496f897b7_0.csv",
    ],
    [
        "police_incidents/2017/",
        "https://opendata.arcgis.com/datasets/3d33a4f94a004fb5816936708642e045_0.csv",
    ],
    [
        "police_incidents/2020/",
        "https://opendata.arcgis.com/datasets/35c7de976a60450bb894fc7aeb68aef6_0.csv",
    ],
    [
        "uof/",
        "https://opendata.arcgis.com/datasets/6d8110617c4b4971a270ff0834971b89_0.csv",
    ],
]

save_folder = "./data/"

# Optional argument `sleep_time` should be set to the site's crawl-delay,
# which can be found in their robots.txt file_name, default time is 1
opendata_scraper2(save_url, save_folder, sleep_time=60)
