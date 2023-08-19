import sys
import os
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from utils.pdf.list_pdf_scrapers import list_pdf_v2

"""
SETUP HOW-TO:
    Step 1: Set webpage to the page you want to scrape.
    Step 2: Click the links that lead to the files, and copy their paths. **NOTE:** Ensure that files all match paths, otherwise remove a level until they match.
            Also ensure that domain stays the same (I've seen some sites use AWS buckets for one file and an on-site storage method for another)
            Verify on page that the href to the file contains the domain, if it doesn't, add the domain to domain.
    Step 3: If the domain is not in the href, set domain_included to False, otherwise set it to True
    Step 4: If you set domain_included to False, you need to add the domain (from the http(s) to the top level domain (TLD) (.com, .edu, etc),
            otherwise, you can leave it blank.
    Step 5: Set sleep_time to the desired integer. Best practice is to set it to the crawl-delay in a website's `robots.txt`.
            Most departments do not seem to have a crawl-delay specified, so leave it at 5.
    Step 6: (Only applies to list_pdf_v3) If there are any documents that you *don't* want to scrape from the page,
            put the words that are **unique** to them.
    Step 7: "debug" is will make the scraper more verbose, but will generally be unhelpful to the average user. Leave False unless you're having issues.
            "csv_dir" is better explained in the readme.

EXAMPLE CONFIG:
    configs = {
        "webpage": "http://www.beverlyhills.org/departments/policedepartment/crimeinformation/crimestatistics/web.jsp",
        "web_path": "/cbhfiles/storage/files/",
        "domain_included": False,
        "domain": "http://www.beverlyhills.org",
        "sleep_time": 5,
        "non_important": ["emergency", "training", "guidelines"],
        "debug": False,
        "csv_dir": "/csv/",
    }
"""

configs = {
    "webpage": "https://www.minneapolismn.gov/resident-services/public-safety/police-public-safety/police-reports-and-data-requests/frequently-requested/disciplinary-decisions-memoranda/",
    "web_path": "/media/-www-content-assets/documents/",
    "domain_included": False,
    "domain": "https://www.minneapolismn.gov/",
    "sleep_time": 5,
    "debug": False,
    "csv_dir": "/csv/",
}

save_dir = "./data/discipline_worksheets/"

list_pdf_v2(configs, save_dir)
