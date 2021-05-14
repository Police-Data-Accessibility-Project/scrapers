import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper2

# Change to what you need (remove what you don't)
save_url = [
    ["crime_reports/", "https://data.austintexas.gov/resource/fdj4-gpfu.csv"],
    ["crime_reports/2017/", "https://data.austintexas.gov/resource/4bxg-n3iv.csv"],
    ["hate_crimes/2021/", "https://data.austintexas.gov/resource/dmxv-zsfa.csv"],
    [
        "racial_profiling/motor_vehicle_stops/",
        "https://data.austintexas.gov/resource/9dis-d5bk.csv",
    ],
    ["population_vs_MV_stops/", "https://data.austintexas.gov/resource/87wz-a3h2.csv"],
    ["warning_obs/", "https://data.austintexas.gov/resource/gzfe-bzj4.csv"],
]
save_folder = "./data/"

# Optional argument `save_subfolder` allows saving in a subfolder
opendata_scraper2(save_url, save_folder, save_subfolder=True)
