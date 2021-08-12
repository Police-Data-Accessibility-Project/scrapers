# Write a data scraper

## Overview

You’re going to program a [legal data scraper](https://docs.pdap.io/meta/legal/legal-data-scraping) and process a sample data file. For example, you could be using Python to turn a PDF of police activities into JSON, or making recurring API calls to pull down files.

### Requirements

- It's [legal](https://docs.pdap.io/meta/legal/legal-data-scraping).

### Best Practices
- We can run the scraper by running one script, called `scraper.py` or at least beginning `scraper-`
- Populate the readme for your scraper with as much helpful information as you can!
- The config file appropriately references a dataset.
- Include a truncated version of some sample data so we understand what is generated.
- Ensure you have a `schema.json` file & a blank `etl.py` file in your scraper directory, and call `import etl` at the end of your scraper! This will hook into our ETL process once we get further along.
- Stick to the format of `USA/$STATE/$COUNTY/$RECORD_TYPE`.

## 1. Find a dataset to scrape.

Navigate to our [Dataset Catalog](https://www.dolthub.com/repositories/pdap/datasets) and find a source to scrape. It's likely you will need to [add the dataset yourself](https://docs.pdap.io/components/data-collection/dataset-catalog/submit-or-update-datasets). This takes about 5–10 minutes. 


## 2. Get set up locally.

1. Clone this repository. [Don't know how?](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)
2. `cd` into the `/setup_gui` directory.
3. Install dependencies. `pip install -r requirements.txt`
4. Follow through the GUI. You can either run the script directly `python3 scraper_setup.py`, or run the executable by double clicking it.
5. Copy the resulting folder into your clone of `PDAP-Scrapers`.

## 3. Check the `common` folder for helpful assets before you start. 

Why start from scratch if we have a useful library? Keep in mind that we can always refactor your work later if necessary, so if you're not sure, we still want 
you to submit!

## 4. Code your scraper and make a Pull Request!
The most important thing here is that your scraper is grabbing public police data, and is [legal](https://docs.pdap.io/meta/legal/legal-data-scraping).


# FAQ

> What kind of data are we scraping?

Police data that's already made public by a government jurisdiction.

> What languages are allowed?

Python is preferred. If you use another language, we may not be able to easily fold it into our infrastructure.

> Are there any specific formatting guidelines I should adhere to?

For now, if you use Python: Try to stick with PEP8 formatting. A good formatter for this is [Black](https://github.com/psf/black).

