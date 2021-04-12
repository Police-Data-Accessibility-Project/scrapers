This readme should give people everything they need to maintain the scraper.

# Summary
Is there anything in particular of note with the scraping landscape in this jurisdiction?
Time period of data: 2010-2019

_Remove fields that were collected_
## Fields that could not be obtained within the PDAP legal guidelines:
**Note:** the naming convention for these fields may not be consistent across data sources
* _id
* _state
* _county
* CaseNum
* FirstName
* MiddleName
* LastName
* Suffix
* DOB
* Race
* Sex
* ArrestDate
* FilingDate
* OffenseDate
* DivisionName
* CaseStatus
* DefenseAttorney
* PublicDefender
* Judge
* ChargeCount
* ChargeStatute
* ChargeDescription
* ChargeDisposition
* ChargeDispositionDate
* ChargeOffenseDate
* ChargeCitationNum
* ChargePlea
* ChargePleaDate
* ArrestingOfficer
* ArrestingOfficerBadgeNumber

# How to locate the data source
1. On [home page](https://www.dixonpolice.org/Year-EndReports), open `Inspect Element` > Networking.
1. Refresh page
1. Scroll down in networking tab until you find `?media_folder_id=`
1. Copy the `Request URL`, and set it as `request_url` in `configs.py`
1. Run the script

# Data refresh rate
Last year_end report was in 2019

# Sample response
See `./data/`

# Legal
There is no `robots.txt`, set `sleep_time` as you please (above 0 (zero) of course)

# Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?
