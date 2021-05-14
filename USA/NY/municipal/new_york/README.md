This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
[Complaint Map](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Current-Year-To-Date-/5uac-w243/data): Quarterly, (not really complaints, more like crime data)
## Legal
Include the Terms of Service (or link to them). Is there anything else we should know?

# Fields to collect:
_Move these fields to the appropriate list below when you submit your scraper._
* CMPLNT_NUM
* ADDR_PCT_CD
* BORO_NM
* CMPLNT_FR_DT
* CMPLNT_FR_TM
* CMPLNT_TO_DT
* CMPLNT_TO_TM
* CRM_ATPT_CPTD_CD
* HADEVELOPT
* HOUSING_PSA
* JURISDICTION_CODE
* JURIS_DESC
* KY_CD
* LAW_CAT_CD
* LOC_OF_OCCUR_DESC
* OFNS_DESC
* PARKS_NM
* PATROL_BORO
* PD_CD
* PD_DESC
* PREM_TYP_DESC
* RPT_DT
* STATION_NAME
* SUSP_AGE_GROUP
* SUSP_RACE
* SUSP_SEX
* TRANSIT_DISTRICT
* VIC_AGE_GROUP
* VIC_RACE
* VIC_SEX
* X_COORD_CD
* Y_COORD_CD
* Latitude
* Longitude
* Lat_Lon
* New Georeferenced Column


## Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.
