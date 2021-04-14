Schema.json Guide
===

The `schema.json` is an overview of the data scraped, the dataset itself, and the table it will import to. It will be utilized in an automated ETL process.

This guide shows you how to fill out the schema.json for use:
* **dataset_id**: The ID from our list of datasets found [here](https://www.dolthub.com/repositories/pdap/datasets/data/master/datasets). If this is a new dataset not yet in our table, leave this blank and the ETL script will use the data below to add a record and automatically add the ID to the schema.json file.
* **dataset_information**: This provides more information about the dataset. If the ID is listed above and you change any information here, it will be automatically updated if the script is ran again.
    * **`agency_name`**: name of the agency such as 'Gaston County Sheriff'
    * **`agency_coords`**: this will probably require you to search up on Google Maps. This is actually very important to ensure we pull the correct FIPS and municipal codes. Search the agency on google maps, and right click on the pin to grab the lat and long coordinates. It is okay if there are multiple districts, just grab the main district if so.
    * **`url`**: the url of the dataset used
    * **`aggregation`**: this is how the data is aggregated. use `federal`, `state`, `county`, `muncipal` or `university`
    * **`state`**: two-letter state code ('IN', 'CA')
    * **`county`**: county name in Title case (first letter capitalized: 'Marion', 'Bristol Bay') (leave blank if a state agency)
    * **`city`**: city of the agency (leave blank if a county or state agency)
* **source_type**: use one of the values in the `id` column found in the source_types table [here] (https://www.dolthub.com/repositories/pdap/datasets/data/master/source_types)
* **data_type**: use one of the values in the `id` column found in the data_types table [here](https://www.dolthub.com/repositories/pdap/datasets/data/master/data_types) (such as `10` for `incident_reports` data)
* **format_type**: use one of the values in the `id` column found in the format_types table [here](https://www.dolthub.com/repositories/pdap/datasets/data/master/format_types) (such as `2` for `cityprotect` data)
* **full_data_location**: the location of all the data from the scraper. It will most likely just be in the `/data` directory in the same folder after the scraper has ran
* **mapping**: based off of your `data_type`, the data will be stored in a different table with different columns. This section is how your data maps to the columns in the database such as for `"table_col": "data_col"`


## Example
In this example, we only have one set of data from Clanton Police Department, Incident Reports. 
If we end up getting more data form this agency (such as arrest records or booking reports), then we would put it in a *separate* directory such as `/booking_data` and add the information in the `data` dictionary of the new folder and it's contents

```
{
    "dataset_id": "5740697099a311ebab258c8590d4a7fc",
    "dataset_info":{
        "agency_name":"Clanton Police Department",
        "agency_coords":{"lat": "32.83853", "long":"-86.62936"},
        "url":"https://cityprotect.com/agency/540048e6ee664a6f88ae0ceb93717e50",
        "aggregation":"municipal",
        "state": "AL",
        "county":"Chilton"
    },
    "data": [
        {
            "full_data_location":"/data",
            "source_type": 3,
            "data_type": 10,
            "format_type": 2,
            "mapping":[
                "ccn":"ccn",
                "incidentDate": "date",
                ...
            ]
        }
    ]
}
```

