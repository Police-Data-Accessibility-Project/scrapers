from concurrent.futures import as_completed, ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime
import math
import sys

import time
from typing import Any, Optional
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from ckanapi import RemoteCKAN
import requests


@dataclass
class Package:
    base_url: str = ""
    url: str = ""
    title: str = ""
    agency_name: str = ""
    description: str = ""
    supplying_entity: str = ""
    record_format: list = field(default_factory=lambda: [])
    data_portal_type: str = ""
    source_last_updated: str = ""

    def to_dict(self):
        return {
            "source_url": self.url,
            "submitted_name": self.title,
            "agency_name": self.agency_name,
            "description": self.description,
            "supplying_entity": self.supplying_entity,
            "record_format": self.record_format,
            "data_portal_type": self.data_portal_type,
            "source_last_updated": self.source_last_updated,
        }


def ckan_package_search(
    base_url: str,
    query: Optional[str] = None,
    rows: Optional[int] = sys.maxsize,
    start: Optional[int] = 0,
    **kwargs,
) -> list[dict[str, Any]]:
    """Performs a CKAN package (dataset) search from a CKAN data catalog URL.

    :param base_url: Base URL to search from. e.g. "https://catalog.data.gov/"
    :param query: Search string, defaults to None. None will return all packages.
    :param rows: Maximum number of results to return, defaults to maximum integer.
    :param start: Offsets the results, defaults to 0.
    :param kwargs: See https://docs.ckan.org/en/2.10/api/index.html#ckan.logic.action.get.package_search for additional arguments.
    :return: List of dictionaries representing the CKAN package search results.
    """
    remote = RemoteCKAN(base_url, get_only=True)
    results = []
    offset = start
    rows_max = 1000  # CKAN's package search has a hard limit of 1000 packages returned at a time by default

    while start < rows:
        num_rows = rows - start + offset
        packages = remote.action.package_search(
            q=query, rows=num_rows, start=start, **kwargs
        )
        # Add the base_url to each package
        [package.update(base_url=base_url) for package in packages["results"]]
        results += packages["results"]

        total_results = packages["count"]
        if rows > total_results:
            rows = total_results

        result_len = len(packages["results"])
        # Check if the website has a different rows_max value than CKAN's default
        if result_len != rows_max and start + rows_max < total_results:
            rows_max = result_len

        start += rows_max

    return results


def ckan_package_search_from_organization(
    base_url: str, organization_id: str
) -> list[dict[str, Any]]:
    """Returns a list of CKAN packages from an organization. Only 10 packages are able to be returned.

    :param base_url: Base URL of the CKAN portal. e.g. "https://catalog.data.gov/"
    :param organization_id: The organization's ID.
    :return: List of dictionaries representing the packages associated with the organization.
    """
    remote = RemoteCKAN(base_url, get_only=True)
    organization = remote.action.organization_show(
        id=organization_id, include_datasets=True
    )
    packages = organization["packages"]
    results = []

    for package in packages:
        query = f"id:{package['id']}"
        results += ckan_package_search(base_url=base_url, query=query)

    return results


def ckan_group_package_show(
    base_url: str, id: str, limit: Optional[int] = sys.maxsize
) -> list[dict[str, Any]]:
    """Returns a list of CKAN packages from a group.

    :param base_url: Base URL of the CKAN portal. e.g. "https://catalog.data.gov/"
    :param id: The group's ID.
    :param limit: Maximum number of results to return, defaults to maximum integer.
    :return: List of dictionaries representing the packages associated with the group.
    """
    remote = RemoteCKAN(base_url, get_only=True)
    results = remote.action.group_package_show(id=id, limit=limit)
    # Add the base_url to each package
    [package.update(base_url=base_url) for package in results]
    return results


def ckan_collection_search(base_url: str, collection_id: str) -> list[Package]:
    """Returns a list of CKAN packages from a collection.

    :param base_url: Base URL of the CKAN portal before the collection ID. e.g. "https://catalog.data.gov/dataset/"
    :param collection_id: The ID of the parent package.
    :return: List of Package objects representing the packages associated with the collection.
    """
    packages = []
    url = f"{base_url}?collection_package_id={collection_id}"
    soup = _get_soup(url)

    # Calculate the total number of pages of packages
    num_results = int(soup.find(class_="new-results").text.split()[0].replace(",", ""))
    pages = math.ceil(num_results / 20)

    for page in range(1, pages + 1):
        url = f"{base_url}?collection_package_id={collection_id}&page={page}"
        soup = _get_soup(url)

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [
                executor.submit(
                    _collection_search_get_package_data, dataset_content, base_url
                )
                for dataset_content in soup.find_all(class_="dataset-content")
            ]

            [
                packages.append(package.result())
                for package in as_completed(futures)
            ]

        # Take a break to avoid being timed out
        if len(futures) >= 15:
            time.sleep(10)

    return packages


def _collection_search_get_package_data(dataset_content, base_url: str):
    package = Package()
    joined_url = urljoin(base_url, dataset_content.a.get("href"))
    dataset_soup = _get_soup(joined_url)
    # Determine if the dataset url should be the linked page to an external site or the current site
    resources = dataset_soup.find("section", id="dataset-resources").find_all(
        class_="resource-item"
    )
    button = resources[0].find(class_="btn-group")
    if len(resources) == 1 and button is not None and button.a.text == "Visit page":
        package.url = button.a.get("href")
    else:
        package.url = joined_url
        package.data_portal_type = "CKAN"
    package.base_url = base_url
    package.title = dataset_soup.find(itemprop="name").text.strip()
    package.agency_name = dataset_soup.find("h1", class_="heading").text.strip()
    package.supplying_entity = dataset_soup.find(property="dct:publisher").text.strip()
    package.description = dataset_soup.find(class_="notes").p.text
    package.record_format = [
        record_format.text.strip() for record_format in dataset_content.find_all("li")
    ]
    package.record_format = list(set(package.record_format))
    
    date = dataset_soup.find(property="dct:modified").text.strip()
    package.source_last_updated = datetime.strptime(date, "%B %d, %Y").strftime("%Y-%d-%m")
    
    return package


def _get_soup(url: str) -> BeautifulSoup:
    """Returns a BeautifulSoup object for the given URL."""
    time.sleep(1)
    response = requests.get(url)
    return BeautifulSoup(response.content, "lxml")
