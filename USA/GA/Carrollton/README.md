This readme should give people everything they need to maintain the scraper.

# Summary
Time period of data (e.g. 06/01/2017 to 03/20/2021)

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

# How to locate the data source
Go to their [administration page](https://www.carrolltonpd.com/divisions/administration/), on the right side, "crime reports"


On the cityprotect website, select "Download crimemap data" and click go ![image](https://user-images.githubusercontent.com/40151222/112383242-40497780-8cc3-11eb-9445-6cf695f2449a.png)


Choose a report (doesn't matter)


![image](https://user-images.githubusercontent.com/40151222/112383296-548d7480-8cc3-11eb-8f44-6aef21de5daf.png)


With the networking tab open, click "download" (after accepting the data policy and terms). After clicking download, close the download prompt and look in the networking tab. The request will look something like this 


![image](https://user-images.githubusercontent.com/40151222/112383534-99191000-8cc3-11eb-873a-c1ee34401947.png)


An example request url is: https://cereplicatorprodcomm.blob.core.windows.net/mainblob/1423-10.2020-01.2021.csv?st=2021-03-24T21%3A08%3A22Z&se=2021-03-24T21%3A13%3A22Z&sp=r&sv=2018-03-28&sr=b&sig=%2FXuaM%2FHtueclub8li3oWGUTHCxcThpRVH62PlkTxaCk%3D


Strip the tracker, located after the `.csv`, leaving just
https://cereplicatorprodcomm.blob.core.windows.net/mainblob/1423-10.2020-01.2021.csv


The file name format is `police_code`-`start_month`.`start_year`-`end_month`.`end_year`, so
`police_code = 1423`


Scroll down to the bottom of the report list, and set [`start_year`](https://github.com/CaptainStabs/Scrapers/blob/master/USA/GA/Carrollton/carrollton_scraper.py#L14) to the lowest year of data available.


If the data is not current, comment out [line 200](https://github.com/CaptainStabs/Scrapers/blob/master/USA/GA/Carrollton/carrollton_scraper.py#L20), and close the block comment on [line 24](https://github.com/CaptainStabs/Scrapers/blob/master/USA/GA/Carrollton/carrollton_scraper.py#L24)


# Data refresh rate
Monthly up until the end of 2020

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.

# Legal
Is there anything specific to this jurisdiction we should know as we work?

# Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?
