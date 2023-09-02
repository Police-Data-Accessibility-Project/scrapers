import os
import sys

import requests
#from from_root import from_root

#p = from_root('CODE_OF_CONDUCT.md').parent
#sys.path.insert(1, str(p))

#https://www.muckrock.com/foi/pittsburgh-130/traffic-stops-140596/#files
#https://www.muckrock.com/api_v1/foia/?format=json&title=Traffic+Stops
#https://www.muckrock.com/foi/kingston-30521/roster-and-hire-dates-143168/#files
#https://www.muckrock.com/agency/pittsburgh-130/pittsburgh-bureau-police-357/

def get_single_file(save_folder, url, file_name=""):
    if not file_name:
        i = url.rfind("/")
        file_name = url[i:]

    file_path = save_folder + file_name

    if os.path.exists(file_path):
        print(f"File {file_path} already exists.")
        return

    if not os.path.exists(save_folder):
       os.makedirs(save_folder)

    print(f"Retrieving file {file_path}...")

    r = requests.get(url, stream=True)
    with open(file_path, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)


def get_foia_files(save_folder, url):
    pass


def get_all_agency_files(url):
    pass
