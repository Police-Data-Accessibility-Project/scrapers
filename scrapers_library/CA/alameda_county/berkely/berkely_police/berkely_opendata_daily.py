import os
import sys

from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.opendata.opendata_scraper import \
    opendata_scraper

save_url = [
    [
        "arrests/",
        "https://data.cityofberkeley.info/resource/xi7q-nji6.csv"
    ],
    [
        "jail_bookings/",
        "https://data.cityofberkeley.info/resource/7ykt-c32j.csv"
    ],
]
save_folder = "./data/daily/"

opendata_scraper(url_table, save_table, save_folder, save_subfolder=True)
