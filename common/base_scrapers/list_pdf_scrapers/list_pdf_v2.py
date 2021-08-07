import requests
import os
from bs4 import BeautifulSoup
import urllib
import re
import time
import sys
from pathlib import Path

# This is a hack that basically loads that root common folder like a module (without you expressly needing to install it).
p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p))
from common.utils import get_files
from common.utils import extract_info

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
    # If save_dir does not exist, make the directory
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

    # Use python's requests module to fetch the webpage as plain html
    html_page = requests.get(webpage).text

    # use BeautifulSoup4 (bs4) to parse the returned html_page using BeautifulSoup4's html parser (html.parser)
    soup = BeautifulSoup(html_page, "html.parser")

    # initialize url_name table
    url_name = []

    # Attempts to remove any residual url_name.txt file as we will want to create a new clean version.
    try:
        os.remove("url_name.txt")
    except FileNotFoundError:
        # if os.remove returns FileNotFoundError, handle the error by continuing.
        pass

    print(" [*] Extracting info...")

    # the following two functions are imported from ./common/utils/list_pdf_utils/
    # send soup, the configs, and the setting of extract_name to the extract_info module
    extract_info(soup, configs, extract_name=extract_name, configs_file=configs_file, debug=debug)

    # Check added for backwards compatibility.
    # pass the variable save_dir, access sleep_time from configs, set name_in_url to the value of name_in_url, and set add_date to the value of add_date
    get_files(save_dir, sleep_time, name_in_url=name_in_url, add_date=add_date)

    # this imports etl for eric to do his magic.
    import etl

    # this section of code only runs if extract_tables is True
    if extract_tables:
        # import the pdf_extract module from ./common/etl/data_extraction.py
        from common.etl import pdf_extract

        try:
            # Pass save_dir to pdf_extract's pdf_directory param, and retrieve csv_dir from the configs
            pdf_extract(save_dir, csv_dir)

        except AttributeError:
            # this will happen if csv_dir was not defined in the configs.
            if debug:
                # because i hate having tons of stuff printed in my terminal, this will only print if debug=True (set when calling list_pdf_v2)
                print("  [INFO] csv_dir is not defined in the configs.")
                print("      If you want to save in a different location for some reason, ")
                print('      define it in the configs as `csv_dir="<folder>"`')
            # call pdf_extract again, this time without passing csv_dir to it.
            pdf_extract(pdf_directory=save_dir, flavor=flavor)
            pass

    # honestly not sure why this is down here, but there is probably a e
    # import etl.py
