import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper2

url_save = [
    ["cfs/", "https://data.cincinnati-oh.gov/resource/gexm-h6bt.csv"],
    ["crime_incidents/", "https://data.cincinnati-oh.gov/resource/k59e-2pvf.csv"],
    ["use_of_force/", "https://data.cincinnati-oh.gov/resource/8us8-wi2w.csv"],
    ["assaults_on_officers/", "https://data.cincinnati-oh.gov/resource/bmmy-avxm.csv"],
    ["non-cpd_shootings/", "https://data.cincinnati-oh.gov/resource/7a3r-kxji.csv"],
    [
        "police_involved_shootings/",
        "https://data.cincinnati-oh.gov/resource/r6q4-muts.csv",
    ],
    ["traffic_stops/drivers/", "https://data.cincinnati-oh.gov/resource/hibq-hbnj.csv"],
    [
        "traffic_stops/all_subjs/",
        "https://data.cincinnati-oh.gov/resource/ktgf-4sjh.csv",
    ],
    ["ped_stops/", "https://data.cincinnati-oh.gov/resource/jx3x-rh6i.csv"],
    ["citizen_complaints/", "https://data.cincinnati-oh.gov/resource/ii65-eyg6.csv"],
]

save_folder = "./data/"

opendata_scraper2(url_save, save_folder, save_subfolder=True)
