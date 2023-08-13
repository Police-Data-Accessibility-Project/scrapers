import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from scrapers.data_portals.opendata.opendata_scraper_2 import opendata_scraper2

# Change to what you need (remove what you don't)
save_url = [
    ["hate_crimes/", "https://lky-open-data.s3.amazonaws.com/LMPD/LMPD_OP_BIAS.csv"],
    [
        "assaulted_officers/",
        "https://lky-open-data.s3.amazonaws.com/LMPD/AssaultedOfficerData.csv",
    ],
    [
        "crime_data/",
        "https://data.louisvilleky.gov/sites/default/files/27091/Crime_Data_2019.csv",
    ],
    [
        "employee_characteristics/",
        "https://lky-open-data.s3.amazonaws.com/LMPD/LMPD_Demographics.csv",
    ],
    [
        "uniform_citation_data/",
        "https://data.louisvilleky.gov/sites/default/files/UniformCitationData%20.csv",
    ],
    ["stops_data/", "https://lky-open-data.s3.amazonaws.com/LMPD/LMPD_STOPS_DATA.CSV"],
    [
        "firearm_intake/normalized_addresses/",
        "https://data.louisvilleky.gov/sites/default/files/Firearm%20Data_normalized_addresses.csv",
    ],
    [
        "firearm_intake/intersections/",
        "https://data.louisvilleky.gov/sites/default/files/fiream_data_intersections_reprocessed.csv",
    ],
]

save_folder = "./data/"


opendata_scraper2(save_url, save_folder, save_subfolder=True, sleep_time=10)
