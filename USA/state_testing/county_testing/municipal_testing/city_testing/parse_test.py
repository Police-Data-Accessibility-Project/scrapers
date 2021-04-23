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

    time_type_date_incident = []
    count = 1
    # for keeping track of multi-line descriptions
    desc_cont = False
    incident_description = ''
    print('======================')
    with open("text.txt", "r") as data:
        for line in data:
            # the first line will have the time, record type and record ID
            if count == 1:
                time_type_date = line.split("    ") # There is a 4 space gap between the time and the activity. This splits that
                time_type_date[:] = [x for x in time_type_date if x] # Removes the 44 blank spaces between the type and the date
                time_type_date[2] = time_type_date[2].strip("\n") # Removes the new line indicators
                print(time_type_date)
            # after that we have the description (for any number of lines)
            # and ends in the disposition
            if count >= 2:
                # when we reach Disposition, it is the final part of the block
                if 'Disposition: ' in line:
                    # print out the full description we have been compiling
                    print(incident_description)
                    # TODO: save incident description somewhere (like an obj or an array)
                    incident_description = '' #reset back to empty
                    desc_cont = False # reset bool back
                    # remove the 'Disposition: ' prefix and any \n or . chars
                    disposition = line.split('Disposition: ')[1].strip().replace('.', '')
                    print('Disposition: ' + disposition)
                    print('======================') # pretty print a closing line saying we are done
                    count = 0 # reset back, next line will be a header
                # if true, then a prior line set this so we know to add it to the description
                elif desc_cont:
                    incident_description += ' ' + line.strip()
                else:
                    incident_description = line.strip()
                    print(" [*] Not an extended description")
                    initiator_location = line.split(" at ")
                    initiator_location[1] = initiator_location[1].strip(".\n")
                    print(initiator_location)
                    desc_cont = True


            count += 1

            # if count % 2 == 0:
            #     initiator line.split("at")
