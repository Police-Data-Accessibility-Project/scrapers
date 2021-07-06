# Conway Police Department

## Calls For Service

The calls for service information on the Conway PD site only covers the previous 10 days. Most of the files in the calls_for_service directory may be ignored. Files that may be of interest are

- _calls_for_service/spiders/conwaypd.py_
  - This is the logic for scraping the fields from the webpage after they are processed by the downloader middleware (which hasn't been changed in this project).
- _calls_for_service/settings.py_
  - The scraper can be configured in here, though most of these settings are unused. The only items changed from their defaults are the CONCURRENT_REQUESTS, set to 1, and ITEM_PIPELINES was changed to activate the ConwayPdPipeline.
- _calls_for_service/pipelines.py_
  - This contains the logic for the ConwayPdPipeline to dump the results to a JSON file.

### Getting started

---

From within the calls_for_service folder use:

```
scrapy crawl conwaypd
```

### Data refresh rate

---

Data in the list is updated continuously, usually multiple times per hour, but definitely multiple times per day.

### Sample response:

---

Sample data is saved to the service_calls.json file in the calls_for_service folder.

## Legal

### Original disclaimer:

---

"This information is not intended to be used as official crime data. This program does not provide information about all crimes, and excludes specific incidents such as sexual assaults and child abuse. The City of Conway Police Department makes every effort to produce and publish current and accurate information. No warranties, expressed or implied, are provided for the data herein, its use, or its interpretation. The services provided are for informational purposes only and should not be relied on for any type of legal action."
