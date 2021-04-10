import os
from sys import exit
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

def get_files(save_dir, sleep_time, delete=True, debug=False, name_in_url=False):
    #name_in_url = name_in_url
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
