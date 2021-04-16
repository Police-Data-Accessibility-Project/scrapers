import requests
import os
from bs4 import BeautifulSoup
import urllib
import re
import time
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/common")
from common.get_files import get_files
from common.extract_info import extract_info


def list_pdf_v3(
    configs,
    save_dir,
    debug=False,
    delete=True,
    important=False,
    try_overwite=False,
    name_in_url=True,
    add_date=False,
    extract_name=False,
    no_overwrite=False,
):  # try_overwite is for get_files
    if not os.path.exists(save_dir):
        print(" [*] Making save_dir")
        os.makedirs(save_dir)
    print(" [*] Getting webpage and parsing")
    html_page = requests.get(configs.webpage).text
    soup = BeautifulSoup(html_page, "html.parser")
    if delete != False:
        try:
            os.remove("url_name.txt")
        except FileNotFoundError:
            pass
    print(" [*] Extracting info.")
    extract_info(soup, configs, extract_name=extract_name)

    if important == False:
        print(" [?] important is False, using non_important")
        non_important = configs.non_important
        print("   [*] Opening url_name.txt")
        with open("url_name.txt", "r") as og_file, open(
            "2url_name.txt", "w"
        ) as new_file:
            print("   [*] Adding only important lines to 2url_name.txt")
            for line in og_file:
                if not any(
                    non_important in line.lower() for non_important in non_important
                ):
                    new_file.write(line)
            print(" [*] Done writing")
    else:
        print(" [?] important is True, assuming important is configured")
        try:
            important = configs.important
        except AttributeError:
            # print("")
            print("   [!] Important is still named `non_important`")
            # print("")
            important = configs.non_important
        print(" [*] Opening url_name.txt")
        with open("url_name.txt", "r") as og_file, open(
            "2url_name.txt", "w"
        ) as new_file:
            print("   [*] Adding lines containing: " + str(important))
            for line in og_file:
                if any(important in line.lower() for important in important):
                    new_file.write(line)
                    print(line)
            print(" [*] Done writing")
    if debug != True:
        try:
            os.remove("url_name.txt")
        except FileNotFoundError:
            pass
        os.rename("2url_name.txt", "url_name.txt")

    get_files(
        save_dir,
        configs.sleep_time,
        debug=debug,
        delete=delete,
        try_overwite=try_overwite,
        name_in_url=name_in_url,
        no_overwrite=no_overwrite,
        add_date=add_date,
    )
