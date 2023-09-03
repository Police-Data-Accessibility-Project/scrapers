import json
import os
import sys
from itertools import chain

import requests


def get_single_file(save_folder, url, file_name=""):
    """Downloads a single file from Muckrock.

    Args:
        save_folder (str): Relative path where the file will be saved.
        url (str): Download URL for the file.
        file_name (str, optional): What the file being downloaded will be named. Defaults to last part of url.
    """
    if not file_name:
        # Retrieve the file name from the URL
        i = url.rfind("/") + 1
        file_name = url[i:]

    file_path = save_folder + file_name

    if os.path.exists(file_path):
        print(f"Already exists: {file_path}")
        return

    if not os.path.exists(save_folder):
       os.makedirs(save_folder)

    print(f"Downloading: {file_path}")

    r = requests.get(url, stream=True)
    with open(file_path, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)


def get_foi_files(save_folder, url, ignore=[]):
    """Downloads all files from a foi request.

    Args:
        save_folder (str): Relative path where the files will be saved.
        url (str): URL for the foi request.
        ignore (list, optional): A list of strings for files to be ignored. Compares from the file download url, datetime, and file title. Defaults to [].
    """
    # Retrieve the foi ID from the URL
    start_index = url.rfind("-") + 1
    end_index = url.rfind("/")
    foi_id = url[start_index:end_index]

    # Retrieve the jurisdiction ID from the URL
    end_index = url.rfind("/", 28, start_index)
    start_index = url.rfind("-", 28, end_index) + 1
    jurisdiction_id = url[start_index:end_index]

    comms = get_communications_data(jurisdiction_id, foi_id)

    if not comms:
        print(f"FOI request could not be found: {url}")
        return

    for comm in comms:
        for file in comm["files"]:
            file_url = file["ffile"]

            if ignore and file_ignored(file, ignore):
                continue

            get_single_file(save_folder, file_url)
        

def get_all_agency_files(save_folder, url, ignore=[]):
    """Downloads all files from an agency.

    Args:
        save_folder (str): Relative path where the files will be saved.
        url (url): URL for the agency.
        ignore (list, optional): A list of strings for files to be ignored. Compares from the file download url, datetime, and file title. Defaults to [].
    """
    # Retrieve the agency ID from the URL
    start_index = url.rfind("-") + 1
    end_index = url.rfind("/")
    agency_id = url[start_index:end_index]

    files = get_files_list(agency_id)

    for file in files:
        file_url = file["ffile"]

        if ignore and file_ignored(file, ignore):
            continue

        path = f"{save_folder}{file['path']}/"

        get_single_file(path, file_url)


def get_communications_data(jurisdiction_id, foi_id):
    """Companion function to get_foi_files(). 

    Retrieves communications data from the Muckrock API for specified FOIA ID.

    Args:
        jurisdiction_id (str): Muckrock jurisdiction ID to be searched through.
        foi_id (str): Muckrock FOIA ID to search for.

    Returns:
        list: List of communications dictionaries. False if none could be found.
    """    
    page = 1

    while True:
        api_url = f"https://www.muckrock.com/api_v1/foia/?format=json&jurisdiction={jurisdiction_id}&page_size=100&page={page}"
        response = requests.get(api_url)
        response_json = json.loads(response.text)

        for foi in response_json["results"]:
            if foi["id"] == int(foi_id):
                return foi["communications"]
        
        if not response_json["next"]:
            return False

        page += 1


def get_files_list(agency_id):
    """Companion function to get_all_agency_files().

    Retrieves all file dictionaries for a given agency.

    Args:
        agency_id (str): Muckrock agency ID to be searched through.

    Returns:
        list: List of file dictionaries.
    """    
    page = 1
    files = []

    while True:
        api_url = f"https://www.muckrock.com/api_v1/foia/?format=json&agency={agency_id}&page_size=100&page={page}"
        response = requests.get(api_url)
        response_json = json.loads(response.text)

        for foi in response_json["results"]:
            for comm in foi["communications"]:
                files.append(comm["files"])
                # Add path key and value to the dictionaries just added to files
                # This is used later for the folder names to sort downloaded files into 
                files[-1] = [dict(file, **{"path": foi["title"].replace("/", "|")}) for file in files[-1]]
        
        if not response_json["next"]:
            break

        page += 1
    
    # Flatten the list
    files = list(chain(*files))
    return files


def file_ignored(file, ignore):
    """Check if a file should be ignored.

    Compares from the file download url, datetime, and file title.

    Args:
        file (dict): File dictionary.
        ignore (list): List of strings for files to be ignored.

    Returns:
        bool: True if file is to be ignored, False otherwise.
    """    
    title = file["title"]
    file_url = file["ffile"]
    datetime = file["datetime"]

    if any(
        ignored_item in title or ignored_item in file_url or datetime.startswith(ignored_item)
        for ignored_item in ignore
    ):
        print(f"Ignored: {file_url}")
        return True

    return False
