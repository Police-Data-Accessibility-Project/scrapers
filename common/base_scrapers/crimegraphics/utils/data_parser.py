import sys
import os
import requests
import json
from pathlib import Path
# from bs4 import BeautifulSoup
from bs4 import BeautifulSoup, NavigableString, Tag
from tqdm import tqdm
import pandas
from datetime import date

data_lists = []

def data_parser(configs, save_dir, table):
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
    was_desc_cont = False
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
                    # TODO: save incident description somewhere (like an obj or an array)
                    # incident_description = '' #reset back to empty
                    desc_cont = False # reset bool back
                    # remove the 'Disposition: ' prefix and any \n or . chars
                    disposition = line.split('Disposition: ')[1].strip().replace('.', '')
                    print('Disposition: ' + disposition)

                    # Format the data for writing
                    # Separating the date from the ReferenceNum
                    act_date = time_type_date[2]
                    act_date = act_date[:6] # First 6 characters are the date in YYMMDD
                    # Add underscores to separate, PDAP hates hyphens (idk why)
                    activity_date = '-'.join([act_date[:2], act_date[2:4], act_date[4:6]])
                    # Adds 20 to the beginning to match MySQL standard of yyyy-mm-dd
                    activity_date = "20" + activity_date
                    reference_num = time_type_date[2]

                    place_street_city = initiator_location[1].split(",")
                    if len(place_street_city) != 3:
                        num_add = 3 - len(place_street_city)
                        for i in range(num_add):
                            place_street_city.append("null")


                    #  ReferenceNum, ActivityDate, ActivityTime, ActivityType, ActivityInitiator, ActivityDescription, Disposition, ActivityPlace, ActivityStreet, ActivityCity
                    if was_desc_cont:
                        all_data = [reference_num, activity_date, time_type_date[0], time_type_date[1], initiator_location[0], incident_description, disposition, place_street_city[0], place_street_city[1], place_street_city[2]]
                    else:
                        all_data = [reference_num, activity_date, time_type_date[0], time_type_date[1], initiator_location[0], "null", disposition, place_street_city[0], place_street_city[1], place_street_city[2]]
                    data_lists.append(all_data)

                    was_desc_cont = False # resset bool back

                    print('======================') # pretty print a closing line saying we are done
                    count = 0 # reset back, next line will be a header

                # if true, then a prior line set this so we know to add it to the description
                elif desc_cont:
                    # print("  [!] There is a description")
                    # print("LINE: " + line)
                    incident_description = line.strip(".\n")
                    was_desc_cont = True
                # if disposition is not in the line, then treat it as the usual initiator and location line
                else:
                    initiator_location = line.split(" at ")
                    initiator_location[1] = initiator_location[1].strip(".\n")
                    # set desc_cont to True, will remain true unless `Disposition` is found in line
                    desc_cont = True
            count += 1

    # print(data_lists)
    columns = ["ReferenceNum", "ActivityDate", "ActivityTime", "ActivityType", "ActivityInitiator", "ActivityDescription", "Disposition", "ActivityPlace", "ActivityStreet", "ActivityCity"]
    index = [i[0] for i in data_lists] #first element of every list in yourlist
    not_index_list = [i for i in data_lists]
    pd = pandas.DataFrame(not_index_list, columns = columns)
    date_name = date.today()
    file_name = "_" + str(date_name).replace("-", "_") + "_"
    pd.to_csv(save_dir + configs.department_code + file_name + "bulletins")

    try:
        os.remove("text.txt")
    except FileNotFoundError:
        pass

                    # if count % 2 == 0:
                    #     initiator line.split("at")
