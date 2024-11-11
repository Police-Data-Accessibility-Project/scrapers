"""Retrieves packages from CKAN data portals and parses relevant information then outputs to a CSV file"""
from itertools import chain
import json
import sys
from typing import Any, Callable, Optional

from from_root import from_root
import pandas as pd
from tqdm import tqdm

p = from_root("CONTRIBUTING.md").parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.ckan.ckan_scraper import (
    ckan_package_search,
    ckan_group_package_show,
    ckan_collection_search,
    ckan_package_search_from_organization,
    Package,
)
from search_terms import package_search, group_search, organization_search


def perform_search(
    search_func: Callable,
    search_terms: list[dict[str, Any]],
    results: list[dict[str, Any]],
):
    """Executes a search function with the given search terms.

    :param search_func: The search function to execute.
    :param search_terms: The list of urls and search terms.
    :param results: The list of results.
    :return: Updated list of results.
    """
    key = list(search_terms[0].keys())[1]
    for search in tqdm(search_terms):
        results += [search_func(search["url"], item) for item in search[key]]

    return results


def get_collection_child_packages(
    results: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """Retrieves the child packages of each collection.

    :param results: List of results.
    :return: List of results containing child packages.
    """
    new_list = []

    for result in tqdm(results):
        if "extras" in result.keys():
            collections = [
                ckan_collection_search(
                    base_url="https://catalog.data.gov/dataset/",
                    collection_id=result["id"],
                )
                for extra in result["extras"]
                if extra["key"] == "collection_metadata"
                and extra["value"] == "true"
                and not result["resources"]
            ]

            if collections:
                new_list += collections[0]
                continue

        new_list.append(result)

    return new_list


def filter_result(result: dict[str, Any] | Package):
    """Filters the result based on the defined criteria.

    :param result: The result to filter.
    :return: True if the result should be included, False otherwise.
    """
    if isinstance(result, Package) or "extras" not in result.keys():
        return True

    for extra in result["extras"]:
        # Remove parent packages with no resources
        if (
            extra["key"] == "collection_metadata"
            and extra["value"] == "true"
            and not result["resources"]
        ):
            return False
        # Remove non-public packages
        elif extra["key"] == "accessLevel" and extra["value"] == "non-public":
            return False

    # Remove packages with no data or landing page
    if len(result["resources"]) == 0:
        landing_page = next(
            (extra for extra in result["extras"] if extra["key"] == "landingPage"), None
        )
        if landing_page is None:
            return False

    return True


def parse_result(result: dict[str, Any] | Package) -> dict[str, Any]:
    """Retrieves the important information from the package.

    :param result: The result to parse.
    :return: The parsed result as a dictionary.
    """
    package = Package()

    if isinstance(result, Package):
        package.record_format = get_record_format_list(package)
        return package.to_dict()

    package.record_format = get_record_format_list(
        package=package, resources=result["resources"]
    )

    package = get_source_url(result, package)
    package.title = result["title"]
    package.description = result["notes"]
    package.agency_name = result["organization"]["title"]
    package.supplying_entity = get_supplying_entity(result)
    package.source_last_updated = result["metadata_modified"][0:10]

    return package.to_dict()


def get_record_format_list(
    package: Package,
    resources: Optional[list[dict[str, Any]]] = None,
) -> list[str]:
    """Retrieves the record formats from the package's resources.

    :param package: The package to retrieve record formats from.
    :param resources: The list of resources.
    :return: List of record formats.
    """
    data_types = [
        "CSV",
        "PDF",
        "XLS",
        "XML",
        "JSON",
        "Other",
        "RDF",
        "GIS / Shapefile",
        "HTML text",
        "DOC / TXT",
        "Video / Image",
    ]
    type_conversion = {
        "XLSX": "XLS",
        "Microsoft Excel": "XLS",
        "KML": "GIS / Shapefile",
        "GeoJSON": "GIS / Shapefile",
        "application/vnd.geo+json": "GIS / Shapefile",
        "ArcGIS GeoServices REST API": "GIS / Shapefile",
        "Esri REST": "GIS / Shapefile",
        "SHP": "GIS / Shapefile",
        "OGC WMS": "GIS / Shapefile",
        "QGIS": "GIS / Shapefile",
        "gml": "GIS / Shapefile",
        "WFS": "GIS / Shapefile",
        "WMS": "GIS / Shapefile",
        "API": "GIS / Shapefile",
        "HTML": "HTML text",
        "HTML page": "HTML text",
        "": "HTML text",
        "TEXT": "DOC / TXT",
        "JPEG": "Video / Image",
        "Api": "JSON",
        "CSV downloads": "CSV",
        "csv file": "CSV",
    }

    if resources is None:
        resources = package.record_format
        package.record_format = []

    for resource in resources:
        if isinstance(resource, str):
            format = resource
        else:
            format = resource["format"]

        # Is the format one of our conversion types?
        if format in type_conversion.keys():
            format = type_conversion[format]

        # Add the format to the package's record format list if it's not already there and is a valid data type
        if format not in package.record_format and format in data_types:
            package.record_format.append(format)

        if format not in data_types:
            package.record_format.append("Other")

    return package.record_format


def get_source_url(result: dict[str, Any], package: Package) -> Package:
    """Retrieves the source URL from the package's resources.

    :param result: The result to retrieve source URL from.
    :param package: The package to update with the source URL.
    :return: The updated package.
    """
    # If there is only one resource available and it's a link
    if len(result["resources"]) == 1 and package.record_format == ["HTML text"]:
        # Use the link to the external page
        package.url = result["resources"][0]["url"]
    # If there are no resources available
    elif len(result["resources"]) == 0:
        # Use the dataset's external landing page
        package.url = [
            extra["value"]
            for extra in result["extras"]
            if extra["key"] == "landingPage"
        ]
        package.record_format = ["HTML text"]
    else:
        # Use the package's dataset information page
        package.url = f"{result['base_url']}dataset/{result['name']}"
        package.data_portal_type = "CKAN"

    return package


def get_supplying_entity(result: dict[str, Any]) -> str:
    """Retrieves the supplying entity from the package's extras.

    :param result: The result to retrieve supplying entity from.
    :return: The supplying entity.
    """
    if "extras" not in result.keys():
        return result["organization"]["title"]

    for extra in result["extras"]:
        if extra["key"] == "publisher":
            return extra["value"]

    return result["organization"]["title"]


def main():
    results = []

    print("Gathering results...")
    results = perform_search(
        search_func=ckan_package_search,
        search_terms=package_search,
        results=results,
    )
    results = perform_search(
        search_func=ckan_group_package_show,
        search_terms=group_search,
        results=results,
    )
    results = perform_search(
        search_func=ckan_package_search_from_organization,
        search_terms=organization_search,
        results=results,
    )

    flat_list = list(chain(*results))
    # Deduplicate entries
    flat_list = [i for n, i in enumerate(flat_list) if i not in flat_list[n + 1 :]]
    print("\nRetrieving collections...")
    flat_list = get_collection_child_packages(flat_list)

    filtered_results = list(filter(filter_result, flat_list))
    parsed_results = list(map(parse_result, filtered_results))

    # Write to CSV
    df = pd.DataFrame(parsed_results)
    df.to_csv("results.csv")


if __name__ == "__main__":
    main()
