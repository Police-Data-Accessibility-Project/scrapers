import os
import sys
import urllib
import re
import time
import requests
import mimetypes
import traceback
from pathlib import Path
import logging

p = Path(__file__).resolve().parents[2]
sys.path.insert(1, str(p))

from common.utils.file_downloaders import get_doc, get_pdf, get_xls


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
):
    """
    Download files provided by extract_info
    :param save_dir: directory to save files to
    :param sleep_time: number of seconds to sleep, set to robots.txt crawler-delay
    :param delete: whether to delete url_name.txt after completion, useful for debugging (default true)
    :param debug: whether to print debug information (default false)
    :param name_in_url: if the file's name is in the url (default True)
    :param try_overwite: deprecated
    :param domain_included: whether the domain is in the html's href (almost always false) (default false)
    :param no_overwrite: replaces try_overwrite. Use with add_date for best results. Prevent overwriting of data files. (default false)
    param add_date: used with no_overwrite. appends date scraped to file. (default false)
    """

    if debug:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    else:
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    # Why do I have this?
    name_in_url = name_in_url

    if not os.path.isfile("url_name.txt"):
        print("url_name.txt does not exist. Did you call extract_info first?")
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
        lines = input_file.read()
        for line in lines:
            print(line)
    input_file.close()

    first_line = 0
    with open("url_name.txt", "r") as input_file:
        print(" [*] Getting files")
        for line in input_file:
            first_line += 1
            logging.debug("line: " + str(line))

            line_list = line.split(", ")
            url_2 = line_list[0]
            file_name = line_list[1].replace(" ", "_")[:-1]
            file_name = file_name.replace("%20", "_")

            response = requests.get(url_2)
            content_type = response.headers["content-type"]
            extension = mimetypes.guess_extension(content_type)
            print("    [*] Extension is " + extension)

            # If the name IS in the url
            if name_in_url == True:
                if first_line <= 1:
                    print(" [?] name_in_url is True")

                #  All of these separate functions are likely unecessary
                if ".pdf" in extension:
                    # save_path = os.path.join(save_dir, file_name+".pdf")
                    print("   [*] Getting file " + file_name)
                    get_pdf(
                        save_dir, file_name, url_2, debug, sleep_time, try_overwite, no_overwrite, add_date=add_date,
                    )
                    print("   [*]Sleeping for: " + str(sleep_time))

                elif ".doc" in extension:
                    print("Getting doc: " + file_name)
                    get_doc(save_dir, file_name, url_2, sleep_time)

                elif ".xls" in extension:
                    get_xls(save_dir, file_name, url_2, sleep_time)

                else:
                    print(" [!!!] Unhandled documents type")
                    print(" [!!!] Url: " + url_2)

            # If name_in_url is False
            else:
                import cgi


                response = urllib.request.urlopen(url_2)
                logging.debug("Response: " + str(response))
                file_name, params = cgi.parse_header(response.headers.get("Content-Disposition", ""))
                logging.debug("file_name: " + str(file_name) + ", params: " + str(params))
                if "=" in file_name:
                    file_name = file_name.split("=")
                elif ":" in file_name:
                    filename = file_name.split(":")
                logging.debug(f"file_name: {file_name}")
                try:
                    file_name = file_name[1].strip('"')
                except IndexError:
                    print(" [!!!] file_name was blank, might want to check that.")
                    print(" [!!!] (Likely caused by using setting name_in_url=False)")
                    logging.exception()
                    pass
                logging.debug(f"file_name: {file_name}")

                if ".pdf" in extension:
                    # save_path = os.path.join(save_dir, file_name+".pdf")
                    print(file_name)
                    get_pdf(save_dir, file_name, url_2, debug, sleep_time, try_overwite)

                elif ".doc" in extension:
                    get_doc(save_dir, file_name, url_2, sleep_time)

                elif ".xls" in extension:
                    get_xls(save_dir, file_name, url_2, sleep_time)

                elif ".zip" in extension:
                    urllib.request.urlretrieve(url_2, save_dir + file_name.replace("/", "-"))

                else:
                    print(" [!!!] Unhandled documents type")
                    print(" [!!!] Url: " + url_2)

    input_file.close()

    # Used for debugging
    if delete is not False:
        os.remove("url_name.txt")
