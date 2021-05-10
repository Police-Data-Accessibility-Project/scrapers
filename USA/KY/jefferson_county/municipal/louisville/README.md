This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
* [Hate Crimes](https://data.louisvilleky.gov/dataset/lmpd-hate-crimes): Daily, 2016-06-09 - current
* [Assaulted Officers](https://data.louisvilleky.gov/dataset/assaulted-officers): Daily, 2015-11-30 - current
* [Crime Data](https://data.louisvilleky.gov/dataset/crime-reports): Daily, 01-01-2019 - three days behind current. Note that the data is separated by year, going back to 2003 (not currently scraped)
* [Employee Characteristics](https://lky-open-data.s3.amazonaws.com/LMPD/LMPD_Demographics.csv): Daily, 2015-11-30 - current
* [Uniform Citation Data](https://data.louisvilleky.gov/sites/default/files/UniformCitationData%20.csv): Daily, temporal coverage 2010-01-01 - current
* [Officer involved shooting statistical analysis](https://data.louisvilleky.gov/dataset/officer-involved-shooting-and-statistical-analysis): Annual, 2018-2020. " Data is updated after there is an officer involved shooting." (not scraped, use list_pdf_v3)
* [Firearms intake](https://data.louisvilleky.gov/dataset/firearms-intake): Weekly, 2017-02-23 - 2019-03-27

## Legal
https://data.louisvilleky.gov/louisville-metro-government-open-data-platform-terms-use

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
