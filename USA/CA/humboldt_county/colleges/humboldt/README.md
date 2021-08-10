This readme should give people everything they need to maintain the scraper.

# Summary
Added to Datasets. Agency ID: 02342e64a2c011eb9c9b8c8590d4a7fc
Is there anything in particular of note with the scraping landscape in this jurisdiction?
Time period of data: Previous two months.

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
* ChargeStatute
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

* Location
* ReportDate

# How to locate the data source
Main page: https://police.humboldt.edu/ > Top horizontal menu bar, furthest to the right, `HSU Crime Map`

# Data refresh rate
Updates daily, but only if there was a crime.

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.

# Legal
There is no ToS for crimegraphics

# Data uniformity
