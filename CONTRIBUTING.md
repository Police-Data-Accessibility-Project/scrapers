# Write a data scraper

## Overview

You’re going to program a [legal data scraper](https://docs.pdap.io/meta/legal/legal-data-scraping) and process a sample data file. For example, you could be using Python to turn a PDF of police activities into JSON, or making recurring API calls to pull down files.

### Requirements

- It's [legal](https://docs.pdap.io/meta/legal/legal-data-scraping).

### Best Practices
- We can run the scraper by running one script, called `scraper.py` or at least beginning `scraper-`
- Populate the readme for your scraper with as much helpful information as you can!
- Include a truncated version of some sample data so we understand what is generated.
- Stick to the format of `USA/$STATE/$COUNTY/$MUNICIPALITY/$RECORD_TYPE`. If there is no specific county or municipality, you can skip those.

## 1. Find a Data Source to scrape.

Browse our [Data Sources](https://docs.pdap.io/activities/data-sources/explore-data-sources) and find a source to scrape. If the source you want to scrape isn't there, please [add it yourself](https://docs.pdap.io/activities/data-sources/contribute-data-sources). This should take under 5 minutes. 


## 2. Get set up locally.

1. Clone this repository. [Don't know how?](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)
2. Optionally, `cd` into the `/setup_gui` directory.
3. Follow through the GUI.
   - Mac: run the script with `python3 ScraperSetup.py`
   - Windows: run the executable by double clicking it.
   - [@Pythonidaer](https://github.com/Pythonidaer/pythonidaer) made an [excellent walkthrough of the GUI as of the v0.0.1 release](https://www.youtube.com/watch?v=oJxXkSytreE).
4. Copy the resulting folder into your clone of `PDAP-Scrapers`.

## 3. Check the `/common` `/Base_Scripts` folder for helpful assets and scrapers before you start.
[`/common` folder here!](https://github.com/Police-Data-Accessibility-Project/PDAP-Scrapers/tree/main/common/)
[`/Base_Scripts` folder here!](https://github.com/Police-Data-Accessibility-Project/PDAP-Scrapers/tree/main/Base_Scripts/Scrapers)

Why start from scratch if we have a useful library? Keep in mind that we can always refactor your work later if necessary, so if you're not sure, we still want you to submit!

## 4. Code your scraper and make a Pull Request!
The most important thing here is that your scraper is grabbing public criminal justice records, and is [legal](https://docs.pdap.io/meta/legal/legal-data-scraping).

Make sure you follow this guideline for creating folders:

```
COUNTRY/
  STATE/
    COUNTY/
      DEPARTMENT_TYPE
                (CITY)
                (COUNTY)
                (COLLEGE)
                (STATE)
                (FEDERAL)/
                    DEPARTMENT-X-NAME/
```


# FAQ

> What kind of data are we scraping?

Police data that's already made public by a government jurisdiction.

> What languages are allowed?

Python is preferred. If you use another language, we may not be able to easily fold it into our infrastructure.

> Are there any specific formatting guidelines I should adhere to?

For now, if you use Python: Try to stick with PEP8 formatting. A good formatter for this is [Black](https://github.com/psf/black).
