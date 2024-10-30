import requests
import json
import time

# Function to fetch jurisdiction IDs based on town names from a text file
def fetch_jurisdiction_ids(town_file, base_url):
    with open(town_file, "r") as file:
        town_names = [line.strip() for line in file]

    jurisdiction_ids = {}
    url = base_url

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for item in data.get('results', []):
                if item['name'] in town_names:
                    jurisdiction_ids[item['name']] = item['id']

            url = data.get("next")
            print(f"Processed page, found {len(jurisdiction_ids)}/{len(town_names)} jurisdictions so far...")
            time.sleep(1)  # To respect the rate limit

        elif response.status_code == 503:
            print("Error 503: Skipping page")
            break
        else:
            print(f"Error fetching data: {response.status_code}")
            break

    return jurisdiction_ids

# Function to fetch FOIA data for each jurisdiction ID and save it to a JSON file
def fetch_foia_data(jurisdiction_ids):
    all_data = []
    for name, id_ in jurisdiction_ids.items():
        url = f"https://www.muckrock.com/api_v1/foia/?status=done&jurisdiction={id_}"
        while url:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                all_data.extend(data.get("results", []))
                url = data.get("next")
                print(f"Fetching records for {name}, {len(all_data)} total records so far...")
                time.sleep(1)  # To respect the rate limit
            elif response.status_code == 503:
                print(f"Error 503: Skipping page for {name}")
                break
            else:
                print(f"Error fetching data: {response.status_code} for {name}")
                break

    # Save the combined data to a JSON file
    with open("foia_data_combined.json", "w") as json_file:
        json.dump(all_data, json_file, indent=4)

    print(f"Saved {len(all_data)} records to foia_data_combined.json")

# Main function to execute the script
def main():
    town_file = "allegheny-county-towns.txt"
    jurisdiction_url = "https://www.muckrock.com/api_v1/jurisdiction/?level=l&parent=126"

    # Fetch jurisdiction IDs based on town names
    jurisdiction_ids = fetch_jurisdiction_ids(town_file, jurisdiction_url)
    print(f"Jurisdiction IDs fetched: {jurisdiction_ids}")

    # Fetch FOIA data for each jurisdiction ID
    fetch_foia_data(jurisdiction_ids)

# Run the main function
if __name__ == "__main__":
    main()
