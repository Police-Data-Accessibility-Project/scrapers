import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper

# Change to what you need (remove what you don't)
url_table = [
    "https://data.cincinnati-oh.gov/resource/gexm-h6bt.csv",
    "https://data.cincinnati-oh.gov/resource/k59e-2pvf.csv",
    "https://data.cincinnati-oh.gov/resource/8us8-wi2w.csv",
    "https://data.cincinnati-oh.gov/resource/bmmy-avxm.csv",
    "https://data.cincinnati-oh.gov/resource/7a3r-kxji.csv",
    "https://data.cincinnati-oh.gov/resource/r6q4-muts.csv",
    "https://data.cincinnati-oh.gov/resource/hibq-hbnj.csv",
    "https://data.cincinnati-oh.gov/resource/ktgf-4sjh.csv",
    "https://data.cincinnati-oh.gov/resource/jx3x-rh6i.csv",
    "https://data.cincinnati-oh.gov/resource/ii65-eyg6.csv",
]

# Change to what you need (remove what you don't)
save_table = [
    "cfs/",
    "crime_incidents/",
    "use_of_force/",
    "assaults_on_officers/",
    "non-cpd_shootings/",
    "police_involved_shootings/",
    "traffic_stops/drivers/",
    "traffic_stops/all_subjs/",
    "ped_stops/",
    "citizen_complaints/",
]

save_folder = "./data/"

opendata_scraper(url_table, save_table, save_folder, save_subfolder=True)
