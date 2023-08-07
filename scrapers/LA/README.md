## Run the scraper.

To run an editor:
1. `cd` into the `/scrapers/LA/scraper-la-jails` directory.
2. Run the command `python scraper-la-jails/spiders` to start the scraper. The data will save to a csv file in the `/scrapers/LA/data/la_jail_data` directory 

To run in a venv:

`virtualenv scraper-la-jails`
`source scraper-la-jails/bin/activate`
`pip install scrapy`


# Source info
Data for each of the Parish (county) jails are published online by the agency. The urls for each agency can be found in the `/scrapers/LA/data/urls` directory 

# Fields collected:

* arresting_agency_url
* inmate_race
* inmate_sex
* inmate_date_of_arrest
