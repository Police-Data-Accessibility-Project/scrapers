"""
Police code is based on the request that is sent when you press download on cityprotect.com
set start_year and start_month to the earliest year and month of data that is available

Forked from https://github.com/Police-Data-Accessibility-Project/Scrapers/tree/master/Base_Scripts/Scrapers/Cityprotect_base_scraper.py
"""

import requests
from datetime import date
import os
import time

# TODO - create a list of the different police codes in CityProtect and loop through gathering all the data for each jurisdiction
# and drop it into its respective folder in /data

police_code = "109542"  # IMPD
start_month = 1
start_year = 2019  # First Migrated to CityProtect Jan 2019
delay = 1

base_url = "https://cereplicatorprodcomm.blob.core.windows.net/mainblob/"

# Get the current month and year, not needed for IMPD as their is a delay in data upload
# Switch which is commented out based on if data is current
"""
today = date.today()
max_month = today.strftime("%m")
max_year = today.strftime("%Y")
"""
# data is released in 3 month batches
# Jan 2021 - Mar 2021 is one batch, use the data for Jan 2021 here
max_year = 2021
max_month = 1

cur_dir = os.getcwd()
save_dir = cur_dir + "/data/impd/"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)


def verify_data(data_code):
    if (
        data_code.status_code != 404 or str(data_code).find("<Error>") == False
    ):  # Verifies that file exists
        save_path = os.path.join(save_dir, file_name)
        with open(save_path, "w") as data_file:
            data_file.write(data.text)  # Writes using requests text function thing
            data_file.close()


end = False
# Iterate over every month until the start_month and year are equal
# 758-10.2019-01.2020.csv
# police_code-start_month.start_year-end_month.end_year
# while max_month != start_month and max_year != start_year:
while start_year <= int(max_year):
    end_month = int(start_month) + 3

    # Convert the int value of the month to mm format
    if len(str(start_month)) == 1:
        start_month = str(start_month).zfill(2)
    if len(str(end_month)) == 1:
        end_month = str(end_month).zfill(2)

    # Compensate for october with end_year change
    if start_month == 10:
        end_year = start_year + 1
        end_month = str(1).zfill(2)
        file_name = (
            str(police_code)
            + "-"
            + str(start_month)
            + "."
            + str(start_year)
            + "-"
            + str(end_month)
            + "."
            + str(end_year)
            + ".csv"
        )
        url = base_url + file_name
        print("Getting " + file_name)
        data = requests.get(url, allow_redirects=True)
        verify_data(data)
        start_month = "01"
        start_year = int(start_year) + 1
    else:
        file_name = (
            str(police_code)
            + "-"
            + str(start_month)
            + "."
            + str(start_year)
            + "-"
            + str(end_month)
            + "."
            + str(start_year)
            + ".csv"
        )
        url = base_url + file_name
        print("Getting " + file_name)
        data = requests.get(url, allow_redirects=True)

        verify_data(data)
        if start_month != 10:
            start_month = int(end_month)
        else:
            start_month = 1
            start_year = int(start_year) + 1

        time.sleep(delay)
    """
	input()
	print(end_month)
	if start_year > int(max_year):
		break
	"""
