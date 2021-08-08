# Resources
Check out `/base_scripts`, `/common`, and `/starter_template` for a head start.

# Write a data scraper

## Overview

You’re going to program a [legal data scraper](https://docs.pdap.io/meta/legal/legal-data-scraping) and process a sample data file. For example, you could be using Python to turn a PDF of police activities into JSON, or making recurring API calls to pull down files.

### Find a dataset to scrape.

Navigate to our [Dataset Catalog](https://www.dolthub.com/repositories/pdap/datasets) and find a source to scrape. It's likely you will need to [add the dataset yourself](https://docs.pdap.io/components/data-collection/dataset-catalog/submit-or-update-datasets). This takes about 5–10 minutes. 


### Get set up locally.

Clone the [Scrapers repo](https://github.com/Police-Data-Accessibility-Project/Scrapers). Make a copy of the `template` folder in the appropriate jurisdiction folder.

### Code your scraper.

The most important thing here is that your scraper is grabbing public police data, and is [legal](https://docs.pdap.io/meta/legal/legal-data-scraping).

#### Scraper requirements

1. It's [legal](https://docs.pdap.io/meta/legal/legal-data-scraping).
2. The config file appropriately references a dataset.
3. Include a truncated version of some sample data so we understand what is generated.
4. Ensure you have a `schema.json` file & a blank `etl.py` file in your scraper directory, and call `import etl` at the end of your scraper! This will hook into our ETL process once we get further along.

Your submission doesn't need to be set up to recur. We can handle that when we run it periodically!

#### Scalability

Check the `common` folder for helpful assets, and be sure to add your own as you work to keep things scalable. Try not to repeat yourself—but keep in mind that we can always refactor your work later if necessary.

#### Readme

The best way to be a good PDAP citizen is to populate the readme for your scraper with as much helpful information as you can!

#### Structure

Stick to the format of `USA/$STATE/$COUNTY/$RECORD_TYPE`. If there are state-level records being scraped, use `USA/$STATE/_State/$RECORD_TYPE`. Use underscores rather than spaces or dashes.

### Submit your work.

Make a PR and request approval from the \#scrapers Slack channel!

## Scraper FAQ

> What kind of data are we scraping?

Police data that's already made public by a government jurisdiction.

> What languages are allowed?

Python is preferred. If you use another language, we may not be able to easily fold it into our infrastructure.

> Are there any specific formatting guidelines I should adhere to?

For now, if you use Python: Try to stick with PEP8 formatting. A good formatter for this is [Black](https://github.com/psf/black).

