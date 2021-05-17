This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate:
* [FOIA Request log - Police](https://data.cityofchicago.org/FOIA/FOIA-Request-Log-Police/wjkc-agnm): As needed
* [FOIA Request log - Police Board](https://data.cityofchicago.org/FOIA/FOIA-Request-Log-Chicago-Police-Board/9pd8-s9t4): As needed
* [FOIA Request log - Independent Police Review Authority (saved as IPRA)](https://data.cityofchicago.org/FOIA/FOIA-Request-Log-Independent-Police-Review-Authori/gzxp-vdqf): As needed
* [Crimes 2001-present](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2): Daily, has data excluding past 7 days
* [Police Sentiment Scores]: Monthly
* [COPA Cases Summary (Civilian Office of Police Accountability)](https://data.cityofchicago.org/Public-Safety/COPA-Cases-Summary/mft5-nfa8): Unsure
* [COPA Cases By Officer](https://data.cityofchicago.org/resource/ufxy-tgry.csv): Unsure
* [COPA Cases by Complainant or Subject](https://data.cityofchicago.org/Public-Safety/COPA-Cases-By-Complainant-or-Subject/vnz2-rmie): Unsure
* [Arrests](https://data.cityofchicago.org/Public-Safety/Arrests/dpt3-jri9): Daily
* [FOIA Request log - Chicago Public Library](https://data.cityofchicago.org/FOIA/FOIA-Request-Log-Chicago-Public-Library/n379-5uzu): As needed

### Archive:
* [IUCR Codes](https://data.cityofchicago.org/Public-Safety/Chicago-Police-Department-Illinois-Uniform-Crime-R/c7ck-438e)
* [Strategic Subject List - Historical](https://data.cityofchicago.org/Public-Safety/Strategic-Subject-List-Historical/4aki-r3np)



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
