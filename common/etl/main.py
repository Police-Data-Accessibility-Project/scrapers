import os
from . import pdap_dolt

'''
    Main Logic for ETL from the schema files
    Returns a schema JSON object that will be modified in the ETL process and can be written back out to the calling file
'''
def schema_load(schema, branch = 'master'):

    # 1 - Init our repo from an existing branch, and then clone it for the changes we are about to make
    dolt, intake = pdap_dolt.init(branch)
    pdap_dolt.new_branch(dolt, intake)

    # 2 - Grab agency info from the schema
    if schema['agency_id']:
        print(" [*] Searching for agency via uuid {}".format(schema['agency_id']))
        agency = pdap_dolt.get_agency_by_uuid(dolt, schema['agency_id'])
    else:
        print(" [*] Searching for agency via name {}".format(schema['agency_info']['name']))
        agency = pdap_dolt.get_agency_id(dolt, schema['agency_info']['name'], schema['agency_info']['state'])

    # 3 - Loop through the available datasets in the the "data" object
    # This will contain the available data types / files / directories.etc
    current_data_index = 0 
    for data in schema['data']:
        print(" [*] Searching PDAP datasets for url: {}".format(data['url']))
        # grab the dataset (or create one) and then sync the schema.json and datasets data
        schema, dataset = pdap_dolt.get_dataset_from_schema(dolt, data, agency, schema, current_data_index)

        # 3a Sync the schema mapping obj with the db columns to verify a match
        # returns the fixed schema file, and the dataframe of cols for the table
        # the latter will be used to actually do the import (and prevent another call)
        print('  [*] Syncing schema.json mapping with database columns...')
        schema, intake_db_cols, intake_table_name = pdap_dolt.merge_dataset_mapping(dolt, intake, schema, dataset, current_data_index)

        # inc the index in case the loop resets
        current_data_index += 1
        # 4 - Enumerate over the files in the mapped directory
        data_dir = os.path.join(os.getcwd(), data['full_data_location'])
        print(" [*] Searching for files in {}".format(data_dir))
        for datafile in os.scandir(data_dir):
            print("--------------------------------------------------------")
            print("Found file in ./{}: {}".format(data['full_data_location'], datafile.name))
            
            
            # 4a load the incident records in the database
            pdap_dolt.load_csv_data_from_schema_map(intake, intake_db_cols, intake_table_name, dataset, datafile)


    # 5 - Commit the Changes to Dolt
    # pdap_dolt.commit(dolt)

    # 6- Write out Schema.json!
    return schema