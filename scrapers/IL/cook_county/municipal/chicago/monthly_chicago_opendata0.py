import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from scrapers.data_portals.opendata.opendata_scraper_2 import opendata_scraper2

save_url = [
    [
        "police_sentiment_scores/",
        "https://data.cityofchicago.org/resource/28me-84fj.csv",
    ],
    ["copa_cases/summary/", "https://data.cityofchicago.org/resource/mft5-nfa8.csv"],
    ["copa_cases/by_officer/", "https://data.cityofchicago.org/resource/ufxy-tgry.csv"],
    [
        "copa_cases/by_complainain_subject/",
        "https://data.cityofchicago.org/resource/vnz2-rmie.csv",
    ],
]
save_folder = "./data/"

# Optional argument `save_subfolder` allows saving in a subfolder
# Optional argument `sleep_time` should be set to the site's crawl-delay,
# which can be found in their robots.txt file_name, default time is 1
opendata_scraper2(save_url, save_folder, sleep_time=1, socrata=True)
