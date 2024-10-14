import requests
import csv
import time
import json

# Define the base API endpoint
base_url = "https://www.muckrock.com/api_v1/foia/"

# Set initial parameters
page = 1
per_page = 100
all_data = []
output_file = "foia_data.json"

# Function to fetch data from a specific page
def fetch_page(page):
    response = requests.get(base_url, params={"page": page, "page_size": per_page, "format": "json"})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching page {page}: {response.status_code}")
        return None

# Fetch and store data from all pages
while True:
    print(f"Fetching page {page}...")
    data = fetch_page(page)
    if data is None:
        print(f"Skipping page {page}...")
        page += 1
        continue

    all_data.extend(data['results'])
    if not data['next']:
        break

    page += 1

# Write data to CSV
with open(output_file, mode='w', encoding='utf-8') as json_file:
    json.dump(all_data, json_file, indent=4)

print(f"Data written to {output_file}")
