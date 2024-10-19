import sys

from from_root import from_root

p = from_root("CONTRIBUTING.md").parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.ckan.ckan_scraper import ckan_package_search

base_url = "http://demo.ckan.org/" # Replace with your own link

results = ckan_package_search(base_url)
