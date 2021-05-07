import requests
import os
import sys
from datetime import date
from pathlib import Path
import json

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common.utils import page_update

response = requests.get("https://egis.baltimorecity.gov/egis/rest/services/GeoSpatialized_Tables/Part1_Crime/FeatureServer/0/query?where=1%3D1&outFields=CrimeDateTime,CrimeCode,Location,Description,Inside_Outside,Weapon,Post,District,Neighborhood,GeoLocation,Premise,VRIName,Total_Incidents&returnGeometry=false&outSR=4326&f=json")

save_folder = "./data/"

updated = page_update(response, save_folder+"part1_crime/", loop=True)
print("Update bool: " + str(updated))

if updated:
    parsed = json.loads(response.text)
    date_name = date.today()
    file_name = str(date_name).replace("-", "_") + "_part1_crime"

    with open(save_folder + "part1_crime/" + file_name + ".json","w") as output:
        output.write(json.dumps(parsed, indent=4, sort_keys=False))
