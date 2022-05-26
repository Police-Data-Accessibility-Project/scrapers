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
from common.utils.metadata import create_metadata

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
    flavor="stream",
    extract_tables=False,
    configs_file=False,
):  # try_overwite is for get_files
    """
    Scrape a list of files from a website
    :param configs: dictionary of configuration
    :param save_dir: where the files should be saved, string
    :param debug: enables more verbose output. (default False)
    :param delete: whether to delete url.txt after script finishes. useful for debugging. (default False)
    :param important: allows switching from ignoring files matching name to only scraping files matching name (default false)
    :param try_overwite: mostly deprecated. ask before using.
    :param name_in_url: whether or not the filename is in the url (default true)
    :param add_date: used when a document is overwritten on a website. set no_overwrite true if using. (default false)
    :param extract_name: extract name from an href's string instead of url, set name_in_url false (default false)
    :param no_overwrite: replaces try_overwrite. Use with add_date for best results. Prevent overwriting of data files. (default false)
    :param flavor: "flavor" that camelot should use to exract data from pdfs. "stream" or "lattice" (default stream)
    :param extract_tables: whether to extract tables from pdf or not. (default false)
    :param configs_file: reverse compatibility parameter, leave false
    """
    # if save_dir does not exist, make the directory
    if not os.path.exists(save_dir):
        print(" [*] Making save_dir")
        os.makedirs(save_dir)

    # Check added for backwards compatibility.
    if not configs_file:  # Default setting
        webpage = configs["webpage"]
        sleep_time = configs["sleep_time"]
        try:
            configs_non_important = configs["non_important"]
        except AttributeError:
            pass
        if extract_tables:
            try:
                csv_dir = configs["csv_dir"]
            except AttributeError:
                pass

    else:
        webpage = configs.webpage
        sleep_time = configs.sleep_time
        try:
            configs_non_important_ = configs.non_important
        except AttributeError:
            pass
        if extract_tables:
            try:
                csv_dir = configs.csv_dir
            except AttributeError:
                pass

    print(" [*] Getting webpage and parsing")

    # use python's requests module to fetch the webpage as plain html
    html_page = requests.get(webpage).text

    # use BeautifulSoup4 (bs4) to parse the returned html_page using BeautifulSoup4's html parser (html.parser)
    soup = BeautifulSoup(html_page, "html.parser")

    # if delete is not false (i think that would be true then), try to remove url_name.txt
    # the delete option is primarily used for debugging
    if delete is not False:
        try:
            os.remove("url_name.txt")
        except FileNotFoundError:
            pass

    print(" [*] Extracting info.")

    # the following function is imported from ./common/utils/list_pdf_utils/
    # send soup, the configs, and the setting of extract_name to the extract_info module
    extract_info(
        soup, configs, extract_name=extract_name, name_in_url=name_in_url, configs_file=configs_file,
    )

    # if important is false,
    if not important:
        print(" [?] important is False, using non_important")

        # retrieve list of non_important keywords from configs file
        non_important = configs_non_important

        print("   [*] Opening url_name.txt")

        # open and read url_name.txt, and open 2url_name.txt,
        with open("url_name.txt", "r") as og_file, open("2url_name.txt", "w") as new_file:
            print("   [*] Adding only important lines to 2url_name.txt")

            # iterate over the lines in url_name.txt (og_file)
            for line in og_file:
                # check if any keywords from non_important are NOT in the line
                if not any(non_important in line.lower() for non_important in non_important):
                    # if there aren't any keywords fom non_important in the line,
                    # write it to 2url_name.txt (new_file)
                    new_file.write(line)
                # print("   [*] The following lines were not added: " + str(line))
            print(" [*] Done writing")

    # if important is true,
    else:
        print(" [?] important is True, assuming important is configured")
        # attempt to import important from configs
        try:
            # Check added for backwards compatibility.
            # Can't combine this into the main check due to the try except block
            if not configs_file:  # Default setting
                important = configs["important"]
            else:
                important = configs.important
        except AttributeError:
            # print("")
            print("   [!] Important is still named `non_important`")
            # print("")

            # As there is no variable called important in configs, use non_important instead.
            # Check added for backwards compatibility.
            if not configs_file:  # Default setting
                important = configs["non_important"]
            else:
                important = configs.non_important
        print(" [*] Opening url_name.txt")

        # open and read url_name.txt, and open 2url_name.txt,
        with open("url_name.txt", "r") as og_file, open("2url_name.txt", "w") as new_file:
            print("   [*] Adding lines containing: " + str(important))
            # iterate over the lines in url_name.txt (og_file)
            for line in og_file:
                # check if any keywords from non_important are in the line
                if any(important in line.lower() for important in important):
                    # if one of the keywords is in the line, write it to 2url_name.txt (new_file)
                    new_file.write(line)
                    print(line)
            print(" [*] Done writing")

    # if debug is false, can probably be rewritten as "if not debug:"
    # functions the same as the delete variable tbh
    if not debug:
        try:
            os.remove("url_name.txt")
        except FileNotFoundError:
            pass
        os.rename("2url_name.txt", "url_name.txt")

    # the following function is imported from ./common/utils/list_pdf_utils/
    # call get_files and pass parameters supplied to `list_pdf_v3` to get_files
    get_files(
        save_dir,
        sleep_time,
        debug=debug,
        delete=delete,
        try_overwite=try_overwite,
        name_in_url=name_in_url,
        no_overwrite=no_overwrite,
        add_date=add_date,
    )


    # this section of code only runs if extract_tables is True
    if extract_tables:
        # import the pdf_extract module from ./common/etl/data_extraction.py
        from common.etl import pdf_extract

        try:
            # Pass save_dir to pdf_extract's pdf_directory param
            pdf_extract(save_dir, csv_dir)

        except AttributeError:
            # this will happen if csv_dir was not defined in the configs.
            if debug:
                # because i hate having tons of stuff printed in my terminal, this will only print if debug=True (set when calling list_pdf_v3)
                print("  [INFO] csv_dir is not defined in the configs.")
                print("      If you want to save in a different location for some reason, ")
                print('      define it in the configs as `csv_dir="<folder>"`')
            # call pdf_extract again, this time without passing csv_dir to it.
            pdf_extract(pdf_directory=save_dir, flavor=flavor)
            pass
    
    create_metadata(webpage)
    # import etl for eric (this likely will not work due to etl being in common)
    # honestly not sure why this is down here, but there is probably a reason
    # import etl.py
