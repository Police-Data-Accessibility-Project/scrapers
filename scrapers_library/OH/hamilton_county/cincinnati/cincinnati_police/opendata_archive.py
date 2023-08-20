import os
import sys

from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.opendata.opendata_scraper_2 import opendata_scraper2

# Change to what you need (remove what you don't)
save_url = [
    ["cfs/archive_2014-2016/", "https://data.cincinnati-oh.gov/resource/4v9f-u3ia.csv"],
]

# Change to what you need (remove what you don't)

save_folder = "./data/"

opendata_scraper2(save_url, save_folder, save_subfolder=True)
