import datetime
import os
import re
import sys
import time
import urllib
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from utils.meta.metadata.metadata import create_metadata
from utils.pdf.list_pdf_utils.extract_info import extract_info
from utils.pdf.list_pdf_utils.get_files import get_files

"""
configs = {
    "webpage": "",
    "web_path": "",
    "domain_included": "",
    "domain": "",
    "sleep_time": "",
    "non_important": "",
    "debug": "",
    "csv_dir": "",
}
"""


def list_pdf_v2(
    configs,
    save_dir,
    name_in_url=True,
    extract_name=False,
    add_date=False,
    try_overwite=False,
    no_overwrite=False,
    debug=False,
    flavor="stream",
    extract_tables=False,
    configs_file=False,
):
    """
    Scrape a list of files from a website
    :param configs: dictionary of configuration
    :param save_dir: where the files should be saved, string
    :param name_in_url: whether or not the filename is in the url (default true)
    :param extract_name: extract name from an href's string instead of url, set name_in_url false (default false)
    :param add_date: used when a document is overwritten on a website. set no_overwrite true if using. (default false)
    :param try_overwite: mostly deprecated. ask before using
    :param no_overwrite: replaces try_overwrite. Use with add_date for best results. Prevent overwriting of data files. (default false)
    """
    run_start = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")
  
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Check added for backwards compatibility.
    if not configs_file:  # Default setting
        webpage = configs["webpage"]
        sleep_time = configs["sleep_time"]
        if extract_tables:
            try:
                csv_dir = configs["csv_dir"]
            except AttributeError:
                pass
    else:
        webpage = configs.webpage
        sleep_time = configs.sleep_time
        if extract_tables:
            try:
                csv_dir = configs.csv_dir
            except AttributeError:
                pass

    html_page = requests.get(webpage).text
    soup = BeautifulSoup(html_page, "html.parser")

    url_name = []

    try:
        os.remove("url_name.txt")
    except FileNotFoundError:
        pass

    print(" [*] Extracting info...")

    extract_info(soup, configs, extract_name=extract_name, configs_file=configs_file, debug=debug)

    get_files(save_dir, sleep_time, name_in_url=name_in_url, add_date=add_date)

    if extract_tables:
        from utils.pdf.list_pdf_utils.pdf_extract import pdf_extract

        try:
            pdf_extract(save_dir, csv_dir)
        except AttributeError:
            # this will happen if csv_dir was not defined in the configs.
            if debug:
                print("  [INFO] csv_dir is not defined in the configs.")
                print("      If you want to save in a different location for some reason, ")
                print('      define it in the configs as `csv_dir="<folder>"`')
            # call pdf_extract again, this time without passing csv_dir to it.
            pdf_extract(pdf_directory=save_dir, flavor=flavor)
            pass

    create_metadata(webpage, run_start)
