"""
    CityProtect  - ETL
    8 Apr 2021
    https://github.com/EricTurner3

    Several hundred agencies use CityProtect and allow bulk downloaded files. Fortunately, all these files follow a similar format
    This script will intake the file(s) in ./data and process them to be ready for ingestion
"""

from doltpy.cli import Dolt
from doltpy.cli.write import write_file
from doltpy.cli.read import read_pandas, read_pandas_sql
import shutil
import os
import json
from pathlib import Path
import sys

# this will grab the libraries we need from /common/etl
# prevents having to keep cloning the libraries everywhere (copied from CaptainStabs' usage on scrapers)
p = Path().resolve().parents[2]
pdap_library = os.path.join(p, "common")  # fix for windows
print(pdap_library)
sys.path.insert(
    1, pdap_library
)  # insert into our path for so we can call directly on the modules
from etl import cityprotect
from etl import pdap_dolt

# we can specify a different starting branch here, if needed
branch = "data_types-sandbox"

# 1 - Drop CSVs in the ./data folder. DO NOT rename them, the naming convention from CityProtect is important!
# For now, we have two sample csvs in the folder to work with. For prod purposes, after cloning the repo remove those sample files

# 2 - Grab agency information
agencies = cityprotect.fetch_agencies()

# 3 - Init our repo from an existing branch, and then clone it for the changes we are about to make
dolt = pdap_dolt.init(branch)
pdap_dolt.new_branch(dolt)

# 4 - Main Loop - Enumerate over all files in ./data and do our ETL proc
cwd = os.getcwd()
for datafile in os.scandir(os.path.join(cwd, "data")):
    print("--------------------------------------------------------")
    print("Found file in ./data: {}".format(datafile.name))
    # files are formatted as crapiId-start.date-end.date.csv; split into vars
    crapiID, start_date, end_date = datafile.name.split("-")
    # pass the crapiId to this function to loop through the list of agenices and retrieve just the agency for this file
    print(" [*] Searching for agency #{}".format(crapiID))
    agency = cityprotect.get_agency_by_crapiId(agencies, crapiID)
    # if the agency is already in our datasets table, it will be in this format
    dataset_url = "https://cityprotect.com/agency/{}".format(agency["agencyPathName"])

    # get the dataset (or create and get if it doesn't exist) and retrieve the record
    print(" [*] Searching PDAP datasets for url: {}".format(dataset_url))
    dataset = pdap_dolt.get_dataset(dolt, dataset_url, agency)

    # this is the id of the dataset, which will be used as the fk for the incidents table
    # incidents_fk = dataset.loc[0, 'id']

    # load the incident records in the database
    pdap_dolt.load_data(dolt, dataset, datafile)


# 5 - Commit the Changes!
pdap_dolt.commit(dolt)
