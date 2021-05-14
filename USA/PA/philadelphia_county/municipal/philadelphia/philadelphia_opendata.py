import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper2

# Change to what you need (remove what you don't)
url_save = [
    [
        "complaints/",
        "https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppd_complaints&filename=ppd_complaints&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator",
    ],
    [
        "complaints/CAP_findings/",
        "https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppd_complaint_disciplines&filename=ppd_complaint_disciplines&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator",
    ],
    [
        "complaints/complainant_demographics/",
        "https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+ppd_complainant_demographics&filename=ppd_complainant_demographics&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator",
    ],
    [
        "shooting_victims/",
        "https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+shootings&filename=shootings&format=csv&skipfields=cartodb_id",
    ],
    [
        "shooting_victims/geojson/",
        "https://phl.carto.com/api/v2/sql?q=SELECT+*+FROM+shootings&filename=shootings&format=geojson&skipfields=cartodb_id",
    ],
    [
        "vehicle_ped_investigations/2020-present/",
        "https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20car_ped_stops%20WHERE%20datetimeoccur%20%3E=%20%272020-01-01%27",
    ],
    [
        "crime_incidents/2021-2022/",
        "https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272021-01-01%27%20AND%20dispatch_date_time%20%3C%20%272022-01-01%27",
    ],
]

save_folder = "./data/"

opendata_scraper2(url_save, save_folder, save_subfolder=True)
