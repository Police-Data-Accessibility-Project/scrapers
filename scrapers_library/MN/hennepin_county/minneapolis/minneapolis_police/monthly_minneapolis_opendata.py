import os
import sys

from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.opendata.opendata_scraper_2 import opendata_scraper2

save_url = [
    [
        "ois/",
        "https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/Police_Officer_Involved_Shootings/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=false&outSR=4326&f=json",
    ],
    [
        "officer_conduct_data/",
        "https://opendata.arcgis.com/datasets/7f54c138c7d745618453fc9f4048d8f1_0.csv",
    ],
]

save_folder = "./data/"

# Optional argument `sleep_time` should be set to the site's crawl-delay,
# which can be found in their robots.txt file_name, default time is 1
opendata_scraper2(save_url, save_folder, sleep_time=60)
