This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Added to dataset. Agency ID: 517d8134b2ca40e2b7da2be4b9f13ccd

Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
* [In car video dropped frame report](https://data.seattle.gov/Public-Safety/Seattle-Police-Department-In-Car-Video-Dropped-Fra/k7a5-emiw): Unsure
* [Office of Police Accountability Complaints](https://data.seattle.gov/Public-Safety/Office-of-Police-Accountability-Complaints/99yi-dthu): Daily
* [Seattle Police Disciplinary Appeals](https://data.seattle.gov/Public-Safety/Seattle-Police-Disciplinary-Appeals/2qns-g7s7): "To be determined"
* [Call Data](https://data.seattle.gov/Public-Safety/Call-Data/33kz-ixgy): Daily
* [Terry Stops](https://data.seattle.gov/Public-Safety/Terry-Stops/28ny-9ts8): Daily
* [SPD Officer Involved Shooting (OIS) Data](https://data.seattle.gov/Public-Safety/SPD-Officer-Involved-Shooting-OIS-Data/mg5r-efcm): "Other"
* [Use of Force](https://data.seattle.gov/Public-Safety/Use-Of-Force/ppi5-g2bj): Daily, duplicate  data bug
* [Crisis Data](https://data.seattle.gov/Public-Safety/Crisis-Data/i2q9-thny): Daily, "Data is denormalized to represent the one to many relationship between the record and the reported disposition of the contact. **USE CAUTION WHEN COUNTING**"
* [Crime Data 2008-present](https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5): Daily
* [PDRs After using "City of Seattle Public Records Request Center"Public Safety](https://data.seattle.gov/Public-Safety/PDRs-After-using-City-of-Seattle-Public-Records-Re/wj44-r6br): Daily
* [COBAN Logs](https://data.seattle.gov/Public-Safety/COBAN-Logs/tpvk-5fr3): Daily, says weekly in description but daily in metadata
* [Closed Case Summaries 2020-present](https://data.seattle.gov/Public-Safety/Closed-Case-Summaries-2020-Present-/f8kp-sfr3): To be determined

## Archive
* [Seattle Police PDRs (public data requests)](https://data.seattle.gov/Public-Safety/Seattle-Police-PDRs/8fwq-jcnn)
## Legal
Include the Terms of Service (or link to them). Is there anything else we should know?

# Fields to collect:
_Move these fields to the appropriate list below when you submit your s* "uniqueid"
* "incident_num"
* "incident_type"
* "occured_date_time"
* "precinct"
* "sector"
* "beat"
* "officer_id"
* "subject_id"
* "subject_race"
* "subject_gender"

* "assigned_staff"
* "completed_closed"
* "create_date"
* "days_open"
* "request_status"
* "summary"
* "customer_full_name"
* "spd_sub_type"
* "close_date"
* "reference_no"
* "total_time_spent_h"

* "assigned_dept"
* "request_type"
* "city_requestertype_internal"
* "source"
* "spd_receiptofrecordspreference"
* "spd_recreqincidentreportyesno"
* "spd_recreqfollowupinvestigationyesno"
* "spd_recreqvideoyesno"
* "spd_recreqspd911yesno"
* "spd_recreqphotoyesno"
* "spd_recreqotheryesno"

* "posted_date"
* "case"
* "disposition"

* "cad_event_number"
* "event_clearance_description"
* "call_type"
* "priority"
* "initial_call_type"
* "final_call_type"
* "original_time_queued"
* "arrived_time"
* "beat"

* "file_date_time"
* "time_range"
* "frame_range"
* "time_stamp_start"
* "time_stamp_end"
* "duration"
* "fps"
* "dropped_frames"
* "resolution"
* "file_size"
* "file_name"

* "subjectagegroup"
* "subjectid"
* "go_num"
* "terry_stop_id"
* "weapon_type"
* "officerid"
* "officer_yob"
* "officer_gender"
* "officer_race"
* "subjectrace"
* "subjectgender"
* "reported_date"
* "reported_time"
* "initialcalltype"
* "finalcalltype"
* "calltype"
* "officersquad"
* "arrestflag"
* "friskflag"
* "frb"
* "go"
* "date_time"
* "blurred_address"
* "longitude"
* "latitude"
* "city"
* "state"
* "rank"
* "years_of_spd_service"
* "officer_injured"
* "number_of_rounds"
* "subject_gender"
* "subject_dob"
* "subject_age"
* "subject_weapon"
* "type_of_weapon"
* "fatal"
* "on_duty"
* "justified_policy"
* "officer_disciplined"
* "summary"

* "unique_id"
* "file_number"
* "incident_number"
* "occurred_date"
* "received_date"
* "incident_precinct"
* "incident_sector"
* "incident_beat"
* "allegation"
* "disposition"
* "discipline"
* "named_employee_id"
* "named_employee_race"
* "named_employee_gender"
* "named_employee_age_at"
* "named_employee_title_at"
* "named_employee_squad_at"
* "complainant_number"
* "complainant_gender"
* "complainant_race"
* "complainant_age_complaint"
* "case_status"
* "finding"
* "investigation_begin_date"
* "investigation_end_date"

* "opa_case"
* "date_of_discipline"
* "disciplinary_decision"
* "date_of_appeal"
* "appeal_type"
* "appeal_status"
* "appeal_outcome"
* "date_appeal_closed"

* "filename"
* "logtime"
* "userid"
* "actcode"
* "id"
* "sent"

* "template_id"
* "use_of_force_indicator"
* "subject_veteran_indicator"
* "cit_officer_requested"
* "cit_officer_dispatched"
* "cit_officer_arrived"
* "officer_year_of_birth"
* "officer_years_of_experience"
* "cit_certified_indicator"
* "officer_bureau_desc"
* "officer_precinct_desc"
* "officer_squad_desc"
* "report_number"
* "offense_id"
* "offense_start_datetime"
* "offense_end_datetime"
* "report_datetime"
* "group_a_b"
* "crime_against_category"
* "offense_parent_group"
* "offense"
* "offense_code"
* "mcpp"
* "_100_block_address"
* "latitude"



## Fields unobtainable within our legal guidelines:

## Fields not available:

## Fields being collected:

## Fields available not present on the list above:

## Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.
