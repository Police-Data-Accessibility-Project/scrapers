import os
import sys

from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.opendata.opendata_scraper_2 import opendata_scraper2

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
# Crawl-delay is 1, so no need to set it.
opendata_scraper2(save_url, save_folder, save_subfolder=True)
