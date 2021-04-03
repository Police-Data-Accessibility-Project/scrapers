import os
from sys import exit
import urllib
import re
import time
import requests
import traceback

def get_files(save_dir, sleep_time, delete=True, debug=False):
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

            if ".pdf" in url_2:
                # save_path = os.path.join(save_dir, file_name+".pdf")
                print(file_name)
                if os.path.exists(save_dir + file_name) == False:
                    try:
                        pdf = urllib.request.urlopen(url_2)
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
            elif ".doc" in url_2:
                if os.path.exists(save_dir + file_name) == False:
                    document = requests.get(url_2, allow_redirects=True)
                    with open(file_name, "w") as data_file:
                        data_file.write(
                            document.text
                        )  # Writes using requests text 	function thing
                    data_file.close()

            elif ".xls" in url_2:
                if ".xls" not in file_name:
                    file_name = file_name + ".xls"
                if os.path.exists(save_dir + file_name) == False:
                    document = requests.get(url_2, allow_redirects=True)
                    with open(file_name, "w") as data_file:
                        data_file.write(
                            document.text
                        )  # Writes using requests text 	function thing
                    data_file.close()

            else:
                print("Unhandled documents type")
                print("Url: " + url_2)
            time.sleep(sleep_time)
            print("Sleep")
        input_file.close()

        # Used for debugging
        if delete != False:
            os.remove("url_name.txt")
