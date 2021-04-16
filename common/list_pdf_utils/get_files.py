import os
import sys
import urllib
import re
import time
import requests
import mimetypes
import traceback
from tqdm import tqdm
from pathlib import Path

p = Path(__file__).resolve().parents[2]
sys.path.insert(1, str(p) + "/common")
from .utils.file_downloaders import get_doc, get_pdf, get_xls


def get_files(
    save_dir,
    sleep_time,
    delete=True,
    debug=False,
    name_in_url=True,
    try_overwite=False,
    domain_included=False,
    no_overwrite=False,
    add_date=False,
    silent=False,
):
    name_in_url = name_in_url
    if not os.path.isfile("url_name.txt"):
        print(" [!] url_name.txt does not exist. Did you call extract_info first?")
        return

    print(" [*] Opening url_name.txt")
    with open("url_name.txt", "r") as input_file:

        # Counts the number of lines in the file
        print("    [*] Counting lines")
        line_count = len(input_file.readlines())

        print(f"     [?] There are {line_count} lines")

        # If the number of lines is less than or equal to 1, set sleep_time to 0 (No need to sleep for a single file)
        if line_count <= 1:
            print("    [?] One line found, setting sleep_time to 0")
            sleep_time = 0
    input_file.close()

    # Not doing this breaks the code due to `readlines()` for some reason. Unsure why
    with open("url_name.txt", "r") as input_file:
        print(" [*] Getting files")
        iter = 0

        # Iterate through the lines in `url_name.txt`
        for line in tqdm(input_file):
            iter += 1
            if debug:
                print(line)

            line_list = line.split(", ")
            url_2 = line_list[0]
            file_name = line_list[1].replace(" ", "_")[:-1]
            file_name = file_name.replace("%20", "_")

            response = requests.get(url_2)
            content_type = response.headers["content-type"]
            extension = mimetypes.guess_extension(content_type)

            # Might be a good idea to add a check if the extension has changed (eventually)
            if iter == 0:
                print(" [*] Extension is " + extension)

            # If the name IS in the url
            if name_in_url == True:

                # Ensures that it only prints once.
                if iter == 0:
                    print(" [?] name_in_url is True")

                if ".pdf" in extension:
                    # save_path = os.path.join(save_dir, file_name+".pdf")
                    if not silent:
                        print("   [*] Getting file " + file_name)
                    get_pdf(
                        save_dir,
                        file_name,
                        url_2,
                        debug,
                        sleep_time,
                        try_overwite,
                        no_overwrite,
                        silent,
                    )

                    if not silent:
                        print("   [*]Sleeping for: " + str(sleep_time))

                elif ".doc" in extension:
                    print("Getting doc: " + file_name)
                    get_doc(save_dir, file_name, url_2, sleep_time)

                elif ".xls" in extension:
                    get_xls(save_dir, file_name, url_2, sleep_time)

                else:
                    print("Unhandled documents type")
                    print("Url: " + url_2)

            # If name_in_url is False
            else:
                import cgi

                if not debug:
                    response = urllib.request.urlopen(url_2)
                    file_name, params = cgi.parse_header(
                        response.headers.get("Content-Disposition", "")
                    )
                    if "=" in file_name:
                        file_name = file_name.split("=")
                    elif ":" in file_name:
                        filename = file_name.split(":")
                    try:
                        file_name = file_name[1].strip('"')
                    except IndexError:
                        print("file_name was blank, might want to check that.")
                        print("(Likely caused by using setting name_in_url=False)")
                        pass

                if debug:
                    response = urllib.request.urlopen(url_2)
                    print(response)
                    file_name, params = cgi.parse_header(
                        response.headers.get("Content-Disposition", "")
                    )
                    print("file_name: " + str(file_name) + ", params: " + str(params))
                    if "=" in file_name:
                        file_name = file_name.split("=")
                    elif ":" in file_name:
                        filename = file_name.split(":")
                    print(f"file_name: {file_name}")
                    try:
                        file_name = file_name[1].strip('"')
                    except IndexError as exception:
                        print("file_name was blank, might want to check that.")
                        print("(Likely caused by using setting name_in_url=False)")
                        print(exception)
                        pass
                    print(f"file_name: {file_name}")

                if ".pdf" in extension:
                    # save_path = os.path.join(save_dir, file_name+".pdf")
                    print(" [*] Getting " + file_name)
                    get_pdf(save_dir, file_name, url_2, debug, sleep_time, try_overwite)

                elif ".doc" in extension:
                    get_doc(save_dir, file_name, url_2, sleep_time)

                elif ".xls" in extension:
                    get_xls(save_dir, file_name, url_2, sleep_time)

                else:
                    print("Unhandled documents type")
                    print("Url: " + url_2)

    input_file.close()

    # Used for debugging
    if delete is not False:
        os.remove("url_name.txt")
