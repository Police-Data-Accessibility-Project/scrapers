'''
PDAP - Dolt

Library for re-usable functions pertaining to our dolt instance
'''

from doltpy.cli import Dolt
from doltpy.cli.write import write_file, write_pandas
from doltpy.sql import DoltSQLServerContext, ServerConfig
from doltpy.cli.read import read_pandas, read_pandas_sql
import pandas as pd
import os
import requests
import json
import sys
import uuid

# TURN OFF FOR PROD
dev_mode = True

dolthub_org = 'pdap'
dolthub_repo= 'datasets'
dolthub_fullrepo = dolthub_org + '/' + dolthub_repo
dolthub_table = 'datasets'
dolthub_incident_reports_table = 'data_incident_reports'
if dev_mode == True: dolthub_branch = 'data_types-sandbox'
else: dolthub_branch = 'master'
dolt = None # placeholder


# init our dolt repo, we can pass a custom branch or it will fall back to master
def init(branch=dolthub_branch):
    # check if repo already exists in our cwd
    cwd = os.getcwd()
    path = os.path.join(cwd, dolthub_repo)
    if os.path.isdir(path):
        print(' [*] DoltHub Repo found in ./{}, re-initializing'.format(dolthub_repo))
        dolt = Dolt(path)
        # make sure the data isn't stale and pull new data
        print(' [*] Performing `dolt pull` to ensure repo is up to date')
        # check what branch we have
        b = Dolt.branch(dolt)[0].name
        print('   [*] Current Branch: {}'.format(b))
        # if we are not on the branch passed, then switch
        if b != branch:
            try:
                print('   [*] Checking out branch: {}'.format(branch))
                Dolt.checkout(dolt, branch=branch)
                # recheck the branch
                b = Dolt.branch(dolt)[0].name
                print('   [*] Current Branch: {}'.format(b))
            except:
                pass

        p = Dolt.pull(dolt)
        s = Dolt.status(dolt)
        
        print('   [*] Current Status: {}'.format(s))
    else:
        # clone the database from DoltHub, save it into a var to be referenced for read/write purposes
        print(' [*] Cloning DoltHub Repo: {} into ./{}'.format(dolthub_fullrepo, dolthub_repo))
        dolt = Dolt.clone(dolthub_fullrepo, branch=branch)
        b = Dolt.branch(dolt)[0].name
        print('   [*] Current Branch: {}'.format(b))
    return dolt

'''
    Search the [pdap/datasets].[datasets] database for the specified URL
    If it does not exist, pass agency info to new func to create it
'''
def get_dataset(dolt, dataset_url, agency):
    # data = read_pandas_sql(dolt, "SELECT * FROM datasets WHERE url = 'https://cityprotect.com/agency/540048e6-ee66-4a6f-88ae-0ceb93717e50'")
    data = read_pandas_sql(dolt, "SELECT * FROM datasets WHERE url = '{}'".format(dataset_url))
    # check if a result was passed
    if data.shape[0] == 0:
        print(" [X] No Dataset Found! Proceeding to Add New Dataset...")
        return new_dataset(dolt, agency, dataset_url)
    if data.shape[0] == 1: 
        print(" [!] Found Existing Dataset Record: ID #{}!".format(data.loc[0, 'id']))
        return data


# Pass State, FIPS, City to get municipality code
def get_municipality(dolt, state, fips, city):
    # data = read_pandas_sql(dolt, "SELECT * FROM datasets WHERE url = 'https://cityprotect.com/agency/540048e6-ee66-4a6f-88ae-0ceb93717e50'")
    data = read_pandas_sql(dolt, "SELECT * FROM `municipalities`where  state_iso = '{}' and county_fips = '{}' and name = '{}'".format(state, fips, city))
    # check if a result was passed
    if data.shape[0] == 0:
        print("     [X] No Matching Municipalities")
        return None
    if data.shape[0] == 1: 
        print("     [!] Found Muncipality: ID #{}!".format(data.loc[0, 'id']))
        return data.loc[0, 'id']

# before we actually start making changes, we should make a new branch
def new_branch(dolt):
    # generates a modifier at the end
    # city-protect-import-py-5d365f9b
    new_branch = 'city-protect-import-py-{}'.format(str(uuid.uuid4()).split('-')[0])
    try:
        print('   [*] Creating new Branch: {}'.format(new_branch))
        b = Dolt.branch(dolt, branch_name=dolthub_branch, new_branch=new_branch, copy=True)
        #print(b)
        Dolt.checkout(dolt, branch=new_branch)
        print('   [*] Checking out new branch...')
        # recheck the branch
        b = Dolt.branch(dolt)[0].name
        print('   [*] Current Branch: {}'.format(b))
    except:
        print('   [!] FATAL ERROR: CANNOT CHECKOUT NEW BRANCH. ABORTING')
        sys.exit()

'''
Use the agency data from city protect to derive a new dataset
The following columns need filled: 
url [url of dataset]
name [name of pd]
aggregation_level [state, county, municipal]
source_type_id [fk from source_types, for CityProtect will always be 3 - Third Party]
data_types_id [fk from data_types, for CityProtect will always be 10 - Incident_Reports]
format_types_id [fk from format_types, for CityProtect will always be 2 - CityProtect]
state_iso [two digit state code, ie 'IN']
county_fips [fk to counties table, can be searched via FCC API]
city_id [fk to municipalities, can use fips, state, city maybe to locate?]
consolidator [CityProtect]
update_frequency [quarterly (bulk downloads are quarterly)]
portal_type [CityProtect]
coverage_start [no clue how to populate. Bulk downloads, use first file date?]
scraper_path [null, would need manual population]
notes [null]
'''
def new_dataset(dolt, agency, url):
    print('   [*] Adding a New Dataset:')
    name = agency['name']
    print('     [*] name: {}'.format(name))
    print('     [*] url: {}'.format(url))

    # it appears most will have 'County' in the name
    # else make it municipal
    if 'County' in name:
        aggregation_level = 'county'
    else:
        aggregation_level = 'municipal'
    
    print('     [*] aggregation level: {}'.format(aggregation_level))
    
    source_type_id = 3 # Third Party
    print('     [*] source type: {}'.format('Third Party'))
    data_types_id = 10 # Incident Reports
    print('     [*] data type: {}'.format('Incident Reports'))
    format_types_id = 2 # CityProtect
    print('     [*] format type: {}'.format('CityProtect'))

    state = agency['state'] 
    print('     [*] state: {}'.format(state))

    # use lat and long to retrieve county fips from FCC.gov
    lat = agency['center']['coordinates'][1]
    lng = agency['center']['coordinates'][0]

    fcc = "https://geo.fcc.gov/api/census/area?lat={}&lon={}&format=json".format(lat, lng)
    print("     [!] Fetching County FIPS code from FCC.gov")
    response = requests.get(fcc)
    # print(response.text)
    json_resp = json.loads(response.text)

    fips = json_resp['results'][0]['county_fips']
    print("     [*] fips: {}".format(fips))

    if aggregation_level == 'municipal':
        print("     [!] Searching municipalities table for id")
        city_id = get_municipality(dolt, state, fips, agency['city'])
    else:
        city_id = None
    
    consolidator = 'CityProtect'
    print('     [*] consolidator: {}'.format(consolidator))
    update_freq = 'quarterly'
    print('     [*] update freq: {}'.format(update_freq))
    portal = 'CityProtect'
    print('     [*] portal type: {}'.format(portal))
    start = agency['reports'][0]['targetPeriodStart'] or None
    print('     [*] start date: {}'.format(start))

    # technically we could just omit these, but leaving them here in case this code
    # is reused elsewhere so they aren't forgotten
    scraper_path = None
    notes = None

    # then grab all our vars and turn into a dataframe:
    data = pd.DataFrame([{
        'url': url,
        'name': name,
        'aggregation_level': aggregation_level,
        'source_type_id': source_type_id,
        'data_types_id': data_types_id,
        'format_types_id': format_types_id,
        'state_iso': state,
        'county_fips': fips,
        'city_id' : city_id,
        'consolidator':consolidator,
        'update_frequency':update_freq,
        'portal_type': portal,
        'coverage_start': start,
        'scraper_path': scraper_path,
        'notes': notes
    }])
    print("   [*] Inserting data to datasets table...")
    id = uuid.uuid4()
    insert = dolt.sql("INSERT into datasets (`id`, `url`, `name`, `aggregation_level`, `source_type_id`, `data_types_id`, `format_types_id`, `state_iso`, `county_fips`, `city_id`, `consolidator`, `portal_type`, `coverage_start`, `scraper_path`, `notes`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(id, url, name, aggregation_level, source_type_id, data_types_id, format_types_id, state, fips, city_id, consolidator, portal, start, scraper_path, notes), result_format="csv")
    # and grab the record
    data = read_pandas_sql(dolt, "select * from datasets where id = '{}'".format(id))
    print(" [!] Inserted Dataset Record: ID #{}!".format(data.loc[0, 'id']))
    return data
    

'''
We use our dolt object, the dataset record passsed from either get_dataset() or new_dataset()
and the file. 

Due to limitations in dolt, we will have to load each line of the csv, add our dataset_id,
and then run a dolt.sql('INSERT ...') statement for each row so auto_inc works.

Alternatively, remove auto_inc and use guids so we can create them here, then we could
use their load_pandas methods or such
'''
def load_data(dolt, dataset_record, file):
    print('  [*] Enumerating records from {} for import'.format(file.name))

    # load the file into a dataframe
    df = pd.read_csv(file)
    # generate new UUID v4 IDs for each record, and push the column to the front
    df = pd.concat([pd.Series([uuid.uuid4() for _ in range(len(df.index))], index=df.index, name='id'), df], axis=1)
    # set the index to our new ID column
    df.set_index('id')
    # add the datasets_fk
    df['datasets_id']=dataset_record.loc[0, 'id']
    # format the date columns
    df['date'] = pd.to_datetime(df['date'])
    df['updateDate'] = pd.to_datetime(df['updateDate'])
    
    '''
    This currently does not work. It is supposed to be doltpy's method of taking a dataframe and enumerating itself


    # write to the database
    # on windows the path to the repo is C:\\Users\\you\\wherever\\this\\file\\is
    # it causes sql alchemy to freak
    # by creating a new dolt instance and stating the repo is just here in this dir, it allows it to work
    db = Dolt(repo_dir = 'datasets', print_output = False)
    # set our server config
    sc = ServerConfig(branch=Dolt.branch(dolt)[0].name, user='root')
    # create a sql server process
    print('    [*] Opening MySQL Connection to Dolt DB')
    with DoltSQLServerContext(db, server_config = sc) as dssc:
        print('    [*] Writing Data...')
        # write the data from the dataframe
        dssc.write_pandas(dolthub_incident_reports_table,
                            df,
                            create_if_not_exists=True,
                            primary_key=['id'],
                            commit=True)
    '''

    #instead, we will just loop our data
    for i, row in df.iterrows():
        print('    [-] Importing record: {}'.format(row['id']))
        insert = dolt.sql("INSERT into data_incident_reports (`id`, `ccn`, `incidentDate`, `updateDate`, `city`, `state`, `postalCode`, `blocksizedAddress`, `incidentType`, `parentIncidentType`, `narrative`, `datasets_id`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(row['id'], row['ccn'], row['date'], row['updateDate'], row['city'], row['state'], row['postalCode'], row['blocksizedAddress'], row['incidentType'], row['parentIncidentType'], row['narrative'], row['datasets_id']), result_format="csv")
    
    print('    [*] Done!')
''' push the changes to our custom branch '''
def commit(dolt):
    branch = Dolt.branch(dolt)[0].name
    print('  [*] Commiting changes to {}'.format(branch))
    # make sure we are in our custom branch and not a main one
    if 'city-protect' in branch:
        dolt.remote(name='origin', url=dolthub_fullrepo)
        dolt.add(['data_incident_reports', 'datasets'])
        dolt.commit('Data Added from cityprotect_load.py ETL Script')
        dolt.push('origin', branch, set_upstream='origin')
        print('  [*] Done!')
    else:
        print(  '[!] ERROR: Cannot push to main branch. Aborting. Use dolt cli to migrate and finalize commit')