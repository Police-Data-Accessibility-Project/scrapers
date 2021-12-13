This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
[Calls for service](https://data.cityofberkeley.info/Public-Safety/Berkeley-PD-Calls-for-Service/k2nh-s5h5): Unsure, maybe every 180 days at the beginning of the week
[Arrests](https://data.cityofberkeley.info/Public-Safety/Berkeley-PD-Log-Arrests/xi7q-nji6): Seems to be daily, has previous day's data. "Daily (Monday through Friday, excluding holidays) at 9:00 am"
[Jail Bookings](https://data.cityofberkeley.info/Public-Safety/Berkeley-PD-Log-Jail-Bookings/7ykt-c32j): Seems to be daily, has previous day's data.
[Stop Data (Jan 26, 2015 to Sep 30, 2020)](https://data.cityofberkeley.info/Public-Safety/Berkeley-PD-Stop-Data-Jan-26-2015-to-Sep-30-2020-/4tbf-3yt8): Should be never, but it was updated a few days ago (05/07/2021). Weekly on fridays (scrape saturday)
[Stop Data ((October 1, 2020 - Present))](https://data.cityofberkeley.info/Public-Safety/Berkeley-PD-Stop-Data-October-1-2020-Present-/ysvs-bcge): Unsure, last updated `April 15, 2021`


## Legal
https://www.cityofberkeley.info/IT/CoBWEB_Legal_Notice.aspx

# Fields to collect:
_Move these fields to the appropriate list below when you submit your scraper._
* "year"
* "murder_and_manslaughter"
* "rape"
* "robbery"
* "aggravated_assault"
* "burglary"
* "larceny_theft"
* "motor_vehicle_theft"
* "total"

* "arrest_number"
* "date_and_time"
* "arrest_type"
* "subject"
* "race"
* "sex"
* "date_of_birth"
* "age"
* "height"
* "weight"
* "hair"
* "eyes"
* "statute"
* "statute_type"
* "statute_description"
* "case_number"

* "caseno"
* "offense"
* "eventdt"
* "eventtm"
* "cvlegend"
* "cvdow"
* "indbdate"
* "block_location"
* "blkaddr"
* "city"
* "state"

* "booking_number"
* "booking_date_and_time"
* "occupation"
* "arrest_date_and_time"
* "case_number"
* "booking_agency"
* "disposition"

* "lea_record_id"
* "person_number"
* "date_of_stop"
* "time_of_stop"
* "duration_of_stop"
* "is_stop_made_in_response"
* "type_of_stop"
* "officer_type_of_assignment"
* "location"
* "is_location_a_k12_public"
* "if_k12_school_is_stop_of"
* "school_name"
* "education_code_section"
* "education_code_subdivision"
* "raceperceivedpriortostop"
* "perceived_race_or_ethnicity"
* "perceived_gender"
* "perceived_gender_nonconforming"
* "is_lgbt"
* "perceived_age"
* "person_had_limited_or_no"
* "perceived_or_known_disability"
* "city_of_residence"
* "reason_for_stop"
* "reason_for_stop_narrative"
* "traffic_violation_type"
* "traffic_violation_offense"
* "suspicion_offense_code"
* "suspicion_subtype"
* "actions_taken"
* "basis_for_search"
* "basis_for_search_narrative"
* "basis_for_property_seizure"
* "type_of_property_seized"
* "contraband_or_evidence"
* "other_contraband_desc"
* "warning_offense_codes"
* "citation_offense_codes"
* "result_of_stop"
* "in_field_cite_and_release"
* "custodial_arrest_

* "createdatetime"
* "incidentnumber"
* "address"
* "lat"
* "lon"
* "calltype"
* "gender"
* "reason"
* "enforcement"
* "car_search"



## Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.
