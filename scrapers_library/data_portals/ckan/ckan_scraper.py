import sys
from typing import Any, Optional

from ckanapi import RemoteCKAN


def ckan_package_search(
    base_url: str,
    query: Optional[str] = None,
    rows: Optional[int] = sys.maxsize,
    start: Optional[int] = 0,
    **kwargs
) -> list[dict[str, Any]]:
    """Performs a CKAN package search from a CKAN data catalog URL.

    :param base_url: Base URL to search from. e.g. "https://catalog.data.gov/"
    :param query: Search string, defaults to None. None will return all packages.
    :param rows: Maximum number of results to return, defaults to maximum integer.
    :param start: Offsets the results, defaults to 0
    :param kwargs: See https://docs.ckan.org/en/2.10/api/index.html#ckan.logic.action.get.package_search for additional arguments.
    :return: List of dictionaries representing the CKAN package search results.
    """    
    remote = RemoteCKAN(base_url, get_only=True)
    results = []
    offset = start
    rows_max = 1000 # CKAN's package search has a hard limit of 1000 packages returned at a time by default

    while start < rows:
        num_rows = rows - start + offset
        packages = remote.action.package_search(q=query, rows=num_rows, start=start, **kwargs)
        results += packages["results"]

        total_results = packages["count"]
        if rows > total_results:
            rows = total_results

        result_len = len(packages["results"])
        if result_len != rows_max and start + rows_max < total_results:
            rows_max = result_len

        start += rows_max
