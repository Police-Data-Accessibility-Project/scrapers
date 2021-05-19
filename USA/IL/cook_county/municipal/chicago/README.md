This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate:
* [FOIA Request log - Police](https://data.cityofchicago.org/FOIA/FOIA-Request-Log-Police/wjkc-agnm): As needed
* [FOIA Request log - Police Board](https://data.cityofchicago.org/FOIA/FOIA-Request-Log-Chicago-Police-Board/9pd8-s9t4): As needed
* [FOIA Request log - Independent Police Review Authority (saved as IPRA)](https://data.cityofchicago.org/FOIA/FOIA-Request-Log-Independent-Police-Review-Authori/gzxp-vdqf): As needed
* [Crimes 2001-present](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2): Daily, has data excluding past 7 days
* [Police Sentiment Scores]: Monthly
* [COPA Cases Summary (Civilian Office of Police Accountability)](https://data.cityofchicago.org/Public-Safety/COPA-Cases-Summary/mft5-nfa8): Unsure
* [COPA Cases By Officer](https://data.cityofchicago.org/resource/ufxy-tgry.csv): Unsure
* [COPA Cases by Complainant or Subject](https://data.cityofchicago.org/Public-Safety/COPA-Cases-By-Complainant-or-Subject/vnz2-rmie): Unsure
* [Arrests](https://data.cityofchicago.org/Public-Safety/Arrests/dpt3-jri9): Daily
* [FOIA Request log - Chicago Public Library](https://data.cityofchicago.org/FOIA/FOIA-Request-Log-Chicago-Public-Library/n379-5uzu): As needed

### Archive:
* [IUCR Codes](https://data.cityofchicago.org/Public-Safety/Chicago-Police-Department-Illinois-Uniform-Crime-R/c7ck-438e)
* [Strategic Subject List - Historical](https://data.cityofchicago.org/Public-Safety/Strategic-Subject-List-Historical/4aki-r3np)



## Legal
https://www.chicago.gov/city/en/narr/foia/data_disclaimer.html

# Fields to collect:
* "ssl_score"
* "predictor_rat_age_at_latest_arrest"
* "predictor_rat_victim_shooting_incidents"
* "predictor_rat_victim_battery_or_assault"
* "predictor_rat_arrests_violent_offenses"
* "predictor_rat_gang_affiliation"
* "predictor_rat_narcotic_arrests"
* "predictor_rat_trend_in_criminal_activity"
* "predictor_rat_uuw_arrests"
* "sex_code_cd"
* "race_code_cd"
* "weapon_i"
* "drug_i"
* "age_group"
* "age_to"
* "stop_order_no"
* "parolee_i"
* "latest_date"
* "latest_dist"
* "majority_dist"
* "dlst"
* "latest_dist_res"
* "weapons_arr_cnt"
* "latest_weapon_arr_date"
* "narcotics_arr_cnt"
* "latest_narcotic_arr_date"
* "idoc_res_city"
* "idoc_res_state_code"
* "idoc_res_zip_code"
* "idoc_cpd_dist"
* "cpd_arrest_i"
* "domestic_arr_cnt"
* "latest_domestic_arr_date"
* "age_curr"
* "ssl_last_ptv_date"
* "trap_status"
* "raw_ssl_score"
* "heat_score"
* "raw_heat_score"
* "status_i"
* "pre_raw_heat_score"
* "trap_flags"
* "ssl_flags"
* "latitude"
* "longitude"
* "census_tract"
* "community_area"
* "location"

* "id"
* "case_number"
* "date"
* "block"
* "iucr"
* "primary_type"
* "description"
* "location_description"
* "arrest"
* "domestic"
* "beat"
* "district"
* "ward"
* "fbi_code"
* "x_coordinate"
* "y_coordinate"
* "year"
* "updated_on"
* "date_received"
* "request_number"
* "requestor_last_name"
* "requestor_first_name"
* "requestor_middle_initial"
* "institution"
* "brief_description_of_records_sought"
* "date_due"

* "requestor_name"
* "organization"
* "description_of_request"
* "due_date"

* "cb_no"
* "arrest_date"
* "race"
* "charge_1_statute"
* "charge_1_description"
* "charge_1_type"
* "charge_1_class"
* "charge_2_statute"
* "charge_2_description"
* "charge_2_type"
* "charge_2_class"
* "charge_3_statute"
* "charge_3_description"
* "charge_3_type"
* "charge_3_class"
* "charge_4_statute"
* "charge_4_description"
* "charge_4_type"
* "charge_4_class"
* "charges_statute"
* "charges_description"
* "charges_type"
* "charges_class"


## Fields unobtainable within our legal guidelines:

## Fields not available:

## Fields being collected:

## Fields available not present on the list above:

## Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.
