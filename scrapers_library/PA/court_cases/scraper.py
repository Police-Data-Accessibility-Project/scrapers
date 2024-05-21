import requests
import json
import os

url=os.getenv("PA_COURTS_ENDPOINT")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'} # prevents request from being denied by api

# "MJ-05213-LT-0000011-2021"

def pull_case_json(case_id):
    resp = requests.get(url + case_id, headers=headers)
    filename = "./data/" + case_id + ".json"

    with open(filename, 'w') as f:
        json.dump(resp.json(), f) # save json to local file

#un-comment one or more lines below, replacing with the appropriate case numbers, to scrape the cases.

#pull_case_json("MJ-09302-TR-0000928-2020")
#pull_case_json("MJ-06306-TR-0000813-2020")
#pull_case_json("MJ-51301-TR-0000779-2020")
