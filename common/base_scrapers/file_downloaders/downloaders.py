import os
import sys
import urllib
import re
import time
import requests
import mimetypes
import traceback

def get_pdf(save_dir, file_name, url_2, debug, sleep_time):
    if os.path.exists(save_dir + file_name) == False:
        try:
            pdf = urllib.request.urlopen(url_2.replace(" ", "%20"))
        except urllib.error.HTTPError:
            print("HTTP Error 404: Not Found")
            print("URL: " + str(url_2))
            print("")
            if debug:
                traceback.print_exc()
            exit()
        with open(save_dir + file_name, "wb") as file:
            file.write(pdf.read())
        file.close()
        time.sleep(sleep_time)
        print("Sleep")

def get_xls(save_dir, file_name, url_2, sleep_time):
    if ".xls" not in file_name:
        # Allows saving as xls even if it's not in the file_name (saves in proper format)
        file_name = file_name + ".xls"
    if os.path.exists(save_dir + file_name) == False:
        try:
            pdf = urllib.request.urlopen(url_2.replace(" ", "%20"))
        except urllib.error.HTTPError:
            print("HTTP Error 404: Not Found")
            print("URL: " + str(url_2))
            print("")
            if debug:
                traceback.print_exc()
            exit()
        with open(save_dir + file_name, "wb") as file:
            file.write(pdf.read())
        file.close()
        time.sleep(sleep_time)
        print("Sleep")

def get_doc(save_dir, file_name, url_2, sleep_time):
    if os.path.exists(save_dir + file_name) == False:
        document = requests.get(url_2.replace(" ", "%20", allow_redirects=True))
        with open(file_name, "w") as data_file:
            data_file.write(
                document.text
            )  # Writes using requests text 	function thing
        data_file.close()
        time.sleep(sleep_time)
        print("Sleep")
