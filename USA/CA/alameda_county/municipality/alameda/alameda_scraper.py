import requests
import os
from bs4 import BeautifulSoup
import urllib
import re
import time

"""
Do not update get_files
"""

webpage = "https://www.alamedaca.gov/Departments/Police-Department/Crime-Activity"
"""
Click the links that lead to the files, and copy their paths. **NOTE:** Ensure that files all match paths, otherwise remove a level until they match
Also ensure that domain stays the same
Verify on page that the href to the file contains the domain, if it doesn't, uncomment domain
"""
web_path = "/files/assets/public/departments/alameda/police/"
domain = "https://www.alamedaca.gov"
sleep_time = 5

save_dir = "./data/monthly/"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

html_page = requests.get(webpage).text
soup = BeautifulSoup(html_page, "html.parser")

url_name = []


def extract_info(soup, source):
    for link in soup.findAll("a"):
        if link.get("href") is None:
            continue
        if not link["href"].startswith(web_path):
            continue
        url = str(link["href"])
        name = url[url.rindex("/") :]
        # name = name[:name.rindex('.')]
        with open("url_name.txt", "a") as output:
            output.write(source + url + ", " + name.strip("/") + "\n")
    print("Done")


def save_pdf(file_name, url_2, dir):
    pdf = urllib.request.urlopen(url_2)
    with open(dir + file_name, "wb") as file:
        file.write(pdf.read())
        file.close()


def get_files():
    if not os.path.isfile("url_name.txt"):
        return
    with open("url_name.txt", "r") as input_file:
        for line in input_file:
            line_list = line.split(", ")
            url_2 = line_list[0]
            file_name = line_list[1].replace(" ", "_")[:-1]
            # file_name = save_dir + file_name
            # document = requests.get(url_2, allow_redirects=True)

            if url_2.find(".pdf"):
                print(file_name)
                if "daily" in file_name:
                    dir = save_dir + "daily_bulletin/"  # Custom bit here
                    if not os.path.exists(dir):
                        os.makedirs(dir)
                    # save_pdf(file_name, url_2, dir)
                else:
                    save_pdf(file_name, url_2, save_dir)
            # This part is not really needed for this site but is left just in case
            elif url_2.find(".doc"):
                # save_path = os.path.join(save_dir, file_name+".doc")
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


try:
    os.remove("url_name.txt")
except FileNotFoundError:
    pass
extract_info(soup, domain)
get_files()

# import etl.py
