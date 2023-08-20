import os
import shutil
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

'''
connect to dolthub to retrieve record from pdap/datasets/datasets
ideally the url should not be primary key (as it is mutable)
and then grabbing the ip
'''
pk_col, pk_val = 'url', 'https://data.sfgov.org/browse?category=Public+Safety' # hopefully will change to an int or guid id in the future
cur_dir = os.getcwd()
output_dir = os.path.join(cur_dir, 'data')

# proof of concept, this could be part of our library in the future, with a bit more error handling
def get_url_dolthub(pk_col, pk_val):
    dolthub_owner = 'pdap'
    dolthub_repo = 'datasets'
    dolthub_table = 'datasets'

    print('Grabbing record from DoltHub')
    # query the DB with the id for our record
    query = '''SELECT * FROM {} WHERE {} = "{}"'''.format(dolthub_table, pk_col, pk_val)
    res = requests.get('https://www.dolthub.com/api/v1alpha1/{}/{}/{}'.format(dolthub_owner, dolthub_repo, 'master'), params={'q': query})
    response = res.json()

    # grab the url from our record
    # (which is redundant now, but a good proof of concept later)
    return response["rows"][0]["url"]

# output to file https://stackoverflow.com/questions/45978295/saving-a-downloaded-csv-file-using-python
def download_file(url, output_dir, filename):
    ''' Downloads file from the url and save it as filename '''
    # make output dir if does not exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    full_file = os.path.join(output_dir, '{}.csv'.format(filename))
    print('Retrieving {}'.format(url))
    response = requests.get(url)
    # Check if the response is ok (200)
    if response.status_code == 200:
        # Open file and write the content
        with open(full_file, 'w+b') as file:
            print('Exporting to file: {}'.format(full_file))
            # A chunk of 128 bytes
            for chunk in response:
                file.write(chunk)


# store the url
scrape = get_url_dolthub(pk_col, pk_val)

# begin the actual scrape
print('Beginning Scrape of {}'.format(scrape))
html = requests.get(scrape)
soup = BeautifulSoup(html.content, 'html.parser')

# get a link of the datasets
datasets = soup.find_all(class_="browse2-result-name-link")
for record in datasets:
    # grab the police dept datasets, two as of now
    # but not hardcoding incase the IDs change
    if 'Police Department Incident Reports' in record.string:
        url = record['href']
        dataset_id = url[url.rindex('/')+1:] # dataset id is after last / in url
        print('Found PD - Incident Reports dataset: {}'.format(dataset_id))
        # download CSV files from here
        csv_download_loc = 'https://data.sfgov.org/api/views/{}/rows.csv'.format(dataset_id)
        # grab the csv and output it
        download_file(csv_download_loc, output_dir, dataset_id)
        
        
print('Done!')
