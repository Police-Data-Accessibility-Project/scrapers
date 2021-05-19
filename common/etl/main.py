
import pdap_dolt
import os

'''
    Main Logic for ETL from the schema files
    Returns a schema JSON object that will be modified in the ETL process and can be written back out to the calling file
'''
def schema_load(schema, branch, cwd):

    # 1 - Init our repo from an existing branch, and then clone it for the changes we are about to make
    dolt, intake = pdap_dolt.init(branch)
    pdap_dolt.new_branch(dolt, intake)

    # 2 - Grab agency info from the schema
    if dataset_id:
        print(" [*] Searching for agency via uuid {}".format(agency_id))
        agency = pdap_dolt.get_agency_by_uuid(agency_id)
    else:
        print(" [*] Searching for agency via name {}".format(agency_info.name))
        agency = pdap_dolt.get_agency_by_name(agency_info.name)

    # 3 - Loop through the available datasets in the the "data" object
    # This will contain the available data types / files / directories.etc
    for data in schema.data:
        dataset = pdap_dolt.get_dataset(dolt, dataset_url, agency)
        # 4 - Enumerate over the files in the mapped directory
        for datafile in os.scandir(os.path.join(cwd, "data")):
            print("--------------------------------------------------------")
            print("Found file in ./data: {}".format(datafile.name))
            # files are formatted as crapiId-start.date-end.date.csv; split into vars
            crapiID, start_date, end_date = datafile.name.split("-")
            # pass the crapiId to this function to loop through the list of agenices and retrieve just the agency for this file
            print(" [*] Searching for agency #{}".format(crapiID))
            agency = cityprotect.get_agency_by_crapiId(agencies, crapiID)
            # if the agency is already in our datasets table, it will be in this format
            dataset_url = "https://cityprotect.com/agency/{}".format(agency["agencyPathName"])

            # get the dataset (or create and get if it doesn't exist) and retrieve the record
            print(" [*] Searching PDAP datasets for url: {}".format(dataset_url))
            dataset = pdap_dolt.get_dataset(dolt, dataset_url, agency)

            # this is the id of the dataset, which will be used as the fk for the incidents table
            # incidents_fk = dataset.loc[0, 'id']

            # load the incident records in the database
            pdap_dolt.load_data(intake, dataset, datafile)


    # 5 - Commit the Changes and Write out Schema.json!

    #pdap_dolt.commit(dolt)
    return schema