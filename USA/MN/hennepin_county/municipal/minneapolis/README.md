This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
* [Police Incidents 2021](https://opendata.minneapolismn.gov/datasets/police-incidents-2021): Daily
* [Stop Data](https://opendata.minneapolismn.gov/datasets/police-stop-data?geometry=67.593%2C-31.286%2C-176.391%2C66.545): Unsure, seems to be at the end of the day
* [Use of Force](https://opendata.minneapolismn.gov/datasets/police-use-of-force?geometry=-165.668%2C-5.468%2C72.340%2C48.789): Daily by 9:30 AM
* [Officer Involved Shootings](https://opendata.minneapolismn.gov/datasets/police-officer-involved-shootings): Last Friday of the month at 7:30 am
* [Officer Conduct Data](https://opendata.minneapolismn.gov/datasets/officer-conduct-data/data): Unsure, may be as needed or annually (put in monthly scraper)
* [Shots fired](https://opendata.minneapolismn.gov/datasets/shots-fired?geometry=-93.729%2C44.884%2C-92.799%2C45.055): Daily by 9:30AM

### Archive:
* [Police Incidents 2108](https://opendata.minneapolismn.gov/datasets/police-incidents-2018?geometry=-165.668%2C-5.468%2C72.339%2C48.789): Archived
* [Police Incidents 2016](https://opendata.minneapolismn.gov/datasets/police-incidents-2016)
* [Police Incidents 2019](https://opendata.minneapolismn.gov/datasets/police-incidents-2019)
* [Police Incidents 2015](https://opendata.minneapolismn.gov/datasets/police-incidents-2015)
* [Police Incidents 2014](https://opendata.minneapolismn.gov/datasets/police-incidents-2014)
* [Police Incidents 2013](https://opendata.minneapolismn.gov/datasets/police-incidents-2013)
* [Police Incidents 2012](https://opendata.minneapolismn.gov/datasets/police-incidents-2012)
* [Police Incidents 2011](https://opendata.minneapolismn.gov/datasets/police-incidents-2011)
* [Police Incidents 2010](https://opendata.minneapolismn.gov/datasets/police-incidents-2010)
* [Police Incidents 2018 PIMS](https://opendata.minneapolismn.gov/datasets/police-incidents-2018-pims?geometry=-165.668%2C-5.468%2C72.339%2C48.789)
* [Police Incidents 2017](https://opendata.minneapolismn.gov/datasets/police-incidents-2017)
* [Police Incidents 2020](https://opendata.minneapolismn.gov/datasets/police-incidents-2020)

## Legal
* https://creativecommons.org/licenses/by-sa/4.0/
* https://opendata.minneapolismn.gov/robots.txt: 60 crawl-delay

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
