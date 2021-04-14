This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
Annual is at the end of the year

## Legal
https://www.ci.brea.ca.us/DocumentCenter/View/1329/Website-Content-User-Policy

"Further, some materials on the City’s website and related links may be protected by copyright law, therefore, if you have any questions regarding whether you may:
  a) modify and/or re-use text, images or other web content from a City server,
  b) distribute the City’s web content, and/or
  c) “mirror” the City’s information on a non-City server,
please contact the City’s Public Information Officer."


# Fields to collect:
_Move these fields to the appropriate list below when you submit your scraper._


## Fields unobtainable within our legal guidelines:

## Fields not available:
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

## Fields being collected:

## Fields available not present on the list above:

## Data uniformity
Currently only annual is available

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.
