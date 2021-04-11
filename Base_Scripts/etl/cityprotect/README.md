CityProtect ETL Process
===
NOTE: BEFORE RUNNING THE SCRIPT, `dolt login` SO IT HAS YOUR CREDENTIALS TO PUSH.

Data
====
Data for this script can be generated from the scraper located here: `\Base_Scripts\Scrapers\CityProtect_Bulk\cityprotect_fulldownload.py`


Script Overview
====
1. Grab the schema of our datasets table to ensure we have the latest information
2. Connect to CityProtect API and grab the agency data using the filename
3. Check the Agency Code against our datasets db, add if needed
    * Automatically fill in FIPS, municipality and fk
4. Format the dates as needed for DoltHub ingestion
5. Open a new branch and commit data

Output
====
If you run the script with the sample files (aka in its current state after cloning) this is the output:
```
 [*] Fetching agencies from https://ce-portal-service.commandcentral.com/api/v1.0/public/agencies
 [*] Agency List Fetched! 1091 agencies found
 [*] Cloning DoltHub Repo: pdap/datasets into ./datasets
   [*] Current Branch: data_types-sandbox
   [*] Creating new Branch: city-protect-import-py-d09b225d
   [*] Checking out new branch...
   [*] Current Branch: city-protect-import-py-d09b225d
--------------------------------------------------------
Found file in ./data: 47645-04.2017-07.2017.csv
 [*] Searching for agency #47645
 [!] Found Agency #47645 - Clanton Police Department  - Clanton,AL
 [*] Searching PDAP datasets for url: https://cityprotect.com/agency/540048e6-ee66-4a6f-88ae-0ceb93717e50
 [!] Found Existing Dataset Record: ID #57406970-99a3-11eb-ab25-8c8590d4a7fc!
  [*] Enumerating records from 47645-04.2017-07.2017.csv for import
    [-] Importing record: 59bab1af-0cdd-46d5-823d-d90fa3804933
    [-] Importing record: 85695836-4e01-4771-b5ba-f5638ec69bee
    [-] Importing record: 29d96e56-d226-4b01-8832-fb3c1ea62b77
    [-] Importing record: b041f9a6-c96d-4f81-8c3e-64b551c965bc
    [*] Done!
--------------------------------------------------------
Found file in ./data: 69025-01.2017-04.2017.csv
 [*] Searching for agency #69025
 [!] Found Agency #69025 - Jacksonville Police Department - Jacksonville,AL
 [*] Searching PDAP datasets for url: https://cityprotect.com/agency/54418486-8965-4ca4-90eb-52cc02214ef5
 [X] No Dataset Found! Proceeding to Add New Dataset...
   [*] Adding a New Dataset:
     [*] name: Jacksonville Police Department
     [*] url: https://cityprotect.com/agency/54418486-8965-4ca4-90eb-52cc02214ef5
     [*] aggregation level: municipal
     [*] source type: Third Party
     [*] data type: Incident Reports
     [*] format type: CityProtect
     [*] state: AL
     [!] Fetching County FIPS code from FCC.gov
     [*] fips: 01015
     [!] Searching municipalities table for id
     [!] Found Muncipality: ID #1840007433!
     [*] consolidator: CityProtect
     [*] update freq: quarterly
     [*] portal type: CityProtect
     [*] start date: 2017-01-01T00:00:00.000Z
   [*] Inserting data to datasets table...
 [!] Inserted Dataset Record: ID #625db196-4b81-471f-9a77-637dc6e98d60!
  [*] Enumerating records from 69025-01.2017-04.2017.csv for import
    [-] Importing record: dff6c870-1e8e-4414-a9ef-2bc2ed98527a
    [-] Importing record: ebe12011-7da0-4c88-b49e-2d4e718a9d94
    [-] Importing record: 42e95e78-adb5-4417-b966-30a6122bab6f
    [-] Importing record: b8fb4483-ba74-42da-952b-7ac3865cb81e
    [*] Done!
  [*] Commiting changes to city-protect-import-py-d09b225d
  [*] Done!
```

You can check out the data it actually imported [here](https://www.dolthub.com/repositories/pdap/datasets/query/city-protect-import-py-d09b225d?q=SELECT+*%0AFROM+%60data_incident_reports%60%0Awhere+datasets_id+%3D+%27625db196-4b81-471f-9a77-637dc6e98d60%27%0A%0A%0A%0A%0A%0A%0A&active=Tables)!