from itertools import chain
import json
import sys

from from_root import from_root
from tqdm import tqdm

p = from_root("CONTRIBUTING.md").parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.ckan.ckan_scraper import (
    ckan_package_search,
    ckan_group_package_show,
    ckan_collection_search,
)
from search_terms import package_search, group_search


def main():
    results = []

    for search in package_search:
        results += [
            ckan_package_search(search["url"], query=query) for query in search["terms"]
        ]

    flat_list = list(chain(*results))
    # Deduplicate entries
    flat_list = [i for n, i in enumerate(flat_list) if i not in flat_list[n + 1 :]]

    print("Retrieving collections...")
    flat_list = [
        (
            [
                ckan_collection_search(
                    base_url="https://catalog.data.gov/dataset/", collection_id=result["id"]
                )
                for extra in result["extras"]
                if extra["key"] == "collection_metadata" and extra["value"] == "true"
            ]
            if "extras" in result.keys()
            else result
        )
        for result in tqdm(flat_list)
    ]
    flat_list = list(chain(*flat_list))

    #print(json.dumps(flat_list, indent=4))
    [print(type(result)) for result in flat_list]
    print(len(flat_list))
    print(flat_list[0])
    print(flat_list[-1])


if __name__ == "__main__":
    main()
    # results = ckan_collection_search(base_url="https://catalog.data.gov/dataset/", collection_id="7b1d1941-b255-4596-89a6-99e1a33cc2d8")
