import requests
import os
import sys
from datetime import date
from pathlib import Path
import json
import urllib
import time

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p))

from common.utils import page_update


# save_url = [
#     [save_folder, url],
#     [save_folder, url],
#     [save_folder, url],
#     [save_folder, url],
#     [save_folder, url],
# ]

# save_folder is the parent directory that all data will be saved under
def opendata_scraper2(save_url, save_folder, sleep_time=1, save_subfolder=False, socrata=False):
    """
    Scrape opendata (and similar) websites
    :param save_url: provide nested list following provided example
    :param save_folder: parent directory where data should be saved
    :param sleep_time: set to robots.txt crawl-delay if available (default 1)
    :param save_subfolder: whether or not to you are trying to save in a subfolder per url (default false)
    :param socrata: if you are scraping a socrata website, set to true (default false)
    """
    for i, row in enumerate(save_url):
        # get the api response
        print(f"   [*] Getting data for table {save_url[i][0]}...")

        url = save_url[i][1]
        if not socrata:
            response = requests.get(url)
            content_type = response.headers["content-type"]
        else:
            # Gets the view-uuid out of the url
            view_uuid = url.rsplit("/", 1)[-1]
            # remove file extension
            view_uuid = view_uuid.split(".")[0]

            # Parse the url using urllib
            parsed_url = urllib.parse.urlparse(url)
            site_hostname = parsed_url.hostname
            api_url = f"https://{site_hostname}/api/views/metadata/v1/{view_uuid}"
            response = requests.get(api_url)

        if response.status_code == 200:
            save_location = save_url[i][0]
            # this could be achieved by using the "Return Count Only" option when generating the query instead of hashing the entire response (later on)
            if not socrata:
                updated = page_update(response, save_folder + save_location, loop=True, print_output=False)
            else:
                # get the update date of the data from the returned dictionary
                response_json = json.loads(response.text)
                data_updated_date = response_json["dataUpdatedAt"]

                if not os.path.exists(save_folder + save_location):
                    os.makedirs(save_folder + save_location)

                # An altered version of page_update.py
                # Check if the file data.txt exists, and that it is not empty
                if os.path.isfile(save_folder + save_location + "date.txt") and os.stat(save_folder + save_location + "date.txt").st_size != 0:
                    with open(save_folder + save_location + "date.txt", "r") as output:
                        # Read the file
                        previous_update_date = output.read()

                        # compare the file to the date gotten from the api
                        if data_updated_date in previous_update_date:
                            print(" [*] File has not updated")
                            updated = False

                        else:
                            with open(save_folder + save_location + "date.txt", "w") as output_writable:
                                print(" [*] File has updated")
                                updated = True
                                output_writable.write(data_updated_date)

                # If the script has never been run, it will generate the hash and store it for the next run.
                else:
                    print("   [*] No date.txt file found. First time?")
                    with open(save_folder + save_location + "date.txt", "w+") as output:
                        updated = True
                        output.write(data_updated_date)

            # print("Update bool: " + str(updated))

            if updated:
                if socrata:
                    # As response is set to the api url we need to set it here.
                    response = requests.get(url)
                    content_type = response.headers["content-type"]

                print(f"    [*] Url in index {i} of save_url has updated.")
                print(f"     [*] save_folder: {save_location}\n")
                if "json" in content_type:
                    parsed = json.loads(response.text)

                date_name = date.today()

                if save_subfolder:
                    print(" [!] save_subfolder is deprecated")

                if save_location.count("/") > 1:
                    file_folder = save_location.split("/")
                    file_name = str(date_name).replace("-", "_") + "_" + file_folder[1].strip("/")

                else:
                    file_name = str(date_name).replace("-", "_") + "_" + save_location.strip("/")

                if "json" in content_type:
                    # if save_subfolder:
                    #     if not os.path.exists(save_folder + save_location):
                    #         os.makedirs(save_folder + save_location)
                    with open(save_folder + save_location + file_name + ".json", "w") as output:
                        output.write(json.dumps(parsed, indent=4, sort_keys=False))

                elif "csv" in content_type:
                    with open(save_folder + save_location + file_name + ".csv", "w") as output:
                        output.write(response.text)

                elif "octet-stream" in content_type:
                    print('  [*] content_type is "octect-stream", saving as csv. (Experimental)')
                    if ".csv" in save_url[i]:
                        with open(save_folder + save_location + file_name + ".csv", "w") as output:
                            output.write(response.text)
                    elif ".xlsx" in save_url[i]:
                        urllib.request.urlretrieve(
                            save_url[i], save_folder + save_location + file_name + ".xlsx",
                        )

                else:
                    print(f"   [!] The url in index {i}, save_folder: {save_location}, did not have a handled content_type!")
                    print("      [?] content_type: " + content_type)
            else:
                print(f"    [*] Url in index {i} of save_url has not updated.")
                print(f"     [*] save_folder: {save_location}\n")

            time.sleep(int(sleep_time))
        else:
            print(f" [!!!] Url {save_url[i]} returned code {response.status_code}. Check that the url is correct.")

    # import etl
