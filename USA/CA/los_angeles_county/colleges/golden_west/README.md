This readme should give people everything they need to maintain the scraper.

# Summary
Added to dataset. Agency ID: 2dcef44d114643e0b2f651886db143a6

Uses `list_pdf_extractor_v3`- Custom `get_info`, **DO NOT** update to use `list_pdf_v3`. This is due to the file paths being `../../PATH` within the HTML, but not within the actual structure of the website.
Time period of data: 2017-2020

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
Give instructions for locating the data source. A URL for a JSON file is OK, but how did you navigate there?

# Data refresh rate
Yearly ("Routinely")

# Sample response
See ./data/

# Legal
Is there anything specific to this jurisdiction we should know as we work?

# Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?
