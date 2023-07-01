 SiteMap Scraper
==============================

This is a general scraper for a list of host URLs, which finds the `hostURL/sitemap.xml`
and finds/stores all the url-routes that have specific words in them. (Currently
only `.us` and `.gov`, see further improvements below.)

Getting Started
------------
Navigate to the base directory here, `PDAP-Scrapers/common/utils/sitemap_scraper/`.

In Mac/Linux, create a new virtual environment and activate it.

```
$python3 -m venv venv
$source venv/bin/activate
(venv) $
```

Now install the required python libraries:

```commandline
$pip install -r requirements.txt
```

Be sure that your list of host URLs is available and contains the URLs you wish to scrape. 
There is a sample list of URLs provided here: 
`PDAP-Scrapers/common/utils/sitemap_scraper/sample_host_sites.txt`

Which looks like:

```text
https://www.in.gov
https://www.indiancreekvillagefl.gov
https://www.indianolams.gov
https://www.indy.gov
...
```

It is a newline delimited text file containing host URLs to start scraping.

To start scraping the sitemaps- run:

`$python updated_sitemap_spider.py`

You'll then find the output located in the base directory (`sitemap_scraper/`) which looks like

`sitemap_scraper/<datetime>_output.csv`

Project Organization
------------

Files of note:

 - `../sitemap_scraper/requirements.txt` - Python library requirements for this sitemap scraper
 - `../sitemap_scraper/sample_host_sites.txt` - initial sample of host domains to run. Replace this file with your list of host domains.
 - `../sitemap_scraper/updated_sitemap_spider.py` - Actual logic for scraping.

Resources
---------

 - [PDAP Discord Link](https://discord.gg/5xAEFjyN)
   - Discord thread pertaining to this work: [Discord Thread Link](https://discord.com/channels/828274060034965575/1036848253083340841)
 - [PDAP Documentation](https://docs.pdap.io/readme)

Purpose & Next Steps
----------------

If we can find a list of relevant URL domains that may contain Police or Cop related web pages,
this project is meant to find them. Initially, we queried the Common Crawl URLs for 
`*.gov` and `*.us` websites that have the words police in them. From these, we deduplicated
and filtered down to about 2,000 relevant government websites (local sites, county sites,
and state sites). A vast majority of these URL domains have sitemap.xml files. This scraper
is meant to search all of those sitemaps.

Next:
- We plan to identify with each URL:
  - Agency Identification & Demographic level. E.g. "Las Vegas, NV", "Local Metro"
  - Record Type: URL is a type from a list. E.g. "Incident List", "Staffing", etc.
  - Any other relevant information.


Limitations
-----------

The URLs we used for this project came from limiting to URLs that use `.us` or `.gov`
domains. This can be limiting to what we can find. We're open to ideas to improve this.

Sitemap exploration is limited to only URLs that have keywords: `.us` or `.gov`.
This is a big limitation. There are many URL routes on a server that can be very highly
relevant but not contain those words. We will have to expand past sitemap scraping into
actual webpage scraping to get past this. E.g. if we find the police department homepage:
(`http://metrocity.state.gov/police`), then most of the URLs off that site would be related
to the police.
