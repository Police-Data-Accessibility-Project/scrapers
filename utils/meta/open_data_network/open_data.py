import csv
import json
from os.path import exists

import requests

# Categories, names, and tags used to filter out irrelevant data
FILTERED_CATEGORIES = [
    "building and facilities", "information", "administration & finance", "general government", "retirement systems",
    "economy", "transportation", "growing economic opportunities", "environment", "licensing", "covid",
    "culture and recreation", "public works", "tax", "city management and ethics", "thriving neighborhoods",
    "infrastructure", "planning", "human services", "city government", "health and social services", "automobiles",
    "neighborhood census data", "business", "housing", "service requests", "ptsd-repository", "fire and medical",
    "services and amenities", "buildings", "water", "surveys", "base maps"
]
FILTERED_NAMES = [
    "permit", "inspection", "blood", "covid", "certificate", "fire and spec ops", "code violation", "weeds",
    "calendar"
]
FILTERED_TAGS = [
    "ems", "survey", "vaccination", "fire", "fire investigations", "employee", "311", "council", "animal", "animals",
    "alarm", "tax", "alert", "dog", "chemical exposure", "directory"
]


def get_data(search_term):
    """Gets Open Data Network data using the Socrata api.

    Args:
        search_term (str): Search term to query.

    Returns:
        list: List of results from the query.
    """    
    api_url = f"http://api.us.socrata.com/api/catalog/v1?categories=Public%20Safety&q={search_term}&limit=10000"
    response = requests.get(api_url)

    if response.status_code != 200:
        print("Response returned status code {response.status_code}")
        quit()

    response_json = response.json()

    return response_json["results"]


def filter_data(dataset):
    """Filters out irrelevant data.

    Args:
        dataset (dict): Information about a dataset.

    Returns:
        bool: True if data is relevant, False otherwise.
    """    
    domain_category = ""
    resource_name = dataset["resource"]["name"].lower()
    domain_tags = [tag.lower() for tag in dataset["classification"]["domain_tags"]]

    try:
        domain_category = dataset["classification"]["domain_category"].lower()
        # Check if the category needs to be filtered out
        if any(tag in domain_category for tag in FILTERED_CATEGORIES):
            # Transportation is a mostly irrelevant category, unless the name contains "crashes"
            if domain_category == "transporation" and "crashes" in resource_name:
                return True
            else:
                return False
    except KeyError:
        pass
    
    # Check if the name or tag needs to be filtered out
    if any(name in resource_name for name in FILTERED_NAMES) or any(tag in domain_tags for tag in FILTERED_TAGS):
        return False

    return True


def remove_duplicates(data):
    """Removes data sources that are already in the PDAP database.

    Args:
        data (list): List of dataset dictionaries.

    Returns:
        list: List of datasets with duplicates removed.
    """    
    with open("PDAP Data Sources.csv", encoding="utf-8-sig") as data_sources:
        sources_list = list(csv.DictReader(data_sources))

    source_urls = [source["source_url"] for source in sources_list]
    data = filter(lambda dataset: dataset["link"] not in source_urls, data)

    return list(data)


def write_csv(data):
    """Write the data to CSV file.

    Args:
        data (list): List of dataset dictionaries.
    """    
    fieldnames = [
        "name", "agency_described", "description", "source_url", "data_portal_type"
    ]

    with open("Open Data Network.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for dataset in data:
            dataset["resource"]["name"] = parse_string(dataset["resource"]["name"])
            if dataset["resource"]["attribution"]:
                dataset["resource"]["attribution"] = parse_string(dataset["resource"]["attribution"])
            dataset["resource"]["description"] = parse_string(dataset["resource"]["description"])

            name = dataset["resource"]["name"]
            agency_described = dataset["resource"]["attribution"]
            description = dataset["resource"]["description"]
            source_url = dataset["link"]

            writer.writerow(
                {
                    "name": name,
                    "agency_described": agency_described,
                    "description": description,
                    "source_url": source_url,
                    "data_portal_type": "Socrata"
                }
            )


def parse_string(string):
    """Parses a string for CSV compatibility.

    Args:
        string (str): String to parse.

    Returns:
        str: Resulting string.
    """    
    string = string.replace('"', '""')
    result = '"' + string + '"'

    return result


def main():
    print("Retrieving data from http://api.us.socrata.com/...")

    return_data = get_data("jail") + get_data("court") + get_data("police") + get_data("crime")

    data = []
    # Remove duplicates from overlapping data
    [data.append(dataset) for dataset in return_data if dataset not in data]

    print(f"{len(data)} records returned by API")

    data = list(filter(filter_data, data))
    if exists("PDAP Data Sources.csv"):
        data = remove_duplicates(data)

    print(f"{len(data)} records remaining after filtering")

    write_csv(data)

    print("Results written to Open Data Network.csv")

if __name__ == "__main__":
    main()
