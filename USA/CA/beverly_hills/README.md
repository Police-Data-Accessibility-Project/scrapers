This readme should give people everything they need to maintain the scraper.

# Summary
All are pdfs
Time period of data 12/2010 - previous month

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
https://www.beverlyhills.org/departments/policedepartment -> left menu -> crime information -> [crime statistics](http://www.beverlyhills.org/departments/policedepartment/crimeinformation/crimestatistics/web.jsp) or [interactive crime map](https://gis.beverlyhills.org/VBH/CrimeMap/)

# Data refresh rate
Monthly

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.

# Legal
Is there anything specific to this jurisdiction we should know as we work?

# Data uniformity
No cases
