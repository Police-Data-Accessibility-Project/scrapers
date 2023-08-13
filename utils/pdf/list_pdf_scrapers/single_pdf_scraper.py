import sys
from pathlib import Path
import os
import mimetypes

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p))

from utils.file_downloaders.downloaders import get_pdf


def single_pdf_scraper(
    save_dir, url_2, try_overwite=False, no_overwrite=True, flavor="stream", name_in_url=True, filename="null",
):
    """
    Scrape a single file from a website
    :param save_dir: where the files should be saved, string
    :param url_2: url of the file
    :param try_overwite: deprecated
    :param no_overwrite: replaces try_overwrite. Use with add_date for best results. Prevent overwriting of data files. (default false)
    :param flavor: "flavor" that camelot should use to exract data from pdfs. "stream" or "lattice" (default stream)
    :param name_in_url: whether or not the filename is in the url (default true)
    :param filename: allows setting of filename. will be ignored unless name_in_url is false. (default null)
    """
    # if save_dir does not exist, make the directory
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # if name_in_url is True,
    if name_in_url:
        # Extract the name from the url,
        # assuming that the filename is follows the last "/" of the url.
        file_name = url_2[url_2.rindex("/") :]

        # print it to verify that you want to use this seting
        print(file_name)

    # If name_in_url is False (default setting)
    else:
        # Set file_name to file name provided to single_pdf_scraper as parameter "filename" (defaults to null)
        file_name = filename

    # the following function is imported from ./common/utils/list_pdf_utils/
    get_pdf(
        save_dir, file_name, url_2, debug=False, sleep_time=0, try_overwite=False, no_overwrite=True, add_date=True,
    )
