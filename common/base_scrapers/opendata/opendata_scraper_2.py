import requests
import os
import sys
from datetime import date
from pathlib import Path
import json
import urllib

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p))

from common.utils import page_update


# url_save = [
#     [save_folder, url],
#     [save_folder, url],
#     [save_folder, url],
#     [save_folder, url],
#     [save_folder, url],
# ]


def opendata_scraper2(url_save, save_folder, save_subfolder=False):
    for i, row in enumerate(url_save):
        # get the api response
        print(f"   [*] Getting data for table {url_save[i][0]}...")

        url = url_save[i][1]
        response = requests.get(url)
        content_type = response.headers["content-type"]

        if response.status_code == 200:
            save_location = url_save[i][0]
            # this could be achieved by using the "Return Count Only" option when generating the query instead of hashing the entire response (later on)
            updated = page_update(
                response, save_folder + save_location, loop=True, print_output=False
            )
            # print("Update bool: " + str(updated))

            if updated:
                print(f"    [*] Url in index {i} of url_save has updated.")
                print(f"     [*] save_folder: {save_location}\n")
                if "json" in content_type:
                    parsed = json.loads(response.text)

                date_name = date.today()
                if not save_subfolder:
                    file_name = (
                        str(date_name).replace("-", "_")
                        + "_"
                        + save_location.strip("/")
                    )
                else:
                    if save_location.count("/") > 1:
                        file_folder = save_location.split("/")
                        file_name = (
                            str(date_name).replace("-", "_")
                            + "_"
                            + file_folder[1].strip("/")
                        )

                    else:
                        file_name = (
                            str(date_name).replace("-", "_")
                            + "_"
                            + save_location.strip("/")
                        )

                if "json" in content_type:
                    # if save_subfolder:
                    #     if not os.path.exists(save_folder + save_location):
                    #         os.makedirs(save_folder + save_location)
                    with open(
                        save_folder + save_location + file_name + ".json", "w"
                    ) as output:
                        output.write(json.dumps(parsed, indent=4, sort_keys=False))

                elif "csv" in content_type:
                    with open(
                        save_folder + save_location + file_name + ".csv", "w"
                    ) as output:
                        output.write(response.text)

                elif "octet-stream" in content_type:
                    print(
                        '  [*] content_type is "octect-stream", saving as csv. (Experimental)'
                    )
                    if ".csv" in url_save[i]:
                        with open(
                            save_folder + save_location + file_name + ".csv", "w"
                        ) as output:
                            output.write(response.text)
                    elif ".xlsx" in url_save[i]:
                        urllib.request.urlretrieve(
                            url_save[i],
                            save_folder + save_location + file_name + ".xlsx",
                        )

                else:
                    print(
                        f"   [!] The url in index {i}, save_folder: {save_location}, did not have a handled content_type!"
                    )
                    print("      [?] content_type: " + content_type)
            else:
                print(f"    [*] Url in index {i} of url_save has not updated.")
                print(f"     [*] save_folder: {save_location}\n")
        else:
            print(
                f" [!!!] Url {url_save[i]} returned code {response.status_code}. Check that the url is correct."
            )

    # import etl
