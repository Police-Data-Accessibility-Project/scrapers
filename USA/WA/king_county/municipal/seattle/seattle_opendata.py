import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper2

save_url = [
    ["in_car_video_dropped_frames/", "https://data.seattle.gov/resource/k7a5-emiw.csv"],
    [
        "police_accountability_office/complaints",
        "https://data.seattle.gov/resource/99yi-dthu.csv",
    ],
    ["disciplinary_appeals/", "https://data.seattle.gov/resource/2qns-g7s7.csv"],
    ["call_data/", "https://data.seattle.gov/resource/33kz-ixgy.csv"],
    ["terry_stops/", "https://data.seattle.gov/resource/28ny-9ts8.csv"],
    ["ois/", "https://data.seattle.gov/resource/mg5r-efcm.csv"],
    ["uof/", "https://data.seattle.gov/resource/ppi5-g2bj.csv"],
    ["crisis_data/", "https://data.seattle.gov/resource/i2q9-thny.csv"],
]

save_folder = "./data/"

# Optional argument `sleep_time` should be set to the site's crawl-delay,
# which can be found in their robots.txt file_name, default time is 1
opendata_scraper2(save_url, save_folder, sleep_time=1, socrata=True)
