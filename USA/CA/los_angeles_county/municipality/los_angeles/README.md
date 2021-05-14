This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
* [Calls for service 2019](https://data.lacity.org/Public-Safety/LAPD-Calls-for-Service-2019/r4ka-x5je): weekly (likely not)
* [Crime Data from 2010-2019](https://data.lacity.org/Public-Safety/Crime-Data-from-2010-to-2019/63jg-8b9z): weekly (likely not)
* [Arrest data from 2010-19](https://data.lacity.org/Public-Safety/Arrest-Data-from-2010-to-2019/yru6-6re4): weekly (likely not)
* [Crime data from 2020 to present](https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8): Weekly
* [Vehicle and Ped Stop 2010-present](https://data.lacity.org/Public-Safety/Vehicle-and-Pedestrian-Stop-Data-2010-to-Present/ci25-wgt7): Weekly
* [CFS 2014](https://data.lacity.org/Public-Safety/LAPD-Calls-for-Service-2014/mgue-vbsx): "Weekly", (not really)
* [Arrests 2020-present](https://data.lacity.org/Public-Safety/Arrest-Data-from-2020-to-Present/amvf-fr72): Weekly
* [CFS 2020](https://data.lacity.org/Public-Safety/LAPD-Calls-for-Service-2020/84iq-i2r6): Weekly, (likely not)
* [Map of drug possesion 2010-2019 (based on arrest data)](https://data.lacity.org/Public-Safety/Map-of-drug-possession-charges/isxh-ztfe): probably weekly, but not really
* [CFS 2010](https://data.lacity.org/Public-Safety/LAPD-Calls-for-Service-2010/iy4q-t9vr): weeklky, but not really
* [CFS 2015](https://data.lacity.org/Public-Safety/LAPD-Calls-for-Service-2015/tss8-455b): monthly, but not really
* [Annual High Level Metrics GOVSTAT](https://data.lacity.org/Public-Safety/LAPD-Annual-High-Level-Metrics-GOVSTAT-Archived/t6kt-2yic): "Other", (probably never)
* [CFS 2013](https://data.lacity.org/Public-Safety/LAPD-Calls-for-Service-2013/urhh-yf63): "Weekly", (never)
* [All Stations Response Metrics](https://data.lacity.org/Public-Safety/All-Stations-Response-Metrics/kszm-sdw4): Archived (never)
* [CFS 2017](https://data.lacity.org/Public-Safety/LAPD-Calls-for-Service-2017/ryvm-a59m): "Weekly", (never)
* [CFS 2011](https://data.lacity.org/Public-Safety/LAPD-Calls-for-Service-2011/4tmc-7r6g): "Weekly", (never)
* [Citywide response metrics](https://data.lacity.org/Public-Safety/Citywide-Response-Metrics-Updated/kcsj-s69p): Monthlys
* [CFS 2016](https://data.lacity.org/Public-Safety/LAPD-Calls-for-Service-2016/xwgr-xw5q): "Weekly", (never)
* [CFS 2021](https://data.lacity.org/Public-Safety/LAPD-Calls-for-Service-2021/cibt-wiru): Weekly
* [All stations response metrics 2014](https://data.lacity.org/Public-Safety/All-Stations-Response-Metrics-2014/y2p7-8ckf): probably never
* [Citywide response metrics 2015](https://data.lacity.org/Public-Safety/Citywide-Response-Metrics-2015/jk5m-4dqg): Probably never
* [Citywide response metrics 2016](https://data.lacity.org/Public-Safety/Citywide-Response-Metrics-2016/8d58-axgy): Probably never
* [citwide response metrics](https://data.lacity.org/Public-Safety/Citywide-Response-Metrics/adam-59ei): ARchived
* [All stations repsonse metrics 2015](https://data.lacity.org/Public-Safety/All-Stations-Response-Metrics-2015/if3i-rtyg): Archived
* [CFS 2018](https://data.lacity.org/Public-Safety/LAPD-Calls-for-Service-2018/nayp-w2tw): "Weekly", probably never
* [Citywide response metrics 2017](https://data.lacity.org/Public-Safety/Citywide-Response-Metrics-2017/t69g-g3uk):
* [all stations response metrics 2013](https://data.lacity.org/Public-Safety/All-Stations-Response-Metrics-2013/x88u-8etg): probably never
* [CFS 2012](https://data.lacity.org/Public-Safety/LAPD-Calls-for-Service-2012/i7pm-cnmm): Probably nevers
* [All stations response metrics 2016](https://data.lacity.org/Public-Safety/All-Stations-Response-Metrics-2016/ieyn-ppaw): Archived
* [All stations response metrics 2017](https://data.lacity.org/Public-Safety/All-Stations-Response-Metrics-2017/rub2-5ih6): ARchived
* [Citywide response metrics 2014](https://data.lacity.org/Public-Safety/Citywide-Response-Metrics-2014/txgp-mc85): Archived



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
