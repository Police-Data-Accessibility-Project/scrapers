from itertools import chain
import json
import sys
from typing import Any

from from_root import from_root
from tqdm import tqdm

p = from_root("CONTRIBUTING.md").parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.ckan.ckan_scraper import (
    ckan_package_search,
    ckan_group_package_show,
    ckan_collection_search,
    ckan_package_search_from_organization,
)
from search_terms import package_search, group_search, organization_search


def get_collection_child_packages(
    results: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    new_list = []

    for result in tqdm(results):
        if "extras" in result.keys():
            collections = [
                ckan_collection_search(
                    base_url="https://catalog.data.gov/dataset/",
                    collection_id=result["id"],
                )
                for extra in result["extras"]
                if extra["key"] == "collection_metadata" and extra["value"] == "true"
            ]

            if collections:
                new_list += collections[0]
                continue

        new_list.append(result)

    return new_list


def main():
    results = []

    for search in package_search:
        results += [
            ckan_package_search(base_url=search["url"], query=query) for query in search["terms"]
        ]

    for search in group_search:
        results += [
            ckan_group_package_show(base_url=search["url"], id=id) for id in search["ids"]
        ]

    for search in organization_search:
        results += [
            ckan_package_search_from_organization(
                base_url=search["url"], organization_id=id
            )
            for id in search["ids"]
        ]

    flat_list = list(chain(*results))
    print(json.dumps(flat_list, indent=4))
    # Deduplicate entries
    flat_list = [i for n, i in enumerate(flat_list) if i not in flat_list[n + 1 :]]
    print(len(flat_list))
    print("Retrieving collections...")
    flat_list = get_collection_child_packages(flat_list)
    # print(json.dumps(results, indent=4))


if __name__ == "__main__":
    main()

    '''result = ckan_package_search(
        "https://data.milwaukee.gov/", 'organizations:669a5b7d-697c-4fab-8864-0b5cc4dcd63c'
    )
    print(json.dumps(result, indent=4))
    print(len(result))'''