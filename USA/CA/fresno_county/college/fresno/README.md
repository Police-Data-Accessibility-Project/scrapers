This readme should give people everything they need to maintain the scraper.

# Summary
Added to dolt. Agency ID: 3255cb899684443ab5add9135738a915

**DO NOT** attempt to update to use `list_pdf_scrapers` or `bs_common`

Only crime statistics

Time period of data 08/2018-02/2021

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
* ~~OffenseDate~~
* DivisionName
* CaseStatus
* DefenseAttorney
* PublicDefender
* Judge
* ChargeCount
* ~~ChargeStatute~~
* ~~ChargeDescription~~
* ~~ChargeDisposition~~
* ~~ChargeDispositionDate~~
* ChargeOffenseDate
* ChargeCitationNum
* ChargePlea
* ChargePleaDate
* ArrestingOfficer
* ArrestingOfficerBadgeNumber

# Other Fields

* Location
* On Campus?

# How to locate the data source
On homepage, https://www.fresnostate.edu/, `Daily Crime Log` on right vertical menu.

# Data refresh rate
Daily.

# Sample response
See /data/

# Legal
No set delay.

# Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?
