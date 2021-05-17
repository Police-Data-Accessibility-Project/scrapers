This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
* [In car video dropped frame report](https://data.seattle.gov/Public-Safety/Seattle-Police-Department-In-Car-Video-Dropped-Fra/k7a5-emiw): Unsure
* [Office of Police Accountability Complaints](https://data.seattle.gov/Public-Safety/Office-of-Police-Accountability-Complaints/99yi-dthu): Daily
* [Seattle Police Disciplinary Appeals](https://data.seattle.gov/Public-Safety/Seattle-Police-Disciplinary-Appeals/2qns-g7s7): "To be determined"
* [Call Data](https://data.seattle.gov/Public-Safety/Call-Data/33kz-ixgy): Daily
* [Terry Stops](https://data.seattle.gov/Public-Safety/Terry-Stops/28ny-9ts8): Daily
* [SPD Officer Involved Shooting (OIS) Data](https://data.seattle.gov/Public-Safety/SPD-Officer-Involved-Shooting-OIS-Data/mg5r-efcm): "Other"

## Archive
* [Seattle Police PDRs (public data requests)](https://data.seattle.gov/Public-Safety/Seattle-Police-PDRs/8fwq-jcnn)
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
