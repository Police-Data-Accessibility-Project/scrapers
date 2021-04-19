import os
import sys
import urllib
import re
import time
import requests
import mimetypes
import traceback
import filecmp
from datetime import date


def file_compare(save_dir, file_1, file_2, try_overwite=False, no_overwrite=False):
    file_1 = save_dir + file_1
    file_2 = save_dir + file_2

    compared = filecmp.cmp(file_1, file_2, shallow=True)

    if compared:
        print("File has not changed")
        # Not sure why I didn't just use `file_2`
        changed_file = file_2
        os.remove(changed_file)
    else:
        # I tried to just put the code to write it here, but it would've required too many arguments
        print("File has changed")
        if try_overwite == True:
            os.remove(file_1)
            # Renames the new file to the old_file's name (without the new_)
            os.rename(file_2, file_1)
        return False


# Needed a different way to check if a file existed due to us changing the file_name to add the current date.
def check_if_exists(save_dir, file_name, add_date):
    if add_date:
        print(" [*] Checking if file is present")
        print("    [?] add_date is True")
        with open("last_run.txt", "r") as last_run:
            # This deletes the date from the file_name in order to compare.
            file_name = re.sub("^[^0-9\t\n]*([0-9]{4})_0*([0-9]+?)_0*([0-9]+?)(?:\.(?:[a-zA-Z]*)?)?$", '', file_name)
            # This removes the extension, and appends the previous run's date to the file_name
            file_name = file_name.strip(".pdf") + "_" + last_run.read().strip(".pdf") + ".pdf"
            print(file_name)
            if os.path.exists(save_dir + file_name):
                prinr(" [*] File found... Returning True")
                return True
            else:
                return False
    else:
        return False


def get_pdf(
    save_dir,
    file_name,
    url_2,
    sleep_time,
    debug=False,
    try_overwite=False,
    no_overwrite=False,
    add_date=False,
):
    file_name = file_name.lstrip("/")
    print(file_name)

    if add_date is True:
        print(" [?] add_date is True")
        if not os.path.isfile("last_run.txt"):
            print(" [!] last_run.txt did not exist... Is this your first time running?")
            print("    [*] Creating last_run.txt and adding data...")
            with open("last_run.txt", "w") as last_run:
                date_name = str(date.today()).replace("-", "_")
                print(date_name)
                last_run.write(date_name)
            last_run.close()
            print(" [*] Done writing")
        else:
            check_if_exists(save_dir, file_name, add_date=add_date)

    # Default run mode, simply checks that the file does not already exists.
    # Don't need to check if
    if (
        os.path.exists(save_dir + file_name) == False
        and check_if_exists(save_dir, file_name, add_date=add_date) == False
    ):
        print(" [*] File does not exist")
        try:
            print(" [*] Requesting file....")
            pdf = urllib.request.urlopen(url_2.replace(" ", "%20"))
        except urllib.error.HTTPError:
            print("   [!] HTTP Error 404: Not Found")
            print("   [!] URL: " + str(url_2))
            print("")
            if debug:
                traceback.print_exc()
            sys.exit()

        if add_date == True:
            print(" [?] add_date is True")
            date_name = date.today()
            file_name = (
                file_name.strip(".pdf")
                + "_"
                + str(date_name).replace("-", "_")
                + ".pdf"
            )
            if debug:
                print(file_name)

        with open(save_dir + file_name, "wb") as file:
            file.write(pdf.read())
        file.close()

        time.sleep(sleep_time)
        print("Sleep")

        # If the file exists, and no_overwrite is true, then:
    elif (
        os.path.exists(save_dir + file_name) == True
        and check_if_exists(save_dir, file_name, add_date=add_date) == False
        and no_overwrite == True
    ):
        # Tries to get the file and set it to pdf
        try:
            print(" [*] Requesting file...")
            pdf = urllib.request.urlopen(url_2.replace(" ", "%20"))
        except urllib.error.HTTPError:
            print("    [!] HTTP Error 404: Not Found")
            print("")
            print("    [!] URL: " + str(url_2))
            if debug:
                traceback.print_exc()
            sys.exit()
        print("Comparing")

        # Saves the pdf while prepending with "new_"
        print(" [*] Saving as new_" + file_name)
        with open(save_dir + "new_" + file_name, "wb") as file:
            file.write(pdf.read())
        file.close()
        new_filename = "new_" + file_name

        print(" [*] Comparing...")
        if file_compare(save_dir, file_name, new_filename, no_overwrite=True) == False:
            print("    [?] Files are different")
            date_name = date.today()
            # print(date_name)
            file_name = (
                file_name.strip(".pdf")
                + "_"
                + str(date_name).replace("-", "_")
                + ".pdf"
            )
            print("   [*] file_name: "+file_name)
            print("   [*] Saving file...")
            with open(save_dir + file_name, "wb") as file:
                file.write(pdf.read())
            file.close()
    # Checks if the files exists, and that `try_overwite` is True
    elif os.path.exists(save_dir + file_name) == True and try_overwite == True:
        print(" [!!!] try_overwite is set to True, verify that you want this before continuing")
        # Tries to get the file and set it to pdf
        try:
            pdf = urllib.request.urlopen(url_2.replace(" ", "%20"))
        except urllib.error.HTTPError:
            print("HTTP Error 404: Not Found")
            print("")
            print("URL: " + str(url_2))
            if debug:
                traceback.print_exc()
            sys.exit()
        print("Comparing")

        if add_date == True:
            date_name = date.today()
            file_name = (
                file_name.strip(".pdf")
                + "_"
                + str(date_name).replace("-", "_")
                + ".pdf"
            )
            print(" [*] Date appended name: " + file_name)
        # Saves the pdf while prepending with "new_"
        with open(save_dir + "new_" + file_name, "wb") as file:
            file.write(pdf.read())
        file.close()

        new_filename = "new_" + file_name

        # Compares the file using file_compare, which will remove the new file if it has not changed
        file_compare(save_dir, file_name, new_filename)
        time.sleep(sleep_time)


def get_xls(save_dir, file_name, url_2, sleep_time, debug=False):
    if ".xls" not in file_name:
        # Allows saving as xls even if it's not in the file_name (saves in proper format)
        file_name = file_name + ".xls"
    if os.path.exists(save_dir + file_name) == False:
        try:
            print(" [*] Requesting file...")
            pdf = urllib.request.urlopen(url_2.replace(" ", "%20"))
        except urllib.error.HTTPError:
            print("    [!] HTTP Error 404: Not Found")
            print("    [!] URL: " + str(url_2))
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
            data_file.write(document.text)  # Writes using requests text 	function thing
        data_file.close()
        time.sleep(sleep_time)
        print("Sleep")
