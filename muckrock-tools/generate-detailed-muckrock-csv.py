import json
import argparse
import csv
import requests
import time

# Load the JSON data
parser = argparse.ArgumentParser(description="Parse JSON from a file.")
parser.add_argument('--json_file', type=str, required=True, help="Path to the JSON file")

args = parser.parse_args()

with open(args.json_file, 'r') as f:
    json_data = json.load(f)

# Define the CSV headers
headers = [
    "name", "agency_described", "record_type", "description", "source_url",
    "readme_url", "scraper_url", "state", "county", "municipality",
    "agency_type", "jurisdiction_type", "View Archive", "agency_aggregation",
    "agency_supplied", "supplying_entity", "agency_originated", "originating_agency",
    "coverage_start", "source_last_updated", "coverage_end", "number_of_records_available",
    "size", "access_type", "data_portal_type", "access_notes", "record_format", "update_frequency",
    "update_method", "retention_schedule", "detail_level"
]

def get_agency(agency_id):
    # API call to get agency_described
    if agency_id:
        agency_url = f"https://www.muckrock.com/api_v1/agency/{agency_id}/"
        response = requests.get(agency_url)
    
        if response.status_code == 200:
            agency_data = response.json()
            return agency_data
        else:
            return ""
    else:
        print("Agency ID not found in item")

def get_jurisdiction(jurisdiction_id):
    if jurisdiction_id:
        jurisdiction_url = f"https://www.muckrock.com/api_v1/jurisdiction/{jurisdiction_id}/"
        response = requests.get(jurisdiction_url)

        if response.status_code == 200:
            jurisdiction_data = response.json()
            return jurisdiction_data
        else:
            return ""
    else:
        print("Jurisdiction ID not found in item")
    

# Open a CSV file for writing
with open('detailed-muckrock-data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)

    # Write the header row
    writer.writeheader()

    # Iterate through the JSON data
    for item in data:
        print(f"Writing data for {item.get('title')}")
        agency_data = get_agency(item.get("agency"))
        time.sleep(1)
        jurisdiction_data = get_jurisdiction(agency_data.get("jurisdiction"))

        jurisdiction_level = jurisdiction_data.get("level")
        #federal jurisduction level
        if jurisdiction_level == "f":
            state = ""
            county = ""
            municipality = ""
            juris_type = "federal"
        #state jurisdiction level
        if jurisdiction_level == "s":
            state = jurisdiction_data.get("name")
            county = ""
            municipality = ""
            juris_type = "state"
        #local jurisdiction level
        if jurisdiction_level == "l":
            parent_juris_data = get_jurisdiction(jurisdiction_data.get("parent"))
            state = parent_juris_data.get("abbrev")
            if "County" in jurisdiction_data.get("name"):
                county = jurisdiction_data.get("name")
                municipality = ""
                juris_type = "county"
            else:
                county = ""
                municipality = jurisdiction_data.get("name")
                juris_type = "local"

        if 'Police' in agency_data.get("types"):
            agency_type = 'law enforcement/police'
        else:
            agency_type = ''

        source_url = ''
        absolute_url = item.get("absolute_url")
        access_type = ''
        for comm in item["communications"]:
            if comm["files"]:
                source_url = absolute_url + '#files'
                access_type = 'Web page,Download,API'
                break

        # Extract the relevant fields from the JSON object
        csv_row = {
            "name": item.get("title", ""),
            "agency_described": agency_data.get("name", "") + ' - ' + state,
            "record_type": "",
            "description": "",
            "source_url": source_url,
            "readme_url": absolute_url,
            "scraper_url": "",
            "state": state,
            "county": county,
            "municipality": municipality,
            "agency_type": agency_type,
            "jurisdiction_type": juris_type,
            "View Archive": "",
            "agency_aggregation": "",
            "agency_supplied": "no",
            "supplying_entity": "MuckRock",
            "agency_originated": "yes",
            "originating_agency": agency_data.get("name", ""),
            "coverage_start": "",
            "source_last_updated": "",
            "coverage_end": "",
            "number_of_records_available": "",
            "size": "",
            "access_type": access_type,
            "data_portal_type": "MuckRock",
            "access_notes": "",
            "record_format": "",
            "update_frequency": "",
            "update_method": "",
            "retention_schedule": "",
            "detail_level": ""
        }
        
        # Write the extracted row to the CSV file
        writer.writerow(csv_row)
