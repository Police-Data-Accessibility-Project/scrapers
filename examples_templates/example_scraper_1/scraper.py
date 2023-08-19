import sys

from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from scrapers.data_portals.opendata.opendata_scraper_2 import opendata_scraper2
from utils.file_downloaders.downloaders import get_xls

'''
We used Internet Archive to archive the websites we were scraping the data from to ensure this example scraper will 
still work even if the original website changes or is unavailable. The URLs will look differnent in scrapers that 
scrape directly from a department's website. Archives used were created 8/18/2023.
See /scrapers/PA/allegheny_county/pittsburgh/pittsburgh_police for the unmodified scraper.
'''
save_url = [
    [
        "incident_blotter_archive/2005-2015/", 
        "https://web.archive.org/web/20230819011822/https://data.wprdc.org/datastore/dump/391942e2-25ef-43e4-8263-f8519fa8aada"
    ],
    [
        "incident_blotter_archive/2016-present/",
        "https://web.archive.org/web/20230819005901/https://data.wprdc.org/datastore/dump/044f2016-1dfd-4ab0-bc1e-065da05fca2e"
    ],
    [
        "incident_blotter_30day/",
        "https://web.archive.org/web/20230819005752/https://data.wprdc.org/datastore/dump/1797ead8-8262-41cc-9099-cbc8a161924b"
    ],
    [
        "officer_training/",
        "https://web.archive.org/web/20230819005610/https://data.wprdc.org/datastore/dump/1f047ff9-c2ae-45cf-af7e-7eb6d33babd7"
    ],
    [
        "arrest_data/",
        "https://web.archive.org/web/20230819004435/https://data.wprdc.org/datastore/dump/e03a89dd-134a-4ee8-a2bd-62c40aeebc6f"
    ],
    [
        "firearm_seizures/",
        "https://web.archive.org/web/20230819003305/https://data.wprdc.org/datastore/dump/e967381d-d7e9-48e3-a2a2-39262f7fa5c4"
    ],
    [
        "non_traffic_citations/",
        "https://web.archive.org/web/20230819000300/https://data.wprdc.org/datastore/dump/6b11e87d-1216-463d-bbd3-37460e539d86"
    ]
]

save_folder = "./data/"

opendata_scraper2(save_url, save_folder, sleep_time=15)

save_dir = "./data/officer_training/"
file_name = "training-report-hours-total.xls"
url = "https://web.archive.org/web/20230819011054/https://data.wprdc.org/dataset/8a7d1d09-c8d3-4a0b-9812-11f72bb22103/resource/8c810512-007e-4d10-bfb9-a027a4fd682c/download/training-report-hours-total.xls"

#get_xls(save_dir, file_name, url, sleep_time=15)
