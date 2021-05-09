import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper

url_table = [
    "https://egis.baltimorecity.gov/egis/rest/services/GeoSpatialized_Tables/Part1_Crime/FeatureServer/0/query?where=1%3D1&outFields=CrimeDateTime,CrimeCode,Location,Description,Inside_Outside,Weapon,Post,District,Neighborhood,GeoLocation,Premise,VRIName,Total_Incidents&returnGeometry=false&outSR=4326&f=json",
    "https://egis.baltimorecity.gov/egis/rest/services/GeoSpatialized_Tables/Arrest/FeatureServer/0/query?where=1%3D1&outFields=ArrestNumber,Age,Gender,Race,ArrestDateTime,ArrestLocation,IncidentOffence,IncidentLocation,Charge,ChargeDescription,District,Post,Neighborhood,GeoLocation&returnGeometry=false&outSR=4326&f=json",
    "https://opendata.baltimorecity.gov/egis/rest/services/NonSpatialTables/CallsForService_2021_Present/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=false&outSR=4326&f=json",
    "https://services1.arcgis.com/UWYHeuuJISiGmgXx/arcgis/rest/services/911_Calls_For_Service_2018_csv/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=false&outSR=4326&f=json",
    "https://services1.arcgis.com/UWYHeuuJISiGmgXx/arcgis/rest/services/911_Calls_For_Service_2020_csv/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=false&outSR=4326&f=json",
    "https://services1.arcgis.com/UWYHeuuJISiGmgXx/arcgis/rest/services/911_Calls_For_Service_2019_csv/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=false&outSR=4326&f=json",
]
save_table = [
    "part1_crime/",
    "arrests/",
    "CFS_2021/",
    "CFS_2018/",
    "CFS_2020/",
    "CFS_2019/",
]
save_folder = "./data/"

opendata_scraper(url_table, save_table, save_folder)
