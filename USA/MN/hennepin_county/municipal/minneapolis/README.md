This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
* [Police Incidents 2021](https://opendata.minneapolismn.gov/datasets/police-incidents-2021): Daily

### Archive:
* [Police Incidents 2108](https://opendata.minneapolismn.gov/datasets/police-incidents-2018?geometry=-165.668%2C-5.468%2C72.339%2C48.789): Archived
* [Police Incidents 2016](https://opendata.minneapolismn.gov/datasets/police-incidents-2016)
* [Police Incidents 2019](https://opendata.minneapolismn.gov/datasets/police-incidents-2019)
* [Police Incidents 2015](https://opendata.minneapolismn.gov/datasets/police-incidents-2015)
* [Police Incidents 2014](https://opendata.minneapolismn.gov/datasets/police-incidents-2014)

## Legal
Include the Terms of Service (or link to them). Is there anything else we should know?

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
* BookingNum
* BookingDate
* WarrantNum
* BailAmount
* SearchIncident

## Fields unobtainable within our legal guidelines:

## Fields not available:

## Fields being collected:

## Fields available not present on the list above:

## Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.
