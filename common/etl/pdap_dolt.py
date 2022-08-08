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
import datetime
import traceback


# TURN OFF ONCE data_types-sandbox IS MERGED INTO MASTER
dev_mode = False

dolthub_org = 'pdap'

dolthub_repo = 'data_sources'
dolthub_fullrepo = dolthub_org + '/' + dolthub_repo
dolthub_table = 'data_sources'
dolthub_branch = 'master'

intake_repo = 'data-intake'
intake_fullrepo = dolthub_org + '/' + intake_repo
intake_table = 'incident_reports'
intake_branch = 'master'

dolt = None # dolt data_sources repo
intake = None # dolt intake repo


# init our dolt repo, we can pass a custom branch or it will fall back to master
def init(branch=dolthub_branch, intake_branch=intake_branch):
    # check if repo already exists in our cwd
    cwd = os.getcwd()
    path = os.path.join(cwd, dolthub_repo)
    if os.path.isdir(path):
        print(' [*] DoltHub Repo found in ./{}, re-initializing'.format(dolthub_repo))
        dolt = Dolt(path)
        intake = Dolt(os.path.join(cwd, intake_repo))
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
        Dolt.pull(intake)
        s = Dolt.status(dolt)
        s2 = Dolt.status(intake)

        print('   [*] Current Status: data_sources: {} / intake: {}'.format(s, intake))
    else:
        # clone the database from DoltHub, save it into a var to be referenced for read/write purposes
        print(' [*] Cloning Data Sources Repo: {} into ./{}'.format(dolthub_fullrepo, dolthub_repo))
        dolt = Dolt.clone(dolthub_fullrepo, branch=branch)
        print(' [*] Cloning Intake Repo: {} into ./{}'.format(intake_fullrepo, intake_repo))
        intake = Dolt.clone(intake_fullrepo, branch=intake_branch)
        print('   [*] Current Branch: data_sources: {} / intake:'.format(Dolt.branch(dolt)[0].name,Dolt.branch(intake)[0].name))
    return dolt, intake

'''
    Search the [pdap/data_sources].[data_sources] database for the specified URL
    If it does not exist, pass agency info to new func to create it
'''
def get_data_source(dolt, data_source_url, agency):
    # data = read_pandas_sql(dolt, "SELECT * FROM data_sources WHERE url = 'https://cityprotect.com/agency/540048e6-ee66-4a6f-88ae-0ceb93717e50'")
    data = read_pandas_sql(dolt, "SELECT * FROM data_sources WHERE url = '{}'".format(data_source_url))
    # check if a result was passed
    if data.shape[0] == 0:
        print(" [X] No Data Source Found! Proceeding to Add New Data Source...")
        return new_data_source(dolt, agency, data_source_url)
    if data.shape[0] == 1:
        print(" [!] Found Existing Data Source Record: ID #{}!".format(data.loc[0, 'id']))
        return data

'''
    Search the [pdap/data_sources].[data_sources] database for the specified URL
    If it does not exist, pass agency info to new func to create it

    This method will verify the data from dolt exactly matches the data in the schema.json
'''
def get_data_source_from_schema(dolt, schema_data_source, agency, full_schema, idx):
    # method 1: check if id is set first
    if schema_data_source['data_source_id']:
        dolt_data = read_pandas_sql(dolt, "SELECT * FROM data_sources WHERE id = '{}'".format(schema_data_source['data_source_id']))
    # else grab the url and check via that
    else:
        dolt_data = read_pandas_sql(dolt, "SELECT * FROM data_sources WHERE url = '{}'".format(schema_data_source['url']))
    # check if a result was passed

    # if not, make one
    if dolt_data.shape[0] == 0:
        print(" [X] No Data Source Found! Proceeding to Add New Data Source...")
        return new_data_source_from_schema(dolt, agency, schema_data_source, full_schema, idx)
    # if so, compare the db data to the schema.json and consolidate
    if dolt_data.shape[0] == 1:
        print(" [!] Found Existing Data Source Record: ID #{}!".format(dolt_data.loc[0, 'id']))
        # compare the changes from the db to the schema.json to consolidate before returning
        return merge_data_source_info(full_schema, dolt_data, idx)


''' merge the data from the db back into the schema '''
def merge_data_source_info(schema, data_source, index):
    # compare the last_modified time of the json vs the

    # merge the data back into the schema
    schema['data'][index]['data_source_id']     = data_source.loc[0, 'id']
    schema['data'][index]['source_type']    = data_source.loc[0, 'source_type_id']
    schema['data'][index]['data_type']      = data_source.loc[0, 'data_type_id']
    schema['data'][index]['format_type']    = data_source.loc[0, 'format_type_id']
    schema['data'][index]['update_freq']    = data_source.loc[0, 'update_frequency']

    return schema, data_source

'''
    used if agency_id is filled out in the schema
    RETURN: the uuid of the data_source or ''
'''
def get_agency_by_uuid(dolt, uuid):
    try:
        data = read_pandas_sql(dolt, "SELECT * FROM agencies where id =  '{}'".format(uuid))
        # check if a result was passed
        if data.shape[0] == 0:
            print("       [X] No Agency Found!")
            return ''
        if data.shape[0] == 1:
            print("       [!] Found Agency ID #{}!".format(data.loc[0, 'id']))
            return data.loc[0, 'id']
    except:
        print("       [X] Error Fetching Agency")
        return ''

''' fallback if the agency_id is blank'''
def get_agency_id(dolt, name, state):
    try:
        data = read_pandas_sql(dolt, "SELECT * FROM 'agencies' where soundex('name') = soundex('{}') and state_iso = '{}'".format(name.strip(), state.strip()))
        # check if a result was passed
        if data.shape[0] == 0:
            print("       [X] No Agency Found!")
            return ''
        if data.shape[0] == 1:
            print("       [!] Found Agency ID #{}!".format(data.loc[0, 'id']))
            return data.loc[0, 'id']
    except:
        print("       [X] Error Fetching Agency")
        return ''

# before we actually start making changes, we should make a new branch
def new_branch(dolt, intake):
    # generates a modifier at the end
    # etl-import-py-5d365f9b
    new_branch = 'etl-import-py-{}'.format(str(uuid.uuid4()).split('-')[0])
    try:
        print('   [*] Creating new Branch: {}'.format(new_branch))
        b = Dolt.branch(dolt, branch_name=dolthub_branch, new_branch=new_branch, copy=True)
        b2 = Dolt.branch(intake, branch_name=intake_branch, new_branch=new_branch, copy=True)
        #print(b)
        Dolt.checkout(dolt, branch=new_branch)
        Dolt.checkout(intake, branch=new_branch)
        print('   [*] Checking out new branch...')
        # recheck the branch
        b = Dolt.branch(dolt)[0].name
        b2 = Dolt.branch(intake)[0].name
        print('   [*] Current Branch: {} / {}'.format(b, b2))
    except:
        print('   [!] FATAL ERROR: CANNOT CHECKOUT NEW BRANCH. ABORTING')
        sys.exit()

'''

This was legacy used for cityprotect data and will most likely be deprecated

'''
def new_data_source(dolt, agency, url):
    print('   [*] Adding a New Data Source:')
    name = agency['name'].replace("'", '')
    print('     [*] name: {}'.format(name))
    print('     [*] url: {}'.format(url))
    status_id = 5
    print('     [*] status: {}'.format('5 - Initial Data Loaded'))

    source_type_id = 3 # Third Party
    print('     [*] source type: {}'.format('Third Party'))
    data_types_id = 10 # Incident Reports
    print('     [*] data type: {}'.format('Incident Reports'))
    format_types_id = 2 # CityProtect
    print('     [*] format type: {}'.format('CityProtect'))

    # try to use soundex to find the agency ID. will not always work
    agency_id = get_agency_id(dolt, name, agency['state'])
    print('     [*] agency id: {}'.format(agency_id))

    '''
    fcc = "https://geo.fcc.gov/api/census/area?lat={}&lon={}&format=json".format(lat, lng)
    print("     [!] Fetching County FIPS code from FCC.gov")
    response = requests.get(fcc)
    # print(response.text)
    json_resp = json.loads(response.text)


    fips = json_resp['results'][0]['county_fips']
    print("     [*] fips: {}".format(fips))
    '''
    update_freq = 3 # quarterly
    print('     [*] update freq: {}'.format(update_freq))
    portal = 'CityProtect'
    print('     [*] portal type: {}'.format(portal))
    start = agency['reports'][0]['targetPeriodStart'] or None
    print('     [*] start date: {}'.format(start))

    # technically we could just omit these, but leaving them here in case this code
    # is reused elsewhere so they aren't forgotten
    scraper_id = ''
    notes = ''

    # then grab all our vars and turn into a dataframe:
    data = pd.DataFrame([{
        'url': url,
        'status_id': status_id,
        'name': name,
        'source_type_id': source_type_id,
        'data_types_id': data_types_id,
        'format_types_id': format_types_id,
        'agency_id': agency_id,
        'update_frequency':update_freq,
        'portal_type': portal,
        'coverage_start': start,
        'scraper_id': scraper_id,
        'notes': notes
    }])
    print("   [*] Inserting data to Data Sources table...")

    id = str(uuid.uuid4()).replace('-','') # UUID without dashes
    insert = dolt.sql("INSERT into data_sources ('id', 'url', 'status_id', 'name', 'source_type_id', 'data_types_id', 'format_types_id', 'agency_id', 'update_frequency', 'portal_type', 'coverage_start', 'scraper_id', 'notes') VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(id, url, status_id, name, source_type_id, data_types_id, format_types_id,  agency_id, update_freq, portal, start, scraper_id, notes), result_format="csv")

    # and grab the record
    data = read_pandas_sql(dolt, "select * from data_sources where id = '{}'".format(id))
    print(" [!] Inserted Data Source Record: ID #{}!".format(data.loc[0, 'id']))
    return data

''' load the data from the schema '''
def new_data_source_from_schema(dolt, agency, schema_data_source, full_schema, idx):
    print('   [*] Adding a New Data Source:')
    url = schema_data_source['url']
    print('     [*] url: {}'.format(url))
    status_id = 5
    print('     [*] status: {}'.format('5 - Initial Data Loaded'))

    # agencies method: get_agency_by_uuid
    agency_id = agency
    print('     [*] agency_id: {}'.format(agency_id))

    source_type_id = schema_data_source['source_type'] # Third Party
    print('     [*] source type: {}'.format(source_type_id))
    data_types_id = schema_data_source['data_type'] # Incident Reports
    print('     [*] data type: {}'.format(data_types_id))
    format_types_id = schema_data_source['format_type'] # CityProtect
    print('     [*] format type: {}'.format(format_types_id))


    '''
    fcc = "https://geo.fcc.gov/api/census/area?lat={}&lon={}&format=json".format(lat, lng)
    print("     [!] Fetching County FIPS code from FCC.gov")
    response = requests.get(fcc)
    # print(response.text)
    json_resp = json.loads(response.text)


    fips = json_resp['results'][0]['county_fips']
    print("     [*] fips: {}".format(fips))
    '''
    update_freq = schema_data_source['update_freq'] # quarterly
    print('     [*] update freq: {}'.format(update_freq))


    # technically we could just omit these, but leaving them here in case this code
    # is reused elsewhere so they aren't forgotten
    scraper_id = ''
    notes = ''

    # then grab all our vars and turn into a dataframe:
    data = pd.DataFrame([{
        'url': url,
        'status_id': status_id,
        'source_type_id': source_type_id,
        'data_types_id': data_types_id,
        'format_types_id': format_types_id,
        'agency_id': agency_id,
        'update_frequency':update_freq,
        'scraper_id': scraper_id,
        'notes': notes
    }])
    print("   [*] Inserting data to Data Sources table...")

    id = str(uuid.uuid4()).replace('-','') # UUID without dashes
    insert = dolt.sql("INSERT INTO data_sources (id, url, status_id, source_type_id, data_types_id, format_types_id, agency_id, update_frequency, scraper_id, notes) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(id, url, status_id, source_type_id, data_types_id, format_types_id,  agency_id, update_freq, scraper_id, notes), result_format="csv")

    # and grab the record
    data = read_pandas_sql(dolt, "select * from data_sources where id = '{}'".format(id))
    print(" [!] Inserted Data Source Record: ID #{}!".format(data.loc[0, 'id']))
    # update the schema file with the lastest info
    # since everything was used from the file to create, only the id and last_modified
    # will change
    full_schema['data'][idx]['data_source_id'] = data.loc[0, 'id']
    full_schema['data'][idx]['last_modified'] = data.loc[0, 'last_modified']

    # return back
    return full_schema, data


'''
We use our dolt object, the Data Source record passsed from either get_data_source() or new_data_source()
and the file.

Due to limitations in dolt, we will have to load each line of the csv, add our data_source_id,
and then run a dolt.sql('INSERT ...') statement for each row so auto_inc works.

Alternatively, remove auto_inc and use guids so we can create them here, then we could
use their load_pandas methods or such
'''
def load_data(intake, data_source_record, file):
    print('  [*] Enumerating records from {} for import'.format(file.name))

    # load the file into a dataframe
    df = pd.read_csv(file)
    # generate new UUID v4 IDs (with no dashes) for each record, and push the column to the front

    df = pd.concat([pd.Series([str(uuid.uuid4()).replace('-','') for _ in range(len(df.index))], index=df.index, name='id'), df], axis=1)
    # set the index to our new ID column
    df.set_index('id')
    # add the data_sources_fk
    df['data_sources_id']=data_source_record.loc[0, 'id']
    # format the date columns
    df['date'] = pd.to_datetime(df['date'], errors='coerce', format='%m/%d/%Y, %I:%M:%S %p')
    df['updateDate'] = pd.to_datetime(df['updateDate'], errors='coerce', format='%m/%d/%Y, %I:%M:%S %p')

    '''
    This currently does not work. It is supposed to be doltpy's method of taking a dataframe and enumerating itself


    # write to the database
    # on windows the path to the repo is C:\\Users\\you\\wherever\\this\\file\\is
    # it causes sql alchemy to freak
    # by creating a new dolt instance and stating the repo is just here in this dir, it allows it to work
    db = Dolt(repo_dir = 'data_sources', print_output = False)
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
    try:
        for i, row in df.iterrows():
            print('    [-] Importing record: {} - ccn:'.format(row['id'], row['ccn']))
            # sometimes may get a glitch like an invalid date
            try:
                insert = intake.sql("INSERT into incident_reports ('id', 'ccn', 'incidentDate', 'updateDate', 'city', 'state', 'postalCode', 'blocksizedAddress', 'incidentType', 'parentIncidentType', 'narrative', 'data_sources_id') VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(row['id'], row['ccn'], row['date'], row['updateDate'], row['city'], row['state'], row['postalCode'], row['blocksizedAddress'], row['incidentType'], row['parentIncidentType'], row['narrative'], row['data_sources_id']))
            except:
                print('      [!] Error importing record: {} - ccn:'.format(row['id'], row['ccn']))
        print('    [*] Done!')
    except:
        print('    [!] Error Iterating over rows! Skipping file {}'.format(file.name))

'''
    This function will ensure ALL of the columns in the DB are represented,
    so if new columns are added to the schema, this function will also load them
    back to the schema as "__unmapped__" in case the data source does have a column
    that could map to it

    Args:
    dolt - the dolt [pdap/data_sources] instance
    intake - the dolt [pdap/data-intake] instance
    schema - the full schema.json file loaded in memory
    data_source_record - a Pandas DataFrame of the particular record in [pdap/data_sources].data_sources
    idx - the current index of the schema['data'] that we are on
'''
def merge_data_source_mapping(dolt, intake, schema, data_source_record, idx):

    data = read_pandas_sql(dolt, "SELECT * FROM data_types where id =  '{}'".format(data_source_record.loc[0, 'data_types_id']))
    # if a result does not exist then fail the script, we must have a proper data_type
    # and at this point we cannot accurately derive one
    if data.shape[0] == 0:
        print("    [CRITICAL] No Data Type Found! Please fix the mapping in the schema.json file!")
        sys.exit() # exit the script

    # we have a result, let's do stuff with it
    if data.shape[0] == 1:
        intake_table_name = data.loc[0, 'name']
        print('    [*] Fetching columns for {} data type'.format(intake_table_name))
        cols = read_pandas_sql(intake, "DESCRIBE {}".format(intake_table_name))
        # no data ? uh oh
        # this should never happen but just in case
        if cols.shape[0] == 0:
            print("    [CRITICAL] No Columns found for table {} in pdap/data-intake! Cannot complete mapping!")
            sys.exit() # exit the script
        # else we have data, let's iterate
        else:
            print('      [*] Loaded mapping: {}'.format(schema['data'][idx]['mapping']))
            #  iterate over all the rows
            for i, row in cols.iterrows():
                # the cols are Field, type, Null, Key, Default, Extra.
                # for us, the field, type & Null are the most important
                field_name = row[0]
                field_type = row[1]
                field_allow_null = row[2]

                # with the above data, we need to compare it to the mapping

                # this is the actual column in the "mapping" object of our current data_source in the schema.json
                # we will need to test to see if it exists first
                if field_name in schema['data'][idx]['mapping']:
                    print('      [*] Found column {} for Data Source in schema.json'.format(field_name))
                else:
                    print('      [x] Missing column {} for Data Source in schema.json, adding...'.format(field_name))
                    # figure out what to set the missing column to
                    if field_name in ['id']:
                        schema['data'][idx]['mapping'][field_name] = "__uuid__"
                    elif field_name in ['date_insert', 'date_update']:
                        schema['data'][idx]['mapping'][field_name] = "__date__"
                    elif field_name == data_sources_id':
                        schema['data'][idx]['mapping'][field_name] = "__data_source_id__"
                    else:
                        schema['data'][idx]['mapping'][field_name] = "__skip__"

    # grab our freshly merged mapping
    intake_db_cols = schema['data'][idx]['mapping']
    # return the full schema back out with the intake cols and table name
    return schema, intake_db_cols, intake_table_name


'''
    Enumerate over the data mapping in order to sync the cols in the database to the data scraped

    Args:
    intake - the dolt [pdap/data-intake] instance
    intake_db_cols - a JSON object - columns from merge_data_source_mapping so we know how to map
    intake_table_name - name of the table the data will be loaded into
    data_source_record - a Pandas DataFrame of the particular record in [pdap/data_sources].data_sources
    file - the csv file path
'''
def load_csv_data_from_schema_map(intake, intake_db_cols, intake_table_name, data_source_record, file):

    print('  [*] Enumerating records from {} for import'.format(file.name))

    # load the file into a dataframe
    df = pd.read_csv(file)
    df = df.where(df.notna(), None) # replace all nan with None

    # dynamically build the insert statement
    # https://stackoverflow.com/questions/51975479/parsing-json-into-insert-statements-with-python


    try:
        # first loop through each record in the flatfile
        for i, row in df.iterrows():
            # for each record, we need to look up the intake mapping to map properly
            keylist = "("
            valuelist = "("
            firstPair = True # first index no , before it
            # key - Dolt db column name
            # value - scraped file column name / dataframe col name
            for key, value in intake_db_cols.items():
                if not firstPair:
                    keylist += ", "
                    valuelist += ", "
                firstPair = False
                keylist += key

                # generate any UUIDs
                if value == '__uuid__':
                    valuelist +=  "'" + str(uuid.uuid4()).replace('-','') + "'"
                # generate any dates
                elif value == '__date__':
                    valuelist +=  "CAST('"+ str(datetime.datetime.now()) + "' as datetime)"
                # fill in the data_source id
                elif value == '__data_source_id__':
                    valuelist +=  "'" + str(data_source_record.loc[0, 'id']) + "'"
                # NULL out any skips
                elif value == '__skip__':
                    valuelist += 'NULL'
                # else find the column in the dataframe
                else:
                    if row[value] in (None, 'null'):
                        valuelist += 'NULL'
                    else:
                        valuelist += "'" + str(row[value]) + "'"
            keylist += ")"
            valuelist += ")"

            sqlstatement = "INSERT INTO " + intake_table_name + " " + keylist + " VALUES " + valuelist



            #print('    [-] Importing record: {}'.format(sqlstatement))
            print('    [-] Importing record')
            # sometimes may get a glitch like an invalid date
            try:
                insert = intake.sql(sqlstatement)
            except:
                print('      [!] Error importing record: {}'.format(traceback.print_exc()))
        print('    [*] Done!')
    except:
        print('    [!] Error Iterating over rows! Skipping file {}. Error: {}'.format(file.name, traceback.print_exc()))

    # first loop through the mapping to grab the dolt col (key) and the flat file key (value)



    #instead, we will just loop our data




''' push the changes to our custom branch '''
def commit(dolt, intake):
    branch = Dolt.branch(dolt)[0].name
    intake_branch = branch = Dolt.branch(intake)[0].name
    print('  [*] Commiting changes to {}'.format(branch))
    # make sure we are in our custom branch and not a main one
    if 'etl-import' in branch and 'etl-import' in intake_branch :
        dolt.remote(add=True, name='origin', url=dolthub_fullrepo)
        dolt.commit('Data Added from ETL Script')
        dolt.push('origin', branch, set_upstream='origin')

        intake.remote(add=True, name='origin', url=intake_fullrepo)
        intake.commit('Data Added from ETL Script')
        intake.push('origin', intake_branch, set_upstream='origin')
        print('  [*] Done!')
    else:
        print(  '[!] ERROR: Cannot push to main branch. Aborting. Use dolt cli to migrate and finalize commit')
