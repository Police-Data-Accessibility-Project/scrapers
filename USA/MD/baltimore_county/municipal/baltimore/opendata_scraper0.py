import requests
import os
import sys
from datetime import date
from pathlib import Path
import json

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common.utils import page_update

url_table = ["https://egis.baltimorecity.gov/egis/rest/services/GeoSpatialized_Tables/Part1_Crime/FeatureServer/0/query?where=1%3D1&outFields=CrimeDateTime,CrimeCode,Location,Description,Inside_Outside,Weapon,Post,District,Neighborhood,GeoLocation,Premise,VRIName,Total_Incidents&returnGeometry=false&outSR=4326&f=json", "https://egis.baltimorecity.gov/egis/rest/services/GeoSpatialized_Tables/Arrest/FeatureServer/0/query?where=1%3D1&outFields=ArrestNumber,Age,Gender,Race,ArrestDateTime,ArrestLocation,IncidentOffence,IncidentLocation,Charge,ChargeDescription,District,Post,Neighborhood,GeoLocation&returnGeometry=false&outSR=4326&f=json", "https://opendata.baltimorecity.gov/egis/rest/services/NonSpatialTables/CallsForService_2021_Present/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=false&outSR=4326&f=json"]
save_table = ["part1_crime/", "arrests/", "CFS_2021/"]

save_folder = "./data/"

for i, row in enumerate(url_table):

    response = requests.get(url_table[i])

    # this could be achieved by using the "Return Count Only" option when generating the query
    updated = page_update(response, save_folder+save_table[i], loop=True)
    print("Update bool: " + str(updated))

    if updated:
        parsed = json.loads(response.text)
        date_name = date.today()
        file_name = str(date_name).replace("-", "_") + "_" + save_table[i].strip("/")

        with open(save_folder + save_table[i] + file_name + ".json","w") as output:
            output.write(json.dumps(parsed, indent=4, sort_keys=False))
