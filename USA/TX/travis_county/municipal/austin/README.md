This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
[Annual Crime 2015](https://data.austintexas.gov/Public-Safety/Annual-Crime-Dataset-2015/spbg-9v94): "As needed"
[Anual Crime 2016](https://data.austintexas.gov/Public-Safety/2016-Annual-Crime-Data/8iue-zpf6): "As needed"
[Crime Reports](https://data.austintexas.gov/Public-Safety/Crime-Reports/fdj4-gpfu): Weekly
[Racial Profiling Dataset 2016 - Citations](https://data.austintexas.gov/Public-Safety/Racial-Profiling-Dataset-2015-Citations/sc6h-qr9f): "As needed"
[Response to Resistance (R2R) 2015](https://data.austintexas.gov/Public-Safety/R2R-2015/iydp-s2cf): "As needed"
[Hate crimes 2017](https://data.austintexas.gov/dataset/Hate-Crimes-2017/79qh-wdpx): "As needed"
[Guide - Arrests](https://data.austintexas.gov/Public-Safety/GUIDE-Arrests/cpxf-2jga): Unknown
[Hate Crimes 2018 Final](https://data.austintexas.gov/Public-Safety/Hate-Crimes-2018-Final/idj2-d9th): Not documented, but likely "as needed"
[Response to resistance 2016](https://data.austintexas.gov/Public-Safety/R2R-2016/h8jq-pcz3): Annually, not sure why it would be annually, field was likely not updated.
[Racial Profiling Data - Citations 2017](https://data.austintexas.gov/dataset/2017-Racial-Profiling-Dataset-Citations/7guv-wkre): "As needed"
[GUIDE - Officer involved shooting](https://data.austintexas.gov/Public-Safety/GUIDE-2017-Officer-Involved-Shooting/eqwy-k8kh): "As needed"
[Guide 2018 Racial Profiling](https://data.austintexas.gov/Public-Safety/GUIDE-2018-Racial-Profiling/mipf-8at9): Not documented, likely "as needed" (never)
[Crime Reports 2017](https://data.austintexas.gov/Public-Safety/Crime-Reports-2017/4bxg-n3iv): Weekly, not sure why
[2018 RP Arrests](https://data.austintexas.gov/Public-Safety/2018-RP-Arrests/xfke-9bsj): Not documented
[2017 Annual Crime](https://data.austintexas.gov/Public-Safety/2017-Annual-Crime/3t4q-mqs5): "As needed"
[Hate Crimes 2018 Final](https://data.austintexas.gov/Public-Safety/Hate-Crimes-2018-Final/idj2-d9th): Not documented
[R2R (response to resistance) 2016](https://data.austintexas.gov/Public-Safety/R2R-2016/h8jq-pcz3): Annually, likely left over.
[2014 Racial Profiling Data - Citations](https://data.austintexas.gov/Public-Safety/2014-Racial-Profiling-Dataset-Citations/mw6q-k5gy): "As needed"
[2017 Racial Profiling Arrests](https://data.austintexas.gov/Public-Safety/2017-Racial-Profiling-Arrests/x4p3-hj3y): "As needed"
[Guide 2018 - Racial Profiling](https://data.austintexas.gov/Public-Safety/GUIDE-2018-Racial-Profiling/mipf-8at9): Not documented
[2018 Annual Crime](https://data.austintexas.gov/Public-Safety/2018-Annual-Crime/pgvh-cpyq): Not documented.
[Officer Involved Shootings 2008-2017](https://data.austintexas.gov/Public-Safety/Officer-Involved-Shootings-2008-17-Incidents/uzqv-9uza): "As needed"
[2008-17 OIS (officer_involved_shooting) Subjects](https://data.austintexas.gov/Public-Safety/2008-17-OIS-Subjects/u2k2-n8ez): "As needed"
[R2R 2010](https://data.austintexas.gov/Public-Safety/R2R-2010/q5ym-htjz): "As needed"
[Hate Crimes 2020](https://data.austintexas.gov/Public-Safety/Hate-Crimes-2020/mi2a-twn5): "As needed"
[R2R 2017](https://data.austintexas.gov/Public-Safety/2017-R2R-Dataset/5evd-3tba): Not documented
[R2R SUBJECTS 2017](https://data.austintexas.gov/dataset/2017-R2R-Subjects/5w6q-adh8): Not documented
[2016 RP Citations](https://data.austintexas.gov/Public-Safety/2016-RP-Citations/urfd-wng9): "As needed"
[R2R 2011](https://data.austintexas.gov/Public-Safety/R2R-2011/jipa-v8m5): "As needed"
[2014 Racial Profiling Arrests](https://data.austintexas.gov/Public-Safety/2014-Racial-Profiling-Arrests/fk9e-2udt): "As needed"
[R2R 2012](https://data.austintexas.gov/Public-Safety/R2R-2012/bx9w-y5sd): "As needed"
[2018 RP Citations](https://data.austintexas.gov/Public-Safety/2018-RP-Citations/b9rk-dixy): Not documented
[2017 racial_profiling Warning + Field Observations](https://data.austintexas.gov/Public-Safety/2017-Racial-Profiling-Warnings-Field-Observations/5asp-dw2k): "As needed"
[Crime reports 2015](https://data.austintexas.gov/Public-Safety/Crime-Reports-2015/g3bw-w7hh): "Weekly"
[2019 Discharge of a Firearm against dog](https://data.austintexas.gov/Public-Safety/2019-Discharge-of-a-Firearm-Against-a-Dog/9qgn-zgva): Not documented
[GUIDE 2017 - RP](https://data.austintexas.gov/Public-Safety/GUIDE-2017-RP/tud4-5x9v): "As needed"
[Hate Crimes 2019](https://data.austintexas.gov/Public-Safety/Hate-Crimes-2019/e3qf-htd9): Not documented
[2018 RP Warnings + Field Observations](https://data.austintexas.gov/Public-Safety/2018-RP-Warnings-Field-Observations/vchc-c622): Not documented

## Legal

From: https://data.austintexas.gov/Public-Safety/2016-Annual-Crime-Data/8iue-zpf6:

> 1. The data provided is for informational use only and is not considered official APD crime data as in official Texas DPS or FBI crime reports.
> 2. APD’s crime database is continuously updated, so reports run at different times may produce different results. Care should be taken when comparing against other reports as different data collection methods and different data sources may have been used.
> 3. The Austin Police Department does not assume any liability for any decision made or action taken or not taken by the recipient in reliance upon any information or data provided.

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
* Race/
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
