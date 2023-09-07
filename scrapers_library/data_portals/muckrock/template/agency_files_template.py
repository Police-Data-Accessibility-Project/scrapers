import sys

from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.muckrock.muckrock_scraper import get_all_agency_files

save_folder = "./data/"
url = "https://www.muckrock.com/agency/pittsburgh-130/pittsburgh-bureau-police-357/" # Replace with your own link

get_all_agency_files(save_folder, url)
