# Write a data scraper

## Overview

Your goal is to submit a data scraper and a sample data file. For example, you could be using Python to turn a PDF of police activities into JSON, or making recurring API calls to pull down files.

### Best practices

- It's [legal](https://docs.pdap.io/meta/legal/legal-data-scraping). Collecting public records from the internet is not problematic in itself, but respecting the wishes of data publishers wherever possible is a good way to ensure data stays accessible.

### Best Practices

- Scrapers are self-contained; when they're run, data should be saved locally or in their own GitHub repo.
- Populate the readme for your scraper with as much helpful information as you can.
- Include a truncated version of some sample data so we understand what is generated.
- Stick to the format of `USA/$STATE/$COUNTY/$MUNICIPALITY/$RECORD_TYPE`. If there is no specific county or municipality, you can skip those.

# Get started

## 0. Decide where the scraper should live.

You can add a scraper to our repo, or create your own. Either way, we'll add it to our database so people can find and use it.

Scrapers repo | Standalone repo
--- | ---
Best for beginners doing things "the PDAP way" | Best if you have strong opinions about your project's structure, license, or usage
May reference common utilities | Does not reference common utilities
Best for simple scrapers and common data portals | Best for complicated projects involving multiple Data Sources
Scrapers only: no analysis, aggregation, messaging | In addition to a web scraper, you can publish analysis of your results
The PDAP community has a responsibility to maintain your work | Maintenance is at your discretion
Best for Data Sources which people may want to scrape at any time | Best for creating a complete package of useful data which may not be updated further


## 1. Find a Data Source to scrape.

Browse our [Data Sources](https://docs.pdap.io/activities/data-sources/explore-data-sources) and find a source to scrape. If the source you want to scrape isn't there, please let us know as part of your submission or [add it yourself](https://docs.pdap.io/activities/data-sources/contribute-data-sources). Filling in that form usually takes under 5 minutes. 


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

# FAQ

> What kind of data are we scraping?

Police data that's already made public by a government jurisdiction. The [data sources listed here](https://airtable.com/shrUAtA8qYasEaepI) are our to-do list. If you're not sure where to start, [read more here](https://docs.pdap.io/activities/data-scraping/our-approach-to-scraping).

> What languages are allowed?

Python is preferred. If you use another language, we may not be able to easily fold it into our infrastructure.

> Are there any specific formatting guidelines I should adhere to?

For now, if you use Python: Try to stick with PEP8 formatting. A good formatter for this is [Black](https://github.com/psf/black).
