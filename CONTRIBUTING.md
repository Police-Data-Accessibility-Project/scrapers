# Help liberate data

## How can you contribute?

One option: Submit a data scraper and a sample data file. For example, you could use Python to turn a PDF of police training records into JSON, or make recurring API calls to pull down files, or toss resulting data into a SQLite database.

Other options: Improve or fix existing scrapers, add tests, extend helpers and utilities, submit a version of an existing scraper in a new language, or write scraper examples or templates to cover use cases we haven't yet gotten to.

### Best practices

- It's [legal](https://docs.pdap.io/meta/legal/legal-data-scraping). Collecting public records from the internet is not problematic in itself, but respecting data publishers wherever possible is a good way to ensure data stays accessible.
- Scrapers are self-contained; when they're run, data should be saved locally or in their own GitHub repo.
- Populate the `README` for your scraper with as much helpful information as you can, including steps to setup and run the code.
- Include a truncated version of some sample data so we understand what is generated.

You can read more about our philosophy and priorities around scraping [here](https://docs.pdap.io/activities/data-scraping/our-approach-to-scraping).

# Get started

## 1. Find a Data Source to scrape.

What question are you trying to answer? What kind of data are you trying to help people use or preserve?

You can browse our [Data Sources](https://docs.pdap.io/activities/data-sources/explore-data-sources) and find a source to scrape. If the source you want to scrape isn't there, please let us know as part of your submission or [add it yourself](https://docs.pdap.io/activities/data-sources/contribute-data-sources). Filling in that form usually takes less than 5 minutes.

## 2. Decide where a new scraper should live.

You can add a scraper to our collection, or create your own within your personal GitHub space.

If you'd like PDAP to host it, there are two options.

You can contribute it here, following our conventions, and people can find and use it as they please. Please stick to the format of `USA/$STATE/$COUNTY/$MUNICIPALITY/$RECORD_TYPE`. If there is no specific county or municipality, it can live in the most relevant higher-level directory.

Or, if there's a compelling reason to have it running regularly -- there's a specific request to use the data, say, or the data gets overwritten periodically -- help us understand that. We will consider hosting it in a separate PDAP repo that also includes automated data collection, such as via [GitHub Actions](https://docs.github.com/en/actions).

Regardless of which way you'd like to go, we'll add it to our list so people can find and use it.

A few ways to think about whether PDAP is the right home for your scraper:

Scrapers repo | Standalone repo
--- | ---
No specific or immediate need to capture the data repeatedly or on a rolling basis | The data disappears often or is overwritten, or there's a specific request to use the data collected
Best for people choosing to do things "the PDAP way" | Best if you have strong opinions about your project's structure, license, or usage
May reference common utilities | Does not reference common utilities
Best for simple scrapers and common data portals | Best for complicated projects involving multiple Data Sources
Scrapers only: no analysis, aggregation, messaging | Whatever you want
Easier to find when people look for tools around police data | Less visible, but more control
Best for Data Sources which people may want to scrape at any time | Best for creating a complete package of useful data which may not be updated further

## 3. Get set up locally.

- Clone this repository. [Don't know how?](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)

## 4. Check our provided examples and utilities for helpful assets and scrapers before you start.

Why start from scratch if we have a useful library? Keep in mind that you -- or we! -- can always refactor your work later if necessary, so if you're not sure, we still want you to submit!

[//]: # (Not gonna lie, writing some templates/examples is gonna be fun)
Not sure where to start with a page you want to scrape? Check our examples and templates to see if we have that covered. If you see use cases we're missing, open an issue or (please and thank you) contribute it yourself.

## 5. Code your scraper and make a Pull Request!

The most important thing here is that your scraper is grabbing public criminal legal records, and is [legal](https://docs.pdap.io/meta/legal/legal-data-scraping).

Beyond that, a PR for a new scraper should:
- Be based on a new branch
- Contain a detailed `README` which includes steps for setup and for running the code in addition to helpful information about the data being collected
- Include recommended steps for testing (we'll poke at it other ways, too, but it's always nice to have a place to start)

[//]: # (Later, when we have some of our own testing tools, this will include that step, too)


# FAQ

> What kind of data are we scraping?

Police data that's already made public by a government agency. The [data sources listed here](https://airtable.com/shrUAtA8qYasEaepI) can be a to-do list. If you're not sure where to start, [read more here](https://docs.pdap.io/activities/data-scraping/our-approach-to-scraping).

> What languages are allowed?

To this point we've been working in Python. If you'd like to contribute and prefer to work in another language, that's fine. Just be sure to note that in your `README` along with any setup steps to get your contribution running.

> Are there any specific formatting guidelines I should adhere to?

For now, if you use Python: Try to stick with PEP8 formatting. A good formatter for this is [Black](https://github.com/psf/black).
