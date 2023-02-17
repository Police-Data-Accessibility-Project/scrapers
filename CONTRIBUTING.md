# Write a data scraper

## Overview

Your goal is to submit a data scraper and a sample data file. For example, you could be using Python to turn a PDF of police activities into JSON, or making recurring API calls to pull down files.

### Best practices

- It's [legal](https://docs.pdap.io/meta/legal/legal-data-scraping). Collecting public records from the internet is not problematic in itself, but respecting data publishers wherever possible is a good way to ensure data stays accessible.

### Best Practices

- Scrapers are self-contained; when they're run, data should be saved locally or in their own GitHub repo.
- Populate the `README` for your scraper with as much helpful information as you can, including steps to setup and run the code.
- Include a truncated version of some sample data so we understand what is generated.
- Stick to the format of `USA/$STATE/$COUNTY/$MUNICIPALITY/$RECORD_TYPE`. If there is no specific county or municipality, you can skip those.

# Get started

## 0. Decide where the scraper should live.

[//]: # (How should we have people contact us if they want a scraper to live in its own PDAP repo? And other than knowing the use case, what else do we need to know so we can communicate that up front?)
You can add a scraper to our repo, or create your own. Or help us understand why we should maintain it in a separate repo that also includes automated data collection, such as via [GitHub Actions](https://docs.github.com/en/actions). Regardless, we'll add it to our list so people can find and use it.

Scrapers repo | Standalone repo
--- | ---
No specific or immediate need to capture the data repeatedly or on a rolling basis | The data disappears often or is overwritten, or there's a specific request to use the data collected
Best for people choosing to do things "the PDAP way" | Best if you have strong opinions about your project's structure, license, or usage
May reference common utilities | Does not reference common utilities
Best for simple scrapers and common data portals | Best for complicated projects involving multiple Data Sources
Scrapers only: no analysis, aggregation, messaging | Whatever you want
The PDAP community has a responsibility to maintain your work | Maintenance is at your discretion
Best for Data Sources which people may want to scrape at any time | Best for creating a complete package of useful data which may not be updated further


## 1. Find a Data Source to scrape.

Browse our [Data Sources](https://docs.pdap.io/activities/data-sources/explore-data-sources) and find a source to scrape. If the source you want to scrape isn't there, please let us know as part of your submission or [add it yourself](https://docs.pdap.io/activities/data-sources/contribute-data-sources). Filling in that form usually takes less than 5 minutes.


## 2. Get set up locally.

1. Clone this repository. [Don't know how?](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)
2. Optionally, `cd` into the `/setup_gui` directory.

[//]: # (Have we made a decision about whether to continue including the GUI stuff here? If there's already a build-and-copy step, giving it its own home feels right to me. Most contributors, based on the type of interest we've gotten, don't seem to need it)
3. Follow through the GUI.
   - Mac: run the script with `python3 ScraperSetup.py`
   - Windows: run the executable by double-clicking it.
   - [@Pythonidaer](https://github.com/Pythonidaer/pythonidaer) made an [excellent walkthrough of the GUI as of the v0.0.1 release](https://www.youtube.com/watch?v=oJxXkSytreE).
4. Copy the resulting folder into your clone of `PDAP-Scrapers`.

## 3. Check our provided examples and utilities for helpful assets and scrapers before you start.

Why start from scratch if we have a useful library? Keep in mind that you -- or we! -- we can always refactor your work later if necessary, so if you're not sure, we still want you to submit!

[//]: # (Not gonna lie, writing some templates/examples is gonna be fun)
Not sure where to start with a page you want to scrape? Check our examples and templates to see if we have that covered. If you see use cases we're missing, open an issue or contribute it yourself.

## 4. Code your scraper and make a Pull Request!

[//]: # (Should we be clearer about process here? Do we just want a PR or do we want a branch, maybe with a naming convention, and some suggestions of what should be included in the PR -- such as recommended steps for testing?)
The most important thing here is that your scraper is grabbing public criminal legal records, and is [legal](https://docs.pdap.io/meta/legal/legal-data-scraping).

# FAQ

> What kind of data are we scraping?

Police data that's already made public by a government agency. The [data sources listed here](https://airtable.com/shrUAtA8qYasEaepI) can be a to-do list. If you're not sure where to start, [read more here](https://docs.pdap.io/activities/data-scraping/our-approach-to-scraping).

> What languages are allowed?

To this point we've been working in Python. If you'd like to contribute and prefer to work in another language, that's fine. Just be sure to note that in your `README` along with any setup steps to get your contribution running.

> Are there any specific formatting guidelines I should adhere to?

For now, if you use Python: Try to stick with PEP8 formatting. A good formatter for this is [Black](https://github.com/psf/black).
