This readme should give people everything they need to maintain the scraper.

# Summary
Is there anything in particular of note with the scraping landscape in this jurisdiction?
On current page, data consists of crime trends going back to 2011 (as of data 2020)
On the first capture on [wayback](https://web.archive.org/web/20171007062627/http://www.cypressca.org/government/departments/police/crime-information/crime-statistics), data goes back to 1990 for historical trends. `Overview`, `Arrests`, `Calls for service`, `Collisions`, `Property/Evidence`, and `Hate Crimes` all go back to 2014.C Crimes by `District` go back to 2002.

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
On main [page](https://www.cypressca.org/home), Click POLICE, left column "Crime Information",

# Data refresh rate
End of the year.

# Sample response
see /data/

# Legal
Is there anything specific to this jurisdiction we should know as we work?

# Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?
