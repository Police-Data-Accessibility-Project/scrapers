import requests
import os
import sys
from datetime import date
from pathlib import Path
import json
import urllib

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p))

from utils.website_hasher.page_update import page_update


def opendata_scraper(
    url_table, save_table, save_folder, save_subfolder=False, dictionary=True
):
    print("[!!!] This scraper is deprecated, use ")
    for i, row in enumerate(url_table):
        # get the api response
        print(f"   [*] Getting data for table {url_table[i]}...")
        response = requests.get(url_table[i])
        content_type = response.headers["content-type"]
        if response.status_code == 200:
            # this could be achieved by using the "Return Count Only" option when generating the query instead of hashing the entire response (later on)
            updated = page_update(
                response, save_folder + save_table[i], loop=True, print_output=False
            )
            # print("Update bool: " + str(updated))

            if updated:
                print(f"  [*] Url in index {i} of url_table has updated.")
                print(f"     [*] save_folder: {save_table[i]}")
                if "json" in content_type:
                    parsed = json.loads(response.text)

                date_name = date.today()
                if not save_subfolder:
                    file_name = (
                        str(date_name).replace("-", "_")
                        + "_"
                        + save_table[i].strip("/")
                    )
                else:
                    if save_table[i].count("/") > 1:
                        file_folder = save_table[i].split("/")
                        file_name = (
                            str(date_name).replace("-", "_")
                            + "_"
                            + file_folder[1].strip("/")
                        )

                    else:
                        file_name = (
                            str(date_name).replace("-", "_")
                            + "_"
                            + save_table[i].strip("/")
                        )

                if "json" in content_type:
                    # if save_subfolder:
                    #     if not os.path.exists(save_folder + save_table[i]):
                    #         os.makedirs(save_folder + save_table[i])
                    with open(
                        save_folder + save_table[i] + file_name + ".json", "w"
                    ) as output:
                        output.write(json.dumps(parsed, indent=4, sort_keys=False))

                elif "csv" in content_type:
                    with open(
                        save_folder + save_table[i] + file_name + ".csv", "w"
                    ) as output:
                        output.write(response.text)

                elif "octet-stream" in content_type:
                    print(
                        '  [*] content_type is "octect-stream", saving as csv. (Experimental)'
                    )
                    if ".csv" in url_table[i]:
                        with open(
                            save_folder + save_table[i] + file_name + ".csv", "w"
                        ) as output:
                            output.write(response.text)
                    elif ".xlsx" in url_table[i]:
                        urllib.request.urlretrieve(
                            url_table[i],
                            save_folder + save_table[i] + file_name + ".xlsx",
                        )

                else:
                    print(
                        f"  [!] The url in index {i}, save_folder: {save_table[i]}, did not have a handled content_type!"
                    )
                    print("      [?] content_type: " + content_type)
            else:
                print(f"  [*] Url in index {i} of url_table has not updated.")
                print(f"     [*] save_folder: {save_table[i]}")
        else:
            print(
                f" [!!!] Url {url_table[i]} returned code {response.status_code}. Check that the url is correct."
            )
