This readme should give people everything they need to maintain the scraper.

# Summary
**DO NOT** attempt to update to use `list_pdf_scrapers` or `bs_common`

Only crime statistics

Time period of data 08/2018-02/2021

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
On homepage, https://www.cityofdelano.org/105/Police-Department, Crime Statistics (Left menu)

# Data refresh rate
"Regularly" - Data is currently two months behind

# Sample response
See /data/

# Legal
Crawl-delay: 20

# Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?
