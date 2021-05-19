import os
from . import pdap_dolt

'''
    Main Logic for ETL from the schema files
    Returns a schema JSON object that will be modified in the ETL process and can be written back out to the calling file
'''
def schema_load(schema, branch, cwd):

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
        dataset = pdap_dolt.get_dataset_from_schema(dolt, data, agency)
        # 4 - Enumerate over the files in the mapped directory
        for datafile in os.scandir(os.path.join(cwd, "data")):
            print("--------------------------------------------------------")
            print("Found file in ./data: {}".format(datafile.name))
           
            # load the incident records in the database
            pdap_dolt.load_data(intake, dataset, datafile)
            # inc the index
            current_data_index += 1


    # 5 - Commit the Changes and Write out Schema.json!

    #pdap_dolt.commit(dolt)
    return schema