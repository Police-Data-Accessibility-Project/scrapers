This readme should give people everything they need to maintain the scraper.

# Summary
Only daily arrest reports

_Remove fields that were collected_
## Fields that could not be obtained within the PDAP legal guidelines:
**Note:** the naming convention for these fields may not be consistent across data sources
* _id
* _state
* _county
* ~~CaseNum~~ # Perhaps, there is `Report/DR No.`
* ~~FirstName~~
* ~~MiddleName~~
* ~~LastName~~
* Suffix
* ~~DOB~~
* Race
* ~~Sex~~
* ~~ArrestDate~~
* FilingDate
* OffenseDate
* DivisionName
* CaseStatus
* DefenseAttorney
* PublicDefender
* Judge
* ChargeCount
* ~~ChargeStatute~~
* ChargeDescription
* ChargeDisposition
* ChargeDispositionDate
* ChargeOffenseDate
* ChargeCitationNum
* ChargePlea
* ChargePleaDate
* ArrestingOfficer
* ArrestingOfficerBadgeNumber

# Other Fields:
* ArrestDate / Time (M/D/YYYY / HHMM)
* BookingDate / Time (M/D/YYYY / HHMM)
* BookingNum
* Occupation
* Height
* Weight
* Hair
* Eye
* WarrantNum
* BailAmount
* CityofResidence
* ArrestLocation
* SearchIncident


# How to locate the data source
On homepage, https://www.cityofdelano.org/105/Police-Department, Crime Statistics (Left menu)

# Data refresh rate
Daily, currently four days behind.

# Sample response
See /data/

# Legal
No crawl delay.

# Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?
