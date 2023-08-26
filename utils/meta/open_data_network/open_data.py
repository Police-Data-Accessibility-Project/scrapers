import json

import requests

FILTERED_CATEGORIES = [
    "building and facilities", "information", "administration & finance", "general government", "retirement systems",
    "economy", "transportation", "growing economic opportunities", "environment", "licensing", "covid",
    "culture and recreation", "public works", "tax", "city management and ethics", "thriving neighborhoods",
    "infrastructure", "planning", "human services", "city government", "health and social services", "automobiles",
    "neighborhood census data", "business", "housing", "service requests", "ptsd-repository", "fire and medical",
    "geographic locations and boundaries"
    ]
FILTERED_NAMES = [
    "permit", "inspection", "blood", "covid", "certificate", "fire and spec ops"
    ]
FILTERED_TAGS = [
    "ems", "survey", "vaccination", "fire", "fire investigations", "employee", "311", "council", "animal", "animals",
    "alarm", "tax", "alert", "dog"
    ]


def get_data(search_term):
    api_url = f"http://api.us.socrata.com/api/catalog/v1?categories=Public%20Safety&q={search_term}&limit=10000"
    response = requests.get(api_url)

    if response.status_code != 200:
        print("Response returned status code {response.status_code}")
        quit()

    response_json = json.loads(response.text)

    return response_json["results"]


def filter_data(dataset):
    domain_category = ""
    resource_name = dataset["resource"]["name"].lower()
    domain_tags = [tag.lower() for tag in dataset["classification"]["domain_tags"]]

    try:
        domain_category = dataset["classification"]["domain_category"].lower()
        if any(tag in domain_category for tag in FILTERED_CATEGORIES):
            if domain_category == "transporation" and "crashes" in resource_name:
                return True
            else:
                return False
    except KeyError:
        pass
    
    if any(name in resource_name for name in FILTERED_NAMES) or any(tag in domain_tags for tag in FILTERED_TAGS):
        return False

    #if domain_category == "":
    #if "fire and spec ops" in resource_name:
    #if "agriculture" in domain_tags:
        #print(f'{dataset["resource"]["id"]} - {resource_name} - {domain_category}')

    #if domain_category not in domain_categories:
    #    domain_categories.append(domain_category)

    return True


def main():
    print("Retrieving data from http://api.us.socrata.com/...")

    data = get_data("police") + get_data("crime")
    data = { each["resource"]["id"] : each for each in data }.values()

    print(f"{len(data)} records returned by API")

    data = list(filter(filter_data, data))

    print(f"{len(data)} records remaining after filtering")


if __name__ == "__main__":
    main()