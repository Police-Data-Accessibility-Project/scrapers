This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
* [Officer Involved Shootings](https://www.dallasopendata.com/Public-Safety/Dallas-Police-Officer-Involved-Shootings/4gmt-jyx2): "Automated", Unknown, last update to data was June 10, 2020
* [Police Incidents](https://www.dallasopendata.com/Public-Safety/Police-Incidents/qv6i-rri7): Daily
* [Active Calls](https://www.dallasopendata.com/Public-Safety/Dallas-Police-Active-Calls/9fxf-t2tr): Every 2 minutes, can be run daily instead.
* [Arrests](https://www.dallasopendata.com/Public-Safety/Police-Arrests/sdr7-6v3j): Daily
* [Police Arrest Charges](https://www.dallasopendata.com/Public-Safety/Police-Arrest-Charges/9u3q-af6p): Daily (Not entirely sure what the difference between this and `Arrests` is)

## Legal
https://www.dallasopendata.com/stories/s/Dallas-OpenData-Terms-of-Use/5dr7-2kgq/

# Fields to collect:
_Move these fields to the appropriate list below when you submit your scraper._

* _id
* _state
* _county
* CaseNum
* FirstName
* MiddleName
* LastName
* Suffix
* DOB
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
* BookingNum
* BookingDate
* WarrantNum
* BailAmount
* SearchIncident

## Fields unobtainable within our legal guidelines:

## Fields not available:

## Fields being collected:
* Race
* Sex
* ArrestDate

## Fields available not present on the list above:
* IncidentNum
* ArrestDay
* Severity

## Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.
