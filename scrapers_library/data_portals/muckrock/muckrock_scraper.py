import sys

import requests
from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from utils.file_downloaders.downloaders import get_pdf, get_xls

#https://www.muckrock.com/foi/pittsburgh-130/traffic-stops-140596/#files
#https://www.muckrock.com/api_v1/foia/?agency=&embargo=unknown&format=json&title=Traffic+Stops
#https://www.muckrock.com/foi/kingston-30521/roster-and-hire-dates-143168/#files
#https://www.muckrock.com/agency/pittsburgh-130/pittsburgh-bureau-police-357/

def get_single_file(url):
    get_xls("./data/", "test.xlsx", url, sleep_time=1)


def get_foia_files(url):
    pass


def get_all_agency_files(url):
    pass