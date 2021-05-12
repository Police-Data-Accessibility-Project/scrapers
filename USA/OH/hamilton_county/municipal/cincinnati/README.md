This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
[Calls for Service](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Police-Calls-for-Servic/gexm-h6bt): Daily
[Crime Incidents](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Crime-Incidents/k59e-2pvf): Daily
[Use of Force](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Use-of-Force/8us8-wi2w): Daily (may not be daily, "*This information will not be updated while the Cincinnati Police Department undergoes transfer to a new data management system.*")
[Assaults on Officers](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Assaults-on-Officers/bmmy-avxm): Daily, (may not be daily, see Use of Force)
[Shootings (non-officer involved)](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-CPD-Shootings/7a3r-kxji): Daily
[Officer Involved Shootings](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Officer-Involved-Shooti/r6q4-muts): Daily
[Traffic Stops (Drivers)](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Traffic-Stops-Drivers-/hibq-hbnj): Daily
[Traffic Stops (All subjects)](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Traffic-Stops-All-Subje/ktgf-4sjh): Daily
[Ped Stops](https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Pedestrian-Stops/jx3x-rh6i): Daily
[Citizen Complaint Authority Closed Complaints](https://data.cincinnati-oh.gov/Safety/Citizen-Complaint-Authority-CCA-Closed-Complaints/ii65-eyg6): Daily


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
