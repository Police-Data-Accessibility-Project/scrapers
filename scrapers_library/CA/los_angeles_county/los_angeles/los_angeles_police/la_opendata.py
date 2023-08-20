import os
import sys

from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.opendata.opendata_scraper_2 import \
    opendata_scraper2

save_url = [
    ["crime_data/2020-present/", "https://data.lacity.org/resource/2nrs-mtv8.csv"],
    [
        "vehicle_ped_stop/2010-present/",
        "https://data.lacity.org/resource/ci25-wgt7.csv",
    ],
    ["arrests/2020-present/", "https://data.lacity.org/resource/amvf-fr72.csv"],
    ["response_metrics/citywide/", "https://data.lacity.org/resource/kcsj-s69p.csv"],
    ["cfs/2021/", "https://data.lacity.org/resource/cibt-wiru.csv"],
]

save_folder = "./data/"

# Optional argument `save_subfolder` allows saving in a subfolder
# Optional argument `sleep_time` should be set to the site's crawl-delay,
# which can be found in their robots.txt file_name, default time is 1
opendata_scraper2(save_url, save_folder, sleep_time=1, save_subfolder=True)
