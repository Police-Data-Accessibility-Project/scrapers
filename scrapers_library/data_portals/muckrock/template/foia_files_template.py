import sys

from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.muckrock.muckrock_scraper import get_foia_files

save_folder = "./data/"
url = "https://www.muckrock.com/foi/pittsburgh-130/traffic-stops-140596/#files" # Replace with your own link

get_foia_files(save_folder, url)
