from itertools import chain
import json
import sys
from typing import Any, Optional

from from_root import from_root
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

    return True


def parse_result(result: dict[str, Any] | Package) -> dict[str, Any]:
    package = Package()

    if isinstance(result, Package):
        return parse_result_package(result)

    package.record_format = get_record_format_list(
        package=package, resources=result["resources"]
    )

    if len(result["resources"]) == 1 and package.record_format == ["HTML text"]:
        package.url = result["resources"][0]["url"]
    else:
        package.url = f"{result['base_url']}dataset/{result['name']}"
        package.data_portal_type = "CKAN"

    package.title = result["title"]
    package.description = result["notes"]
    package.agency_name = result["organization"]["title"]
    package.supplying_entity = get_supplying_entity(result)
    package.source_last_updated = result["metadata_modified"][0:10]

    return package.to_dict()


def parse_result_package(package: Package) -> dict[str, Any]:
    package.record_format = get_record_format_list(package)
    return package.to_dict()


def get_record_format_list(
    package: Package,
    resources: Optional[list[dict[str, Any]]] = None,
) -> list[str]:
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

        if format in type_conversion.keys():
            format = type_conversion[format]

        if format not in package.record_format and format in data_types:
            package.record_format.append(format)

        if format not in data_types:
            package.record_format.append("Other")

    return package.record_format


def get_supplying_entity(result: dict[str, Any]) -> str:
    if "extras" not in result.keys():
        return result["organization"]["title"]
    
    for extra in result["extras"]:
        if extra["key"] == "publisher":
            return extra["value"]
        
    return result["organization"]["title"]


def main():
    results = []

    print("Gathering results...")
    for search in tqdm(package_search):
        results += [
            ckan_package_search(base_url=search["url"], query=query)
            for query in search["terms"]
        ]

    for search in tqdm(group_search):
        results += [
            ckan_group_package_show(base_url=search["url"], id=id)
            for id in search["ids"]
        ]

    for search in tqdm(organization_search):
        results += [
            ckan_package_search_from_organization(
                base_url=search["url"], organization_id=id
            )
            for id in search["ids"]
        ]

    flat_list = list(chain(*results))
    # Deduplicate entries
    flat_list = [i for n, i in enumerate(flat_list) if i not in flat_list[n + 1 :]]
    print("\nRetrieving collections...")
    flat_list = get_collection_child_packages(flat_list)

    filtered_results = list(filter(filter_result, flat_list))
    parsed_results = list(map(parse_result, filtered_results))


if __name__ == "__main__":
    main()
