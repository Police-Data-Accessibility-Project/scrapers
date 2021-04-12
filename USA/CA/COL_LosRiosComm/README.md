This readme should give people everything they need to maintain the scraper.

# Summary
Crime statistics are scraped by `annual_report_scraper.py`

Daily bulletin is scraped by `LosRios_dailybull_scraper.py`
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

# Other Fields:

* ReportDate
* Location

# How to locate the data source
Clery: https://police.losrios.edu/clery

Bulletin:
1. On [home page](https://police.losrios.edu/)
1. Bottom of page, `Crime Log`
1. Choose any school (all lead to same place)

# Data refresh rate
Annual should be annual, latest available year is 2020

Daily is daily, depending on if there is crime.

# Sample response
See /data/

# Legal
No robots.txt or ToS to be see

# Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?
