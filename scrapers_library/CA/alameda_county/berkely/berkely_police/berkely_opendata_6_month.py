import os
import sys

from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.opendata.opendata_scraper import \
    opendata_scraper

save_url = [
    [
        "cfs/",
        "https://data.cityofberkeley.info/resource/k2nh-s5h5.csv"
    ]
]
save_folder = "./data/"

opendata_scraper(url_table, save_table, save_folder, save_subfolder=True)
