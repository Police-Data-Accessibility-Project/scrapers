This readme should give people everything they need to maintain the scraper.

# Summary
This scraper saves data into a seperate folder if it has `daily` in the `name`. **DO NOT** attempt to update to use `list_pdf_scrapers` or `bs_common`, as the `get_files` function sorts the documents as they are downloaded by name. As they are unique to this department, I see no reason to add them to the common script.

Most data is private, only public data is the "Daily" activity log, monthly crime statistics, annual arrest and traffic statistics.

Time period of monthly stats: 02/2020 - 01/2021

Time period of annual arrest: 2016-2020

**NOTE:** daily_bulletin is no longer used by the PD, they have migrated to crimegraphics. See message under "[Alameda Crime Graphics](https://www.alamedaca.gov/Departments/Police-Department/Crime-Activity)"

[Internet Archive capture](https://web.archive.org/web/20210505124522/https://www.alamedaca.gov/Departments/Police-Department/Crime-Activity)

> \*\*On April 7, 2021, APD's Crime Mapping website and Daily Activity Logs were replaced with Alameda's Crime Graphics website. Daily Activity Logs will now be referred to as Media Bulletins and are accessible through the Crime Graphics website.**

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

Set `webpage` to the page with the pdf lists


Open a few pdfs and get the common file path for them, and set that as `web_path`


Set the `domain` to the beginning of the document host.


# Data refresh rate
Unsure, daily bulletin seems to be two days behind, and the monthly is nearly two months behind.

Monthly reports are updated 10-14 business days after the end of the month

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.

# Legal
Is there anything specific to this jurisdiction we should know as we work?

# Data uniformity
There are no specific cases. Data is similar to other departments.
