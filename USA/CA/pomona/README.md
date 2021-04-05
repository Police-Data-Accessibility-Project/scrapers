This readme should give people everything they need to maintain the scraper.

# Summary
Is there anything in particular of note with the scraping landscape in this jurisdiction?
Time period of data: 06/29/2020-01/04/"2020" (Is likely supposed to be 2021)

_Remove fields that were collected_
## Fields that could not be obtained within the PDAP legal guidelines:
**Note:** the naming convention for these fields may not be consistent across data sources
* _id
* _state
* _county
* ~~CaseNum~~
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
* ~~ChargeDescription~~ "Nature"
* ~~ChargeDisposition~~
* ~~ChargeDispositionDate~~
* ChargeOffenseDate
* ChargeCitationNum
* ChargePlea
* ChargePleaDate
* ArrestingOfficer
* ArrestingOfficerBadgeNumber

# How to locate the data source
Main page: https://www.cpp.edu/police/ > Bottom right under "Safety Resources" > Daily crime and fire log

# Data refresh rate
Currently a year and a half behind

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.

# Legal
Is there anything specific to this jurisdiction we should know as we work?

# Data uniformity
Nature, CaseNum, Reported, Occurrence_date, location, ChargeDisposition & ChargeDispositionDate, On campus
