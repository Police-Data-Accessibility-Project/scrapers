This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
[Calls for Service](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Police-Calls-for-Servic/gexm-h6bt): Daily
[Crime Incidents](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Crime-Incidents/k59e-2pvf): Daily
[Use of Force](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Use-of-Force/8us8-wi2w): Daily (may not be daily, "*This information will not be updated while the Cincinnati Police Department undergoes transfer to a new data management system.*")
[Assaults on Officers](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Assaults-on-Officers/bmmy-avxm): Daily, (may not be daily, see Use of Force)
[Shootings (non-officer involved)](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-CPD-Shootings/7a3r-kxji): Daily
[Officer Involved Shootings](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Officer-Involved-Shooti/r6q4-muts): Daily
[Traffic Stops (Drivers)](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Traffic-Stops-Drivers-/hibq-hbnj): Daily
[Traffic Stops (All subjects)](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Traffic-Stops-All-Subje/ktgf-4sjh): Daily
[Ped Stops](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Pedestrian-Stops/jx3x-rh6i): Daily
[Citizen Complaint Authority Closed Complaints](https://data.cincinnati-oh.gov/Safety/Citizen-Complaint-Authority-CCA-Closed-Complaints/ii65-eyg6): Daily


## Legal
Include the Terms of Service (or link to them). Is there anything else we should know?

# Fields to collect:
* "address_x"
* "incident_no"
* "district"
* "latitude_x"
* "longitude_x"
* "date_reported"
* "subject"
* "crime_type"
* "premise_type"
* "beat"
* "day_of_week"
* "weapon"
* "victim_type"
* "victim_race"
* "victim_gender"
* "sna_neighborhood"
* "cpd_neighborhood"
* "community_council_neighborhood"

* "agency"
* "create_time_incident"
* "disposition_text"
* "event_number"
* "incident_type_id"
* "incident_type_desc"
* "priority"
* "priority_color"
* "arrival_time_primary_unit"
* "closed_time_incident"
* "dispatch_time_primary_unit"
* "community_council_neighborhood"
* "cpd_neighborhood"

* "city"
* "disposition_1_text"
* "incident_type_description"
* "neighborhood"
* "area_id"
* "call_source_text"
* "priority"

* "addendum"
* "complainant_age_range"
* "allegation_code"
* "allegation_description"
* "body_camera_worn"
* "case_severity_category"
* "sna_preferred_name"
* "unique_case_number"
* "complainant_charged"
* "citizen_id"
* "board_review_date"
* "city_manager_review_date"
* "case_completion_date"
* "incident_date_time"
* "cca_recieved_date"
* "board_disposition"
* "city_manager_disposition"
* "police_district"
* "allegation_finding"
* "complainant_hearing_impaired"
* "how_complaint_received"
* "injuries_sustained"
* "complainant_medically_treated"
* "complainant_mentally_impaired"
* "notice_to_appear"
* "officer_off_duty"
* "officer_off_duty_detail"
* "officer_sex"
* "officer_race"
* "complainant_physclly_impaired"
* "complainant_race"
* "reassigned"
* "complainant_sex"
* "complainant_visually_impaired"
* "unique_officer_id"

* "instanceid"
* "date_from"
* "date_to"
* "clsd"
* "ucr"
* "dst"
* "offense"
* "location"
* "theft_code"
* "floor"
* "side"
* "opening"
* "hate_bias"
* "dayofweek"
* "rpt_area"
* "weapons"
* "date_of_clearance"
* "hour_from"
* "hour_to"
* "victim_age"
* "victim_ethnicity"
* "suspect_age"
* "suspect_race"
* "suspect_ethnicity"
* "suspect_gender"
* "totalnumbervictims"
* "totalsuspects"
* "ucr_group"
* "zip"

* "inclocation_x"
* "oid"
* "rms_no"
* "viccount"
* "citystatezip"
* "race"
* "sex"
* "age"
* "type"
* "dateoccurred"
* "monthoccured"
* "timeoccured"
* "hroccured"
* "dayoccurred"
* "rmsdup"
* "datetime"
* "dstfull"
* "zip"
* "priority_"
* "actiontakencid"
* "actiontakencidid"
* "instance_id"
* "is_juvenile"
* "interview_number"
* "interview_date"
* "vehicle_make"
* "vehicle_model"
* "vehicle_year"
* "contact_type_cid"
* "license_plate_state"
* "officer_assignment"
* "report_type_cid"
* "field_subject_cid"
* "age_range_cid"
* "district"

* "incident_location_x"
* "incident_date"
* "case_no"
* "cfs_no"
* "incident_description"
* "firearm_make"
* "firearm_model"
* "subject_gender"
* "subject_race"
* "officer_gender"
* "incident_type"


## Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.
