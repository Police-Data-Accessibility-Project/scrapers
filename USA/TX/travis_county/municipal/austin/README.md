This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
[Annual Crime 2015](https://data.austintexas.gov/Public-Safety/Annual-Crime-Dataset-2015/spbg-9v94): "As needed"
[Anual Crime 2016](https://data.austintexas.gov/Public-Safety/2016-Annual-Crime-Data/8iue-zpf6): "As needed"
[Crime Reports](https://data.austintexas.gov/Public-Safety/Crime-Reports/fdj4-gpfu): Weekly
[Racial Profiling Dataset 2016 - Citations](https://data.austintexas.gov/Public-Safety/Racial-Profiling-Dataset-2015-Citations/sc6h-qr9f): "As needed"
[Response to Resistance (R2R) 2015](https://data.austintexas.gov/Public-Safety/R2R-2015/iydp-s2cf): "As needed"
[Hate crimes 2017](https://data.austintexas.gov/dataset/Hate-Crimes-2017/79qh-wdpx): "As needed"
[Guide - Arrests](https://data.austintexas.gov/Public-Safety/GUIDE-Arrests/cpxf-2jga): Unknown
[Hate Crimes 2018 Final](https://data.austintexas.gov/Public-Safety/Hate-Crimes-2018-Final/idj2-d9th): Not documented, but likely "as needed"
[Response to resistance 2016](https://data.austintexas.gov/Public-Safety/R2R-2016/h8jq-pcz3): Annually, not sure why it would be annually, field was likely not updated.
[Racial Profiling Data - Citations 2017](https://data.austintexas.gov/dataset/2017-Racial-Profiling-Dataset-Citations/7guv-wkre): "As needed"
[GUIDE - Officer involved shooting](https://data.austintexas.gov/Public-Safety/GUIDE-2017-Officer-Involved-Shooting/eqwy-k8kh): "As needed"
[Guide 2018 Racial Profiling](https://data.austintexas.gov/Public-Safety/GUIDE-2018-Racial-Profiling/mipf-8at9): Not documented, likely "as needed" (never)
[Crime Reports 2017](https://data.austintexas.gov/Public-Safety/Crime-Reports-2017/4bxg-n3iv): Weekly, not sure why
[2018 RP Arrests](https://data.austintexas.gov/Public-Safety/2018-RP-Arrests/xfke-9bsj): Not documented
[2017 Annual Crime](https://data.austintexas.gov/Public-Safety/2017-Annual-Crime/3t4q-mqs5): "As needed"
[Hate Crimes 2018 Final](https://data.austintexas.gov/Public-Safety/Hate-Crimes-2018-Final/idj2-d9th): Not documented
[R2R (response to resistance) 2016](https://data.austintexas.gov/Public-Safety/R2R-2016/h8jq-pcz3): Annually, likely left over.
[2014 Racial Profiling Data - Citations](https://data.austintexas.gov/Public-Safety/2014-Racial-Profiling-Dataset-Citations/mw6q-k5gy): "As needed"
[2017 Racial Profiling Arrests](https://data.austintexas.gov/Public-Safety/2017-Racial-Profiling-Arrests/x4p3-hj3y): "As needed"
[Guide 2018 - Racial Profiling](https://data.austintexas.gov/Public-Safety/GUIDE-2018-Racial-Profiling/mipf-8at9): Not documented
[2018 Annual Crime](https://data.austintexas.gov/Public-Safety/2018-Annual-Crime/pgvh-cpyq): Not documented.
[Officer Involved Shootings 2008-2017](https://data.austintexas.gov/Public-Safety/Officer-Involved-Shootings-2008-17-Incidents/uzqv-9uza): "As needed"
[2008-17 OIS (officer_involved_shooting) Subjects](https://data.austintexas.gov/Public-Safety/2008-17-OIS-Subjects/u2k2-n8ez): "As needed"
[R2R 2010](https://data.austintexas.gov/Public-Safety/R2R-2010/q5ym-htjz): "As needed"
[Hate Crimes 2020](https://data.austintexas.gov/Public-Safety/Hate-Crimes-2020/mi2a-twn5): "As needed"
[R2R 2017](https://data.austintexas.gov/Public-Safety/2017-R2R-Dataset/5evd-3tba): Not documented
[R2R SUBJECTS 2017](https://data.austintexas.gov/dataset/2017-R2R-Subjects/5w6q-adh8): Not documented
[2016 RP Citations](https://data.austintexas.gov/Public-Safety/2016-RP-Citations/urfd-wng9): "As needed"
[R2R 2011](https://data.austintexas.gov/Public-Safety/R2R-2011/jipa-v8m5): "As needed"
[2014 Racial Profiling Arrests](https://data.austintexas.gov/Public-Safety/2014-Racial-Profiling-Arrests/fk9e-2udt): "As needed"
[R2R 2012](https://data.austintexas.gov/Public-Safety/R2R-2012/bx9w-y5sd): "As needed"
[2018 RP Citations](https://data.austintexas.gov/Public-Safety/2018-RP-Citations/b9rk-dixy): Not documented
[2017 racial_profiling Warning + Field Observations](https://data.austintexas.gov/Public-Safety/2017-Racial-Profiling-Warnings-Field-Observations/5asp-dw2k): "As needed"
[Crime reports 2015](https://data.austintexas.gov/Public-Safety/Crime-Reports-2015/g3bw-w7hh): "Weekly"
[2019 Discharge of a Firearm against dog](https://data.austintexas.gov/Public-Safety/2019-Discharge-of-a-Firearm-Against-a-Dog/9qgn-zgva): Not documented
[GUIDE 2017 - RP](https://data.austintexas.gov/Public-Safety/GUIDE-2017-RP/tud4-5x9v): "As needed"
[Hate Crimes 2019](https://data.austintexas.gov/Public-Safety/Hate-Crimes-2019/e3qf-htd9): Not documented
[2018 RP Warnings + Field Observations](https://data.austintexas.gov/Public-Safety/2018-RP-Warnings-Field-Observations/vchc-c622): Not documented
[Hate Crimes 2021](https://data.austintexas.gov/Public-Safety/Hate-Crimes-2021/dmxv-zsfa): "As needed"
[R2R 2017](https://data.austintexas.gov/Public-Safety/2017-R2-R-Subjects/bmeh-xaea): Undocumented
[2014 Racial Profiling Warnings + field Observations](https://data.austintexas.gov/City-Government/2014-Racial-Profiling-Warnings-Field-Observations/tqet-vty2): "As needed"
[2019 RP Citations]("https://data.austintexas.gov/Public-Safety/2019-Racial-Profiling-RP-Citations/uzta-a386"): "As needed"
[2018 R2R Data](https://data.austintexas.gov/Public-Safety/2018-Response-to-Resistance-Data/rus9-w6q5): "As needed"
[2019 R2R Data](https://data.austintexas.gov/dataset/2019-Response-to-Resistance-Data/3bfz-mri4): "As needed"
[2015 RP + FO](https://data.austintexas.gov/Public-Safety/2015-RP-Warnings-Field-Observations/v6rq-ainw): "As needed"
[2019 RP Warning and FO](https://data.austintexas.gov/Public-Safety/2019-Racial-Profiling-RP-Warning-and-Field-Observa/djcn-eje6): "As needed"
[2019 r2r subjects](https://data.austintexas.gov/Public-Safety/2019-Response-to-Resistance-Subject-Data/dwrk-z7q9): Not documented
[2018 R2R Subjectes](https://data.austintexas.gov/Public-Safety/2018-Response-to-Resistance-Subjects-Data/c7is-tz8m)
[S.D.1a-c Racial Profiling Motor Vehicle Stops](https://data.austintexas.gov/Public-Safety/S-D-1a-c-Racial-Profiling-Motor-Vehicle-Stops/9dis-d5bk): Annually
[2019 RP guide](https://data.austintexas.gov/Public-Safety/2019-Racial-Profiling-RP-Guide/f59a-wt7w): "As needed"
[S.D.1a-c Population vs. MV Stops](https://data.austintexas.gov/Public-Safety/S-D-1a-c-Population-vs-MV-Stops/87wz-a3h2): "Annually"
[S.D.1b Warnings FOs](https://data.austintexas.gov/Public-Safety/S-D-1b-Warnings-FOs/gzfe-bzj4): "Annually"

## Legal

From: https://data.austintexas.gov/Public-Safety/2016-Annual-Crime-Data/8iue-zpf6:

> 1. The data provided is for informational use only and is not considered official APD crime data as in official Texas DPS or FBI crime reports.
> 2. APD’s crime database is continuously updated, so reports run at different times may produce different results. Care should be taken when comparing against other reports as different data collection methods and different data sources may have been used.
> 3. The Austin Police Department does not assume any liability for any decision made or action taken or not taken by the recipient in reliance upon any information or data provided.

# Fields to collect:
* "go_primary_key"
* "council_district"
* "go_highest_offense_desc"
* "highest_nibrs_ucr_offense_description"
* "go_report_date"
* "go_location"
* "clearance_status"
* "clearance_date"
* "go_district"
* "go_location_zip"
* "go_census_tract"
* "go_x_coordinate"
* "go_y_coordinate"

* "go_primary_key_year_plus"
* "crime_type"
* "go_y_coordinate"
* "go_census_tract"

* "primary_key"
* "rep_date"
* "rep_time"
* "sex"
* "apd_race_desc"
* "location"
* "person_searched_desc"
* "reason_for_stop_desc"
* "search_based_on_desc"
* "search_disc_desc"
* "race_known"
* "x_coordinate"
* "y_coordinate"
* "sector"
* "local_field1"

* "data_purpose"
* "none"

* "incident_report_number"
* "ucr_code"
* "family_violence"
* "occ_date_time"
* "occ_date"
* "occ_time"
* "rep_date_time"
* "location_type"
* "address"
* "zip_code"
* "district"
* "pra"
* "census_tract"
* "ucr_category"
* "category_description"
* "latitude"
* "longitude"
* "location"

* Incident Number
* Highest Offense Description
* Highest Offense Code
* Family Violence
* Occurred Date Time
* Occurred Date
* Occurred Time
* Report Date Time
* Report Date
* Report Time
* Location Type
* Address
* Zip Code
* Council District
* APD Sector
* APD District
* PRA
* Census Tract
* Clearance Status
* Clearance Date
* UCR Category
* Category Description
* X-coordinate
* Y-coordinate
* Latitude
* Longitude
* Location
* Zip Codes
* Single Member Council Districts
* BOUNDARIES_single_member_districts
* Zoning Review Cases_data

* "case_number"
* "offense_description"
* "date"
* "species"
* "hit"
* "killed"

* "month"
* "incident_number"
* "date_of_incident_day_of_week"
* "number_of_vitims_under_18"
* "number_of_victims_over_18"
* "number_of_offenders_under_18"
* "number_of_offenders_over_18"
* "race_or_ethnic_of_offender"
* "offense"
* "offense_location"
* "bias"
* "victim_type"

* "race_ethnic_of_offender_s"
* "offense_s"
* "date_of_incident"
* "day_of_week"
* "number_of_victims_under_18"
* "number_of_offenders_under"
* "number_of_offenders_over"
* "race_ethnicity_of_offenders"
* "notes"

* "case"
* "time"
* "premise_category"
* "less_lethal_force_used_by_apd_prior_to_shooting"
* "subject_weapon"
* "number_of_officer_shooters"
* "call_type_categories"
* "officers_present_when_shots_fired"
* "hits"
* "location_1"

* "subject_race_ethnicity"
* "subject_gender"
* "subject_injuries"
* "race"
* "count"
* "of_total_motor_vehicle_stops"
* "city_of_austin_over_18"
* "city_of_austin_over_18_1"
* "difference_population_vs"
* "year"

* "rin"
* "date_occurred"
* "time_occurred"
* "area_command"
* "nature_of_contact"
* "reason_desc"
* "r2r_level"
* "master_subject_id"
* "subject_sex"
* "subject_race"
* "subject_ethnicity"
* "subject_conduct_desc"
* "subject_resistance"
* "weapon_used_1"
* "weapon_used_2"
* "weapon_used_3"
* "weapon_used_4"
* "weapon_used_5"
* "number_shots"
* "subject_effects"
* "effect_on_officer"
* "officer_organization_desc"
* "officer_commission_date"
* "officer_yrs_of_service"
* "councildistrict"

* "council_district"

* "county"
* "apd_race"
* "zip"
* "county_description"

* "county"

* "county_desc"

* "sector"

* "citation_number"
* "off_from_date"
* "off_time"
* "race_origin_code"
* "case_party_sex"
* "reason_for_stop"
* "vl_street_name"
* "msearch_y_n"
* "msearch_type"
* "msearch_found"

* "warning_fo"
* "person_searched"
* "search_based_on"
* "search_discovered"
* "cad_date_time"
* "corrected_search_based_on"
* "corrected_search_discovered"
* "cad_sector"
* "apd_sector"
* "councildistrict"
* "county_description"
* "reason_for_stop_tcole_form"
* "person_search_yn"
* "search_found"

* "offensedate"
* "offensetime"
* "search_yn"
* "id"
* "county_desc"
* "reason_for_stop_tcole_form_mv_stops_only"
* "unnamed_column"

* "year"
* "citations"
* "arrests"
* "field_observations_warnings"
* "total_motor_vehicle_stops"

* "of_total_warnings_and_field"

## Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.
