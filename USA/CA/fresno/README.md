This readme should give people everything they need to maintain the scraper.

# Summary
Will need to get date from third line of pdf (date range is there)
Time period of data: Previous 30 days.

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
* ~~OffenseDate~~ **Reported**
* DivisionName
* CaseStatus
* DefenseAttorney
* PublicDefender
* Judge
* ChargeCount
* ChargeStatute
* ~~ChargeDescription~~ **Nature**
* ~~ChargeDisposition~~ **Disposition**
* ~~ChargeDispositionDate~~ **Disposition**
* ChargeOffenseDate
* ChargeCitationNum
* ChargePlea
* ChargePleaDate
* ArrestingOfficer
* ArrestingOfficerBadgeNumber

# How to locate the data source
On [home Page](http://www.fresnostate.edu/adminserv/police/), right side, `Quick Links` > `Daily Crime Log`

# Data refresh rate
Currently two days behind, likely updates on Thursdays

# Sample response
See `./data/`

# Legal
Is there anything specific to this jurisdiction we should know as we work?

# Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?
