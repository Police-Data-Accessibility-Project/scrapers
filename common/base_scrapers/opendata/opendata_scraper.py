import requests
import os
import sys
from datetime import date
from pathlib import Path
import json

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p))

from common.utils import page_update


def opendata_scraper(url_table, save_table, save_folder):
    for i, row in enumerate(url_table):
        # get the api response
        response = requests.get(url_table[i])
        content_type = response.headers["content-type"]
        if response.status_code == 200:
            # this could be achieved by using the "Return Count Only" option when generating the query instead of hashing the entire response (later on)
            updated = page_update(response, save_folder + save_table[i], loop=True, print_output=False)
            # print("Update bool: " + str(updated))

            if updated:
                print(f"  [*] Url in index {i} of url_table has updated.")
                if "json" in content_type:
                    parsed = json.loads(response.text)

                date_name = date.today()
                file_name = (
                    str(date_name).replace("-", "_") + "_" + save_table[i].strip("/")
                )
                if "json" in content_type:
                    with open(
                        save_folder + save_table[i] + file_name + ".json", "w"
                    ) as output:
                        output.write(json.dumps(parsed, indent=4, sort_keys=False))
                        
                elif "csv" in content_type:
                    with open(save_folder + save_table[i] + file_name +".csv", "w") as output:
                        output.write(response.text)
            else:
                print(f"  [*] Url in index {i} of url_table has not updated.")
        else:
            print(
                f" [!!!] Url {url_table[i]} returned code {response.status_code}. Check that the url is correct."
            )
