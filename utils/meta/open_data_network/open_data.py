import requests
import json


FILTERED_TAGS = ["police", "safe community"]


def get_data():
    api_url = "http://api.us.socrata.com/api/catalog/v1?categories=Public%20Safety&limit=10000"
    response = requests.get(api_url)
    response_json = json.loads(response.text)
    
    return response_json["results"]


def filter_data(dataset):
    try:
        if any(tag in dataset["classification"]["domain_category"].lower() for tag in FILTERED_TAGS):

            print(dataset["resource"]["id"] + " - " + dataset["resource"]["name"])
            return True
    except KeyError:
        pass
    
    domain_tags = [tag.lower() for tag in dataset["classification"]["domain_tags"]]
    #if any(tag in domain_tags for tag in FILTERED_TAGS):
        #rint(dataset["resource"]["name"])
        #return True

    return False


def main():
    data = get_data()

    data = list(filter(filter_data, data))

    print(len(data))


if __name__ == "__main__":
    main()