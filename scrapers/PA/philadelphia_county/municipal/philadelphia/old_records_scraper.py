import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from scrapers.data_portals.opendata.opendata_scraper_2 import opendata_scraper2

# Change to what you need (remove what you don't)
url_save = [
    [
        "vehicle_ped_investigations/2014/",
        "https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20car_ped_stops%20WHERE%20datetimeoccur%20%3E=%20%272014-01-01%27%20AND%20datetimeoccur%20%3C%20%272015-01-01%27",
    ],
    [
        "vehicle_ped_investigations/2015/",
        "https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20car_ped_stops%20WHERE%20datetimeoccur%20%3E=%20%272015-01-01%27%20AND%20datetimeoccur%20%3C%20%272016-01-01%27",
    ],
    [
        "vehicle_ped_investigations/2016/",
        "https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20car_ped_stops%20WHERE%20datetimeoccur%20%3E=%20%272016-01-01%27%20AND%20datetimeoccur%20%3C%20%272017-01-01%27",
    ],
    [
        "vehicle_ped_investigations/2017/",
        "https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20car_ped_stops%20WHERE%20datetimeoccur%20%3E=%20%272017-01-01%27%20AND%20datetimeoccur%20%3C%20%272018-01-01%27",
    ],
    [
        "vehicle_ped_investigations/2018/",
        "https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20car_ped_stops%20WHERE%20datetimeoccur%20%3E=%20%272018-01-01%27%20AND%20datetimeoccur%20%3C%20%272019-01-01%27",
    ],
    [
        "vehicle_ped_investigations/2019/",
        "https://phl.carto.com/api/v2/sql?filename=car_ped_stops&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20car_ped_stops%20WHERE%20datetimeoccur%20%3E=%20%272019-01-01%27%20AND%20datetimeoccur%20%3C%20%272020-01-01%27",
    ],
    [
        "crime_incidents/2006/",
        "https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272006-01-01%27%20AND%20dispatch_date_time%20%3C%20%272007-01-01%27",
    ],
    [
        "crime_incidents/2007/",
        "https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272007-01-01%27%20AND%20dispatch_date_time%20%3C%20%272008-01-01%27",
    ],
    [
        "crime_incidents/2008/",
        "https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272009-01-01%27%20AND%20dispatch_date_time%20%3C%20%272010-01-01%27",
    ],
    [
        "crime_incidents/2009/",
        "https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272010-01-01%27%20AND%20dispatch_date_time%20%3C%20%272011-01-01%27",
    ],
    [
        "crime_incidents/2010/",
        "https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272011-01-01%27%20AND%20dispatch_date_time%20%3C%20%272012-01-01%27",
    ],
    [
        "crime_incidents/2011/",
        "https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272012-01-01%27%20AND%20dispatch_date_time%20%3C%20%272013-01-01%27",
    ],
    [
        "crime_incidents/2012/",
        "https://phl.carto.com/api/v2/sql?filename/home/kali/github/PDAP-Scrapers/scrapers/PA/philadelphia_county/municipal/philadelphia=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272013-01-01%27%20AND%20dispatch_date_time%20%3C%20%272014-01-01%27",
    ],
    [
        "crime_incidents/2013/",
        "https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272014-01-01%27%20AND%20dispatch_date_time%20%3C%20%272015-01-01%27",
    ],
    [
        "crime_incidents/2014/",
        "https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272015-01-01%27%20AND%20dispatch_date_time%20%3C%20%272016-01-01%27",
    ],
    [
        "crime_incidents/2015/",
        "https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272016-01-01%27%20AND%20dispatch_date_time%20%3C%20%272017-01-01%27",
    ],
    [
        "crime_incidents/2016/",
        "https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272017-01-01%27%20AND%20dispatch_date_time%20%3C%20%272018-01-01%27",
    ],
    [
        "crime_incidents/2017/",
        "https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272018-01-01%27%20AND%20dispatch_date_time%20%3C%20%272019-01-01%27",
    ],
    [
        "crime_incidents/2018/",
        "https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272019-01-01%27%20AND%20dispatch_date_time%20%3C%20%272020-01-01%27",
    ],
    [
        "crime_incidents/2019",
        "https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272020-01-01%27%20AND%20dispatch_date_time%20%3C%20%272021-01-01%27",
    ],
]

save_folder = "./data/"

opendata_scraper2(url_save, save_folder, save_subfolder=True, sleep_time=10)
