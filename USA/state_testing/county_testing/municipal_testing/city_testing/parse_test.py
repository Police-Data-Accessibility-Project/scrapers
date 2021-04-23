import sys
import os
import requests
import json
from pathlib import Path
# from bs4 import BeautifulSoup
from bs4 import BeautifulSoup, NavigableString, Tag

from tqdm import tqdm

data = []
with open("html.html", 'r') as output:
    output = output.read()
    soup = BeautifulSoup(output, "html.parser")

    table = soup.find("span", id="Bull")
    # print(table)

    # for a in table.childGenerator():
    #     print(type(a), str(a))
    with open("text.txt", "w") as data:
        for br in table.findAll('br'):
            next_s = br.nextSibling
            if not (next_s and isinstance(next_s,NavigableString)):
                continue
            next2_s = next_s.nextSibling
            if next2_s and isinstance(next2_s,Tag) and next2_s.name == 'br':
                text = str(next_s).strip()
                if text:
                    data.write(text + "\n")
    data.close()

    date_type_incident = []
    count = 1
    with open("text.txt", "r") as data:
        for line in data:
            if count == 1:
                print("Line 1")
                date_type = line.split("    ")
                date_type[:] = [x for x in date_type if x]
                print(date_type)
                print(f"count: {count}")

            elif count == 3:
                count = 0
                print("third")
                print(f"count: {count}")

            count += 1
            # if count % 2 == 0:
            #     initiator line.split("at")
