ETL Library
===

These modules are used for automating the connection and transformation to DoltHub

See `\Base_Scripts\etl\cityprotect\cityprotect_load.py` for usage of these scripts. 

CURRENT PROCEDURE
====
1. Call this library from a specific scraped agency dir, pass the schema.json file to it.
1. The library will locally clone the `pdap/datasets` and `pdap/data-intake` repos
1. Then it will verify the `agency_id` exists and will grab the appropriate record from the database
1. Next it will enumerate over the `data` items in the `schema.json`. It will create any datasets where the id is null, otherwise it will find an existing dataset and sync the data from the table with the `schema.json`. Whichever source has the most recent `last_modified` time will be the "Source of Truth" and that's the data that will be used to sync.
1. It will do the same for the `data`.`mapping` object, it will search for a table in `pdap/data-intake` with the exact name of the `data_type` and then sync the columns so they are there. If a new column is in the database but not the schema.json file, it will add the missing column with a `__skip__` value. 
1. Once everything has been synced, it will finally enumerate over the `mapping` object and insert the data into `pdap/data-intake`. Erroneous records are skipped a message displayed to the console.
1. The schema.json is overwritten in the directory with the synced changes from the database.


KNOWN LIMITATIONS & BUGS
====
* Will not auto create a missing agency
* Data from the scraped files is only inserted, it does not check if the data already exists
* only csv files are supported
* Does not auto commit (although it **can**, I have that off for now so the person manually reviews and commits)
* If the data_type is wrong or missing, it will kill the script
* Need to handle picking up an existing dolt / intake repo dirs (I just delete them and run the script fresh each time)
* Need to handle output on insert from Dolt (Must provide a value for result_format to get output back) (I don't really care about getting output back)