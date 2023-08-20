import os
import sys

from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.opendata.opendata_scraper_2 import opendata_scraper2

save_url = [
    ["officer_hires/", "https://stat.stpete.org/resource/9nht-ysk6.csv"],
    ["officer_hires/applications/", "https://stat.stpete.org/resource/gty9-7yu4.csv"],
    ["park_walk_talk/", "https://stat.stpete.org/resource/bk6h-28ux.csv"],
    ["directed_patrols/", "https://stat.stpete.org/resource/9cbi-474e.csv"],
    ["all_tips/", "https://stat.stpete.org/resource/v5at-unyi.csv"],
    ["cfs/monthly_counts/", "https://stat.stpete.org/resource/6373-bvti.csv"],
    [
        "professional_statistics_office/",
        "https://stat.stpete.org/resource/6jpx-t9kn.csv",
    ],
]

save_folder = "./data/"

# Optional argument `sleep_time` should be set to the site's crawl-delay,
# which can be found in their robots.txt file_name, default time is 1
opendata_scraper2(save_url, save_folder, sleep_time=1, socrata=True)
