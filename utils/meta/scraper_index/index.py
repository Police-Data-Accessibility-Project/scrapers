import csv
import re
import requests
import os
from pathlib import Path
from collections import OrderedDict


def get_data():
    """Retrieve data from the PDAP API data sources endpoint.

    Returns:
        list: List of dictionaries of data sources sorted by state code.
    """
    API_KEY = os.getenv("PDAP_API_KEY")
    r = requests.get("http://data-sources.pdap.io/data-sources", headers={"Authorization": f"Bearer {API_KEY}"})
    data = r.json()["data"]
    clean_data = []
    for d in data:
        d["state"] = d["state"] if d["state"] is not None else ""
        clean_data.append(d)
    # Sort by state code
    clean_data.sort(key=lambda data_source: data_source["state"])
    return clean_data


def in_repo_filter(data_source):
    """Filters data sources between whether or not they're in the PDAP repository.

    Args:
        data_source (dict): Data source to be sorted.
    """

    """Checks for duplicate names"""
    is_in_list = lambda list: data_source["name"] in [data_source["name"] for data_source in list]

    if "scraper_url" in data_source and data_source["scraper_url"] and "Police-Data-Accessibility-Project" in data_source["scraper_url"] and not is_in_list(in_repo):
        in_repo.append(data_source)
    elif data_source["scraper_url"] and not is_in_list(not_in_repo):
        not_in_repo.append(data_source)


def write_md():
    """Create and write to the markdown file"""
    filepath = Path(__file__).resolve().parents[3]

    md = open(f"{filepath}/INDEX.md", "w")
    md.write("# Scraper Index\n\n")
    md.write("[Scrapers in this repo](#scrapers-in-this-repo)\n\n")
    md.write("[Scrapers not in this repo](#scrapers-not-in-this-repo)\n")

    # In this repo section
    write_section(md, in_repo, header="Scrapers in this repo")

    # Not in this repo section
    write_section(md, not_in_repo, header="Scrapers not in this repo")

    md.close()


def write_section(md, section_data, header):
    """Write data for a particular section.

    Args:
        md (TextIOWrapper): Markdown file to write to.
        section_data (list): List of dictionaries of data sources.
        header (String): Header, either In this repo or Not in this repo
    """
    national_data = []

    md.write(f"\n## {header}\n\n")
    md.write("Name | Agency Described | Record Type | State | County | Municipality | Scraper URL\n")
    md.write("--- | --- | --- | --- | --- | --- | ---\n")

    for data_source in section_data:
        # Sort out national and multistate data sources
        if not data_source["state"] or "," in data_source["state"]:
            national_data.append(data_source)
            continue

        write_scraper(md, data_source)

    if national_data:
        md.write("\n### National and Multistate\n\n")
        md.write("Name | Agency Described | Record Type | State | County | Municipality | Scraper URL\n")
        md.write("--- | --- | --- | --- | --- | --- | ---\n")

        """Removes duplicate entries from a string"""
        remove_duplicates = lambda s: ", ".join(OrderedDict.fromkeys(s.split(",")))

        for data_source in national_data:
            is_multistate = "," in data_source["state"]
            if is_multistate:
                data_source["agency_described"] = remove_duplicates(data_source["agency_described"]) if "agency_described" in data_source else ""
                data_source["state"] = remove_duplicates(data_source["state"])
                data_source["county"] = remove_duplicates(data_source["county"])
                data_source["municipality"] = remove_duplicates(data_source["municipality"])
            elif not data_source["state"]:
                data_source["state"] = "USA"

            write_scraper(md, data_source)


def write_scraper(md, data_source):
    """Write scraper information in table.

    Args:
        md (TextIOWrapper): Markdown file to write to.
        data_source (dict): Data source.
    """

    """Removes redundant trailing state code"""
    remove_state_code = lambda s: re.sub(r" - [A-Z]{2}$", "", s)

    name = remove_state_code(data_source["name"])
    agency = data_source["agency_described"] if "agency_described" in data_source else ""
    if "," not in agency:
        agency = remove_state_code(agency)
    type = data_source["record_type"]
    state = data_source["state"]
    county = data_source["county"]
    municipality = data_source["municipality"]
    url = data_source["scraper_url"]

    md.write(f"{name} | {agency} | {type} | {state} | {county} | {municipality} | [{url}]({url})\n")


def main():
    data_sources = get_data()

    for data_source in data_sources:
        in_repo_filter(data_source)

    write_md()


if __name__ == "__main__":
    in_repo = []
    not_in_repo = []

    main()
