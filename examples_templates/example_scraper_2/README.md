# Source Info

Copied and modified from `/scrapers/CA/humboldt_county/arcata/cal_poly_humboldt`

cd into `/example_scraper_2/` and run `humboldt_daily_scraper.py` to see how it works!

Scrapes daily crime/fire log from the Cal Poly Humbolt Police Department

## Data source location

Main page: https://police.humboldt.edu/ > Top horizontal menu bar, furthest to the right, HSU Crime Map

## Data refresh rate

Daily

## Legal

>This website is provided as a public service by the Humboldt State University Police Department. In an effort to protect victim privacy this website does not provide information regarding juvenile offenders, or specific information regarding calls for service that are sensitive in nature. The Department does not guarantee the accuracy, completeness, or timeliness of the information contained on this website regarding specific incidents, crimes, or people with respect to the omission of information that may have not yet been filed or is pending filing with a court of jurisdiction relating to criminal offenses.

## Fields being collected:

* `Nature`: Nature of incident
* `Case/Incident #`
* `Reported`: Time incident reported
* `Occurred`: Time incident occurred
* `Location`
* `Disposition`: Action taken by authorities

## Sample response

See `./data` folder
