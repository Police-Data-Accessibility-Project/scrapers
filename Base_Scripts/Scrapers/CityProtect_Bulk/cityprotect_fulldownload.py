"""
Download full Incident Report data from CityProtect.com where bulkDownload is authorized
https://github.com/EricTurner3
7 Apr 2021

Description:
  - Will drop full data drops in ./data/<state>/<agency-id>
  - Also grabs some canadian data, because CityProtect does not have a country code to filter and they use the province as a state code

Known Issues & Limitations:
  - Even if a file is available, sometimes the file is completely empty (0 bytes), seems to be a glitch on the server or with the agency that uploaded the data
    - I think the data is corrupted with incorrect codes. One time I got an invalid ASCII error during write so CityProtect may just abort the download.
  - No way to grab an accurate city or county from the agency, so data drops in an agency-id subfolder so it's recognizable
"""

import requests
import json
import os
from time import sleep

url = "https://ce-portal-service.commandcentral.com/api/v1.0/public/agencies"
print("Fetching agencies from {}".format(url))

payload = '{"limit":15000,"offset":0,"geoJson":{"type":"MultiPolygon","coordinates":[[[[-180,90],[0,90],[0,-90],[-180,-90],[-180,90]]],[[[0,90],[180,90],[180,-90],[0,-90],[0,90]]]]},"projection":false,"propertyMap":{}}'
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, data=payload)

json_resp = json.loads(response.text)

# 1092 agencies
print("Total Fetched: " + str(len(json_resp["result"]["list"])))


print("Downloading data from agencies with bulk data authorized.")


def verify_data(data_code, save_dir):
    if (
        data_code.status_code != 404 or str(data_code).find("<Error>") == False
    ):  # Verifies that file exists
        with open(save_dir, "wb") as data_file:
            try:
                data_file.write(
                    data_code.text.encode("utf-8")
                )  # Writes using requests text function thing
                data_file.close()
            except:
                print("Error in encoding")
                data_file.close()


def get_agency_data(agency):
    # check the reports section of the agency, it has every single report available for download if bulkDownload is 'y'

    cur_dir = os.getcwd()
    state = agency["state"]
    customerId = agency["customerId"]
    # build the save directory as ./data/<state>/<customerId>
    # City Protect has bad data for city so we cannot use it
    save_dir = os.path.join(cur_dir, "data", state, customerId)

    # make path if needed
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    base_url = "https://cereplicatorprodcomm.blob.core.windows.net/mainblob/"

    for report in agency["reports"]:
        # this is the JSON of what a report looks like
        """
        {
            "_id": "5e4528c9c2dd47001118ba81",
            "generationDate": "2020-02-13T10:44:00.509Z",
            "filename": "78431-01.2017-04.2017.csv",
            "targetPeriodStart": "2017-01-01T00:00:00.000Z",
            "targetPeriodEnd": "2017-04-01T00:00:00.000Z",
            "available": true
        }
    """
        # NOTE: each report has a generationDate, we can check this against the last time the script was ran and then only pull newly generated files instead of doing a full data dump each time
        # not implemented currently but good info to have

        if report["available"] == True:
            print("Getting {} - {}, {}".format(state, customerId, report["filename"]))
            # handle a connection reset error
            try:
                data = requests.get(base_url + report["filename"], allow_redirects=True)
                save_path = os.path.join(
                    save_dir, report["filename"]
                )  # file name to write to
                verify_data(data, save_path)
            except:
                print("  Error in Connection, skipping download")
        sleep(
            5
        )  # prevent a DoS attack by sleeping for 5 seconds between requests, no robots.txt found for crawler speed


# check if bulkDownload is allowed in the full list of agencies queried
# if so, lets grab the data!
for agency in json_resp["result"]["list"]:
    if agency["bulkDownload"]:
        get_agency_data(agency)  # download the data if bulk download is allowed
