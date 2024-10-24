import requests
import json

# Define the base API endpoint
base_url = "https://www.muckrock.com/api_v1/foia/"

# Define the search string
search_string = "use of force"
per_page = 100
page = 1
all_results = []
max_count = 20

while True:

    # Make the GET request with the search string as a query parameter
    response = requests.get(base_url, params={"page" : page, "page_size" : per_page, "format": "json"})

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        if not data['results']:
            break

        filtered_results = [item for item in data['results'] if search_string.lower() in item['title'].lower()]

        all_results.extend(filtered_results)

        if len(filtered_results) > 0:
            num_results = len(filtered_results)
            print(f"found {num_results} more matching result(s)...")

        if len(all_results) >= max_count:
            print("max count reached... exiting")
            break

        page += 1

    else:
        print(f"Error: {response.status_code}")
        break

# Dump list into a JSON file
json_out_file = search_string.replace(" ", "_") + ".json"
with open(json_out_file, 'w') as json_file:
    json.dump(all_results, json_file)

print(f"List dumped into {json_out_file}")
