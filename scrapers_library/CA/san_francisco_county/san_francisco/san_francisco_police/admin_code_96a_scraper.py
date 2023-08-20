import requests
import os
from bs4 import BeautifulSoup
import urllib
import re
import time
import sys
import traceback


configs = {
    "webpage": "https://www.sanfranciscopolice.org/your-sfpd/published-reports/arrests-use-force-and-stop-data-admin-code-96a",
    "web_path": "/sites/default/files/",
    "domain_included": False,
    "domain": "https://www.sanfranciscopolice.org/",
    "sleep_time": 5,
    "non_important": ["letter"],
    "debug": False,
    "csv_dir": "/csv/",
}


def extract_info(
    soup, configs, extract_name=False, name_in_url=True, configs_file=False, debug=False
):
    for link in soup.findAll("a"):
        if link.get("href") is None:
            continue
        if not link["href"].startswith(web_path):
            # Not really sure why I added these in commit 986357286bc98bc154f2333ae75934be4e5df00d,
            # But they were causing tons of terminal puke.
            # print("href not startswith")
            # print(link)
            continue
        if debug:
            print("link: " + link.get("href"))

        url = str(link["href"])
        if extract_name == False:
            # print(" [?] extract_name is False")
            date_index = url[: url.rfind("/")].rindex("/")
            name = url[date_index:]

        else:
            name = link.string
            # print(" [?] extract_name is True")
            # print(name)

        if not name_in_url:
            response = urllib.request.urlopen(domain + url)
            file_name, params = cgi.parse_header(
                response.headers.get("Content-Disposition", "")
            )
            name = file_name

        with open("url_name.txt", "a+") as output:
            if url not in output.read():
                if domain_included == True:
                    output.write(url + ", " + name + "\n")
                elif domain_included == False:
                    output.write(domain + url + ", " + name + "\n")
    print("   [*] Done extracting!")


save_dir = "./data/admin_code_96a/"
web_path = configs["web_path"]
domain = configs["domain"]
domain_included = configs["domain_included"]
webpage = configs["webpage"]
sleep_time = configs["sleep_time"]

try:
    configs_non_important = configs["non_important"]
except AttributeError:
    pass
non_important = configs_non_important


if not os.path.exists(save_dir):
    os.makedirs(save_dir)

html_page = requests.get(webpage).text
soup = BeautifulSoup(html_page, "html.parser")

url_name = []

try:
    os.remove("url_name.txt")
except FileNotFoundError:
    pass

extract_info(soup, configs)

with open("url_name.txt", "r") as og_file, open("2url_name.txt", "w") as new_file:
    for line in og_file:
        if not any(non_important in line.lower() for non_important in non_important):
            new_file.write(line)

try:
    os.remove("url_name.txt")
except FileNotFoundError:
    pass
os.rename("2url_name.txt", "url_name.txt")


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
            file_name = re.sub(
                "^[^0-9\t\n]*([0-9]{4})_0*([0-9]+?)_0*([0-9]+?)(?:\.(?:[a-zA-Z]*)?)?$",
                "",
                file_name,
            )
            # This removes the extension, and appends the previous run's date to the file_name
            file_name = (
                file_name.strip(".pdf") + "_" + last_run.read().strip(".pdf") + ".pdf"
            )
            print(file_name)
            if os.path.exists(save_dir + file_name):
                print(" [*] File found... Returning True")
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
            req = urllib.request.Request(
                url=url_2.replace(" ", "%20"),
                headers={
                    "Host": "www.sanfranciscopolice.org",
                    "User-Agent": " Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0",
                },
            )
            pdf = urllib.request.urlopen(req)
        except urllib.error.HTTPError as exception:
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

        print(file_name)
        # Get the date from the all characters prior to the last most stringg
        file_date = file_name[: file_name.rindex("/")]
        print(file_date)
        # Get the actual file's name (all characters AFTER the right most slash)
        file_name = file_name[file_name.rindex("/") :]

        save_dir = "./data/admin_code_96a/" + file_date + "/"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

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
            print("   [*] file_name: " + file_name)
            print("   [*] Saving file...")
            with open(save_dir + file_name, "wb") as file:
                file.write(pdf.read())
            file.close()
    # Checks if the files exists, and that `try_overwite` is True
    elif os.path.exists(save_dir + file_name) == True and try_overwite == True:
        print(
            " [!!!] try_overwite is set to True, verify that you want this before continuing"
        )
        # Tries to get the file and set it to pdf
        try:
            pdf = urllib.request.urlopen(url_2.replace(" ", "%20"))
        except urllib.error.HTTPError as exception:
            print("HTTP Error 404: Not Found")
            print("")
            print("URL: " + str(url_2))
            if debug:
                print(exception)
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
            if debug:
                print(line)

            line_list = line.split(", ")
            url_2 = line_list[0]
            file_name = line_list[1].replace(" ", "_")[:-1]
            file_name = file_name.replace("%20", "_")

            get_pdf(save_dir, file_name, url_2, sleep_time, debug=True)


get_files(save_dir, sleep_time)
