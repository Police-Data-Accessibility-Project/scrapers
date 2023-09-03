import json
import os
import sys
from itertools import chain

import requests


def get_single_file(save_folder, url, file_name=""):
    if not file_name:
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


def get_foia_files(save_folder, url, ignore=[]):
    start_index = url.rfind("-") + 1
    end_index = url.rfind("/")
    foia_id = url[start_index:end_index]

    end_index = url.rfind("/", 28, start_index)
    start_index = url.rfind("-", 28, end_index) + 1
    jurisdiction_id = url[start_index:end_index]

    comms = get_communications_data(jurisdiction_id, foia_id)

    if not comms:
        print(f"FOIA request could not be found: {url}")
        return

    for comm in comms:
        for file in comm["files"]:
            file_url = file["ffile"]

            if ignore and file_ignored(file, ignore):
                continue

            get_single_file(save_folder, file_url)
        

def get_all_agency_files(save_folder, url, ignore=[]):
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


def get_communications_data(jurisdiction_id, foia_id):
    page = 1

    while True:
        api_url = f"https://www.muckrock.com/api_v1/foia/?format=json&jurisdiction={jurisdiction_id}&page_size=100&page={page}"
        response = requests.get(api_url)
        response_json = json.loads(response.text)

        for foia in response_json["results"]:
            if foia["id"] == int(foia_id):
                return foia["communications"]
        
        if not response_json["next"]:
            return False

        page += 1


def get_files_list(agency_id):
    page = 1
    files = []

    while True:
        api_url = f"https://www.muckrock.com/api_v1/foia/?format=json&agency={agency_id}&page_size=100&page={page}"
        response = requests.get(api_url)
        response_json = json.loads(response.text)

        for foia in response_json["results"]:
            for comm in foia["communications"]:
                files.append(comm["files"])
                files[-1] = [dict(file, **{"path": foia["title"].replace("/", "|")}) for file in files[-1]]
        
        if not response_json["next"]:
            break

        page += 1
    
    files = list(chain(*files))
    return files


def file_ignored(file, ignore):
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
