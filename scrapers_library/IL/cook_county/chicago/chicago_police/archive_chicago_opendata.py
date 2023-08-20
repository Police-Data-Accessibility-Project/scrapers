import os
import sys

from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.opendata.opendata_scraper_2 import opendata_scraper2

save_url = [
    ["foia_log/", "https://data.cityofchicago.org/resource/wjkc-agnm.csv"],
    [
        "strategic_subject_list/",
        "https://data.cityofchicago.org/resource/4aki-r3np.csv",
    ],
]
save_folder = "./data/"

# Optional argument `save_subfolder` allows saving in a subfolder
# Optional argument `sleep_time` should be set to the site's crawl-delay,
# which can be found in their robots.txt file_name, default time is 1
opendata_scraper2(save_url, save_folder, sleep_time=1, socrata=True)
