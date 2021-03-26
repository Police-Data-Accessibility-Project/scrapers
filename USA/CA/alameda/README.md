This readme should give people everything they need to maintain the scraper.

# Summary
Most data is private, only public data is the "Daily" activity log, monthly crime statistics, annual arrest and traffic statistics.
Time period of monthly stats: 02/2020 - 01/2021
Time period of annual arrest: 2016-2020

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
On main page: https://www.alamedaca.gov/Departments/Police-Department/Crime-Activity
Click "Monthly Crime Statistics"
Set webpage to the page with the pdf lists
Open a few pdfs and get the common file path for them, and set that as `web_path`
Set the domain to the beginning of the document host.

# Data refresh rate
Unsure, daily bulletin seems to be two days behind, and the monthly is nearly two months behind.

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.

# Legal
Is there anything specific to this jurisdiction we should know as we work?

# Data uniformity
There are no specific cases. Data is similar to other departments.
