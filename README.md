# Police Data Accessibility Project Scrapers
This repo contains the data scrapers for [Police Data Accessibility Project](https://pdap.io). Thank you for being here!

# How to run a scraper
Right now, this requires some Python knowledge and patience. We're in the early stages: there's no automated scraper farm or fancy GUI yet.

1. Install Python.
2. [Clone this repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
3. Find the scraper you wish to run. These are sorted geographically, so start by looking in `/USA/...`.
4. Run the `scraper.py` file with something like `python3 <scraper path>` depending on how you  installed it.

## Did it work?
If it worked, discuss your findings in our [Discord](https://discord.gg/wMqex8nKZJ). If it didn't, make an issue in this repo or reach out in Discord.

# How to contribute
To write a scraper, start with [CONTRIBUTING.md](https://github.com/Police-Data-Accessibility-Project/PDAP-Scrapers/blob/main/CONTRIBUTING.md). Be sure to check out the [/common folder](https://github.com/Police-Data-Accessibility-Project/PDAP-Scrapers/tree/main/common/)!

For everything else, start with [docs.pdap.io](https://docs.pdap.io/).

## What data are we scraping?
The [data sources listed here](https://www.dolthub.com/repositories/pdap/datasets/query/master?q=SELECT+*%0AFROM+%60datasets%60%0Awhere+status_id+%3D+1%0A%0A&active=Tables) are our to-do list. If we should targeting a new data type, suggest it in Discord or make a DoltHub PR!

## Resources
Potentially useful tools. If you find something useful, or if one of these is out of date, make a PR!
- https://www.scrapingbee.com/
- https://github.com/CJWorkbench/cjworkbench
