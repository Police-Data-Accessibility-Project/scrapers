import sys

from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.muckrock.muckrock_scraper import get_single_file

url = "https://cdn.muckrock.com/foia_files/2023/03/27/TrafficStops_2020-2022_RTK129-01-2023.xlsx"

get_single_file(url)