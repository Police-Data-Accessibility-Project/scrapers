import sys
import os
import configs
import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

def crimegraphics_scraper(configs, save_dir):
    # automatically have the CLERYMenu clicked for daily crime data
    payload={'MYAGCODE': configs.department_code,
    '__EVENTTARGET': 'MainMenu$CLERYMenu',
    '__EVENTARGUMENT': 'CLERYMenu'}
    data = []

    print("Receiving Data... Please wait...")
    response = requests.request("POST", configs.url, data=payload)
    print("Data received.")
    soup = BeautifulSoup(response.text, 'html.parser')

    # this website has a bunch of empty tables with the same name
    # the 6th index has the data we need
    table = soup.find_all('table', {'class' : 'ob_gBody'})[6]

    rows = table.find_all('tr')
    for row in tqdm(rows):
        td = row.find_all('td')
        table_data = []
        for actual_data in td:
            table_data.append(actual_data.get_text())
        data.append(table_data)

    dataframe = pd.DataFrame(data = data, columns = configs.list_header)

    dataframe.to_csv(save_dir + configs.department_code + "_daily_bulletin")
