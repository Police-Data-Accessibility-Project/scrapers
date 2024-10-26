from dataclasses import dataclass
import math
import sys
from typing import Any, Optional
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from ckanapi import RemoteCKAN
import requests


@dataclass
class Package:
    url: str = ""
    title: str = ""
    agency_name: str = ""
    description: str = ""


def ckan_package_search(
    base_url: str,
    query: Optional[str] = None,
    rows: Optional[int] = sys.maxsize,
    start: Optional[int] = 0,
    **kwargs
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
    result = remote.action.group_package_show(id=id, limit=limit)
    return result


def ckan_collection_search(base_url: str, collection_id: str) -> list[Package]:
    """Returns a list of CKAN packages from a collection.

    :param base_url: Base URL of the CKAN portal before the collection ID. e.g. "https://catalog.data.gov/dataset/"
    :param collection_id: The ID of the parent package.
    :return: List of Package objects representing the packages associated with the collection.
    """
    packages = []
    # Calculate the total number of pages of packages
    num_results = int(soup.find(class_="new-results").text.split()[0].replace(",", ""))
    pages = math.ceil(num_results / 20)

    for page in range(1, pages + 1):
        url = f"{base_url}?collection_package_id={collection_id}&page={page}"
        soup = get_soup(url)

        # Extract the URL of each dataset from the HTML content
        for pos, dataset_heading in enumerate(soup.find_all(class_="dataset-heading")):
            package = Package()
            joined_url = urljoin(base_url, dataset_heading.a.get("href"))
            dataset_soup = get_soup(joined_url)

            # Determine if the dataset url should be the linked page to an external site or the current site
            resources = dataset_soup.find("section", id="dataset-resources").find_all(class_="resource-item")
            button = resources[0].find(class_="btn-group")
            if len(resources) == 1 and button is not None and button.a.text == "Visit page":
                package.url = button.a.get("href")
            else:
                package.url = joined_url
            
            package.title = dataset_soup.find(itemprop="name").text.strip()
            package.agency_name = dataset_soup.find("h1", class_="heading").text.strip()
            package.description = dataset_soup.find(class_="notes").p.text

            packages.append(package)
    
    return packages


def get_soup(url: str) -> BeautifulSoup:
    """Returns a BeautifulSoup object for the given URL."""
    response = requests.get(url)
    return BeautifulSoup(response.content, "lxml")
