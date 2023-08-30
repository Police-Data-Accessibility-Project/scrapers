import json
import os
import sys

import configs
import requests
from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_utils.get_files import get_files

save_dir = "./data/"

response = requests.get(configs.request_url).text
parsed = json.loads(response)
dumped = json.dumps(parsed, indent=4, sort_keys=True)

with open("response.json", "w") as output:
    output.write(dumped)
output.close()

try:
    os.remove("url_name.txt")
except FileNotFoundError:
    pass

with open("response.json", "r") as output:
    data = json.load(output)
    with open("url_name.txt", "w+") as outfile:
        for i in range(len(data) + 1):
            media_dict = data["media"][i]
            outfile.write(
                str(media_dict["frontend_url"]) + ", " + str(media_dict["name"]) + "\n"
            )

    outfile.close()

try:
    os.remove("response.json")
except FileNotFoundError:
    pass

get_files(save_dir, configs.sleep_time)
