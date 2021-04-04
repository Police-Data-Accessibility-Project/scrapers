import requests
import os
from bs4 import BeautifulSoup
import urllib
import re
import datetime
from dateutil import relativedelta

"""
Uses custom get_files(); Do not update
"""

__noted__ = "fixes shamelessly stolen from dunnousername without credit"  # Just don't delete this
webpage = "https://www.antiochca.gov/fc/police/crime-maps/this-weeks-aar.pdf"
"""
Click the links that lead to the files, and copy their paths. **NOTE:** Ensure that files all match paths, otherwise remove a level until they match
Also ensure that domain stays the same
Verify on page that the href to the file contains the domain, if it doesn't, uncomment domain
"""
web_path = "https://www.antiochca.gov/fc/police/crime-maps/"
# domain = https://www.antiochca.gov


cur_dir = os.getcwd()
save_dir = cur_dir + "/data/arrests/"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

html_page = requests.get(webpage).text


today = datetime.datetime.now()
start = today - datetime.timedelta((today.weekday() + 1) % 7)
sat = start + relativedelta.relativedelta(weekday=relativedelta.SA(-1))
sun = sat + relativedelta.relativedelta(weekday=relativedelta.SU(-1))
# Gave up on trying to use strptime to strip the time
sat_date = str(sat).replace("-", "_").split()
sun_date = str(sun).replace("-", "_").split()

file_name = "arrest_reports_" + str(sun_date[0]) + "_" + str(sat_date[0])
print(file_name)


def get_files():
    # file_name = line_list[1].replace(" ", "_")[:-1]
    # file_name = save_dir + file_name
    # document = requests.get(url_2, allow_redirects=True)
    pdf = urllib.request.urlopen(webpage)
    with open(save_dir + file_name + ".pdf", "wb") as file:
        file.write(pdf.read())
        file.close()


get_files()
