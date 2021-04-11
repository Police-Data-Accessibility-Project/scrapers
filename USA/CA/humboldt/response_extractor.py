import sys
import os
import configs
import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/common")
from base_scrapers.get_files import get_files

save_dir = "./data/"

response = requests.post(configs.request_url, data=configs.data)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class' : 'ob_gBody'})
# print(table.get_text())
rows = table.find_all('tr')
for row in rows:
    print(row.get_text())



# with open("response.json", 'w') as output:
#     output.write(dumped)
# output.close()
#
# try:
#     os.remove("url_name.txt")
# except FileNotFoundError:
#     pass
#
# with open("response.json", "r") as output:
#     data = json.load(output)
#     with open("url_name.txt", "w+") as outfile:
#         for i in range(len(data)+1):
#             media_dict = data["media"][i]
#             outfile.write(str(media_dict["frontend_url"]) + ", " + str(media_dict["name"])+"\n")
#
#     outfile.close()
#
# try:
#     os.remove("response.json")
# except FileNotFoundError:
#     pass
#
# get_files(save_dir, configs.sleep_time)
