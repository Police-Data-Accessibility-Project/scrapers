import os
import sys
import urllib
import re
import time
import requests
import mimetypes
import traceback

from pathlib import Path
p = Path(__file__).resolve().parents[2]
sys.path.insert(1, str(p) + '/common')

# from file_downloaders.downloaders import get_doc, get_pdf, get_xls
from file_downloaders import *

def get_files(save_dir, sleep_time, delete=True, debug=False, name_in_url=False):
    name_in_url = name_in_url
    print("name_in_url " + str(name_in_url))
    if not os.path.isfile("url_name.txt"):
        return
    with open("url_name.txt", "r") as input_file:
        for line in input_file:
            print(line)

            line_list = line.split(", ")
            url_2 = line_list[0]
            file_name = line_list[1].replace(" ", "_")[:-1]
            # file_name = save_dir + file_name
            # document = requests.get(url_2, allow_redirects=True)
            response = requests.get(url_2)
            content_type = response.headers['content-type']
            extension = mimetypes.guess_extension(content_type)

            if name_in_url == False:
                if ".pdf" in extension:
                    # save_path = os.path.join(save_dir, file_name+".pdf")
                    print(file_name)
                    get_pdf(save_dir, file_name, url_2, debug, sleep_time)

                elif ".doc" in extension:
                    get_doc(save_dir, file_name, url_2, sleep_time)

                elif ".xls" in extension:
                    get_xls(save_dir, file_name, url_2, sleep_time)

                else:
                    print("Unhandled documents type")
                    print("Url: " + url_2)

                input_file.close()
            else:
                print("ELSE")
                import cgi
                response = urllib.request.urlopen(url_2)
                _, params = cgi.parse_header(response.headers.get('Content-Disposition', ''))
                print(_, params)
                file_name = params['filename']

                if ".pdf" in extension:
                    # save_path = os.path.join(save_dir, file_name+".pdf")
                    print(file_name)
                    get_pdf(save_dir, file_name, url_2, debug, sleep_time)

                elif ".doc" in extension:
                    get_doc(save_dir, file_name, url_2, sleep_time)

                elif ".xls" in extension:
                    get_xls(save_dir, file_name, url_2, sleep_time)

                else:
                    print("Unhandled documents type")
                    print("Url: " + url_2)

                input_file.close()

        # Used for debugging
        if delete != False:
            os.remove("url_name.txt")
