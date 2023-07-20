This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
* [Police Calls](https://stat.stpete.org/dataset/Police-Calls/2eks-pg5j): Daily
* [Police Officer Hires](https://stat.stpete.org/Safety/Police-Officer-New-Hires/9nht-ysk6): Monthly
* [Employment Applications for Police Officer](https://stat.stpete.org/Safety/Employment-Applications-for-Police-Officer/gty9-7yu4): Monthly
* [Park Walk And Talks](https://stat.stpete.org/Safety/Park-Walk-Talks/bk6h-28ux): Monthly
* [Directed Patrols](https://stat.stpete.org/Safety/Directed-Patrols/9cbi-474e): Monthly
* [All Tips](https://stat.stpete.org/Safety/All-Tips/v5at-unyi): Monthly
* [Citizen Calls for Service (counts)](https://stat.stpete.org/Safety/Citizen-Calls-for-Service/6373-bvti): Monthly
* [Office of Professional Standards Statistics (READ DESCRIPTION)](https://stat.stpete.org/Safety/Office-of-Professional-Standards-Statistics/6jpx-t9kn): Monthly

## Legal
* https://support.socrata.com/hc/en-us/articles/360019057154
* https://stat.stpete.org/robots.txt: Crawl-delay is 1, no need to set it.

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
