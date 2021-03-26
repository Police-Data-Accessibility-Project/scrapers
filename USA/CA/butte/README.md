This readme should give people everything they need to maintain the scraper.

# Summary

Time period of booking logs: As of writing, 01/15/2021-Current day

_Remove fields that were collected_
## Fields that could not be obtained within the PDAP legal guidelines:
**Note:** the naming convention for these fields may not be consistent across data sources
* _id
* _state
* _county
* ~~CaseNum~~ **MAYBE, data contains `Reference #`, unsure of meaning**
* ~~FirstName~~
* MiddleName
* ~~LastName~~
* Suffix
* ~~DOB~~
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
* ~~ChargeCount~~
* ~~ChargeStatute~~   **Assuming this means the same as `ChargeCode`
* ~~ChargeDescription~~
* ChargeDisposition
* ChargeDispositionDate
* ChargeOffenseDate
* ChargeCitationNum
* ChargePlea
* ChargePleaDate
* ArrestingOfficer
* ArrestingOfficerBadgeNumber


Other fields:
* ~~Inmate #~~
* ~~BookingDate~~
* ~~BookingTime~~

# How to locate the data source
Under `I WANT TO...` > `MEDIA ACCESS` > `See the booking logs`

# Data refresh rate
Booking Logs: Appears to be daily
Bulletin: Daily (previous day's info) **Currently no scraper for bulletin**

# Sample response
In the `data` folder

# Legal
The usual "Don't DOS us"
`You may not obtain or attempt to obtain any materials or information through any means not intentionally made available or provided for through the Sheriff and Coroner Web Sites.`


# Data uniformity
Booking logs (in `data/arrests`) are in the date format of `mmdd-mmdd` with BL (probably Booking Logs) on the end. See example in `data/arrests/`
