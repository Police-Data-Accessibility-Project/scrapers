This readme should give people everything they need to maintain the scraper.

# Summary
Is there anything in particular of note with the scraping landscape in this jurisdiction?
Time period of data 2019-2020

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
Navigate to [home page](http://beaumontpd.org/)
Crime>Crime Statistics
Each year (except 2018, dead link) leads to a separate index. The scraper first scrapes this page, gets the yearly links, and then opens those to scrape the pdf links, before downloading them.

# Data refresh rate
2019-2020, 9/12 months for 2020

# Sample response
see /data/


# Legal
Is there anything specific to this jurisdiction we should know as we work?

# Data uniformity
http://beaumontpd.org/uniform-crime-reporting/, uses UCR
