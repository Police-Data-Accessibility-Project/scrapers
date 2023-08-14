This readme should give people everything they need to maintain the scraper.

# Summary

Added to datasets. Agency ID: b83eb5be02144bf9a884d1697dc24a51
This scraper is **NOT** the default `list_pdf_scrapers`.
This jurisdiction uses a different naming system.

- `CFS_scraper.py` scrapes the Calls for service
- `antiochca_scraper.py` scrapes the annual reports
- `antiocha_arrest_scraper.py` scrapes the arrests.

Time period of crime statistics: 2006-current

_Remove fields that were collected_
## Fields that could not be obtained within the PDAP legal guidelines:
**Note:** the naming convention for these fields may not be consistent across data sources
* _id
* _state
* _county
* MiddleName
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

# How to locate the data source
Go to https://www.antiochca.gov/police/
Right side > Crime statistics > crime statistics


Eventually a scraper will be written for the [arrest reports](https://www.antiochca.gov/police/crime-statistics/adult-arrest-report/)


# Data refresh rate
Crime stats are yearly, with the exception of the current year, which I believe updates monthly
Calls for service updates weekly, updates the following monday


[Calls for service](https://www.antiochca.gov/police/crime-statistics/calls-for-service/) (**Not Scraped**) updates weekly.


[Adult arrest reports](https://www.antiochca.gov/police/crime-statistics/adult-arrest-report/) (**Not Scraped**) updates weekly (Pull on Monday)


# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.

# Legal
Is there anything specific to this jurisdiction we should know as we work?

# Data uniformity
Cases are not scraped yet.
