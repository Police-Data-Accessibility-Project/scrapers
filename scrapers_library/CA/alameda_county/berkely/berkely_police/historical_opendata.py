import os
import sys

from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.opendata.opendata_scraper import \
    opendata_scraper

# Change to what you need (remove what you don't)
url_table = [
    "https://data.cityofberkeley.info/resource/efkp-2py4.csv",
]

# Change to what you need (remove what you don't)
save_table = ["annual_part1/"]
save_folder = "./data/"

opendata_scraper(url_table, save_table, save_folder, save_subfolder=True)
