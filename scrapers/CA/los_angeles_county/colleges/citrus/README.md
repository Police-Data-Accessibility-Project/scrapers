This readme should give people everything they need to maintain the scraper.

# Summary
Added to dataset. Agency ID: 99be6b8ca2c011eb9c9b8c8590d4a7fc

There are two scrapers for this department, the annual report scraper, and the crime log scraper.

Time period of Crime log: 2017-2020, may update yearly, unsure.

Time period of annual report: 2020

_Remove fields that were collected_
## Fields that could not be obtained within the PDAP legal guidelines:
**Note:** the naming convention for these fields may not be consistent across data sources
* _id
* _state
* _county
* ~~CaseNum~~ Department based
* FirstName
* MiddleName
* LastName
* Suffix
* DOB
* Race
* Sex
* ArrestDate
* FilingDate
* ~~OffenseDate~~
* DivisionName
* ~~CaseStatus~~
* DefenseAttorney
* PublicDefender
* Judge
* ChargeCount
* ChargeStatute
* ~~ChargeDescription~~
* ~~ChargeDisposition~~
* ChargeDispositionDate
* ChargeOffenseDate
* ChargeCitationNum
* ChargePlea
* ChargePleaDate
* ArrestingOfficer
* ArrestingOfficerBadgeNumber

# How to locate the data source
On the [main page](https://www.citruscollege.edu/campussafety/Pages/default.aspx), under `Clery Act`, all data available can be found.

# Data refresh rate
All data is currently a year behind, leading me to believe that it is updated at the end of the year.

# Sample response
In `USA/CA/citrus_college/data`

# Legal
Is there anything specific to this jurisdiction we should know as we work?

# Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?
