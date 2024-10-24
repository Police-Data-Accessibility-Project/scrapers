# CKAN Scraper

## Introduction

This scraper can be used to retrieve package information from CKAN, which hosts open data projects such as <https://data.gov/>

The scraper's functions can be found in `ckan_scraper.py`.

A template can be found in the `template` folder.

## Setup

1. In a terminal, navigate to the CKAN scraper folder
    ```cmd
    cd scrapers_library/data_portals/ckan/
    ```
2. Create a Python virtual environment
    ```cmd
    python -m venv venv
    ```
3. Install the requirements
    ```cmd
    pip install -r requirements.txt
    ```
4. Copy the template script to another desired directory. Edit the template as needed. Then, run the scraper
    ```cmd
    python [script name]
    ```

## How can I tell if a website I want to scrape is hosted using CKAN?

There's no easy way to tell, some websites will reference CKAN or link back to the CKAN documentation while others will not. There doesn't seem to be a database of all CKAN instances either.

The best way to determine if a data catalog is using CKAN is to attempt to query its API. To do this:

1. In a web browser, navigate to the website's data catalog (e.g. for data.gov this is at <https://catalog.data.gov/dataset/>)
2. Copy the first part of the link (e.g. <https://catalog.data.gov/>)
3. Paste it in the browser's URL bar and add `api/3/action/package_search` to the end (e.g. <https://catalog.data.gov/api/3/action/package_search>)

*NOTE: Some hosts use a different base URL for API requests. For example, Canada's Open Government Portal can be found at <https://search.open.canada.ca/opendata/> while the API access link is <https://open.canada.ca/data/en/api/3/action/package_search> as described on their [Access our API](https://open.canada.ca/en/access-our-application-programming-interface-api) page*

## Documentation

`ckan_package_search(base_url: str, query: Optional[str], rows: Optional[int], start: Optional[int], **kwargs) -> list[dict[str, Any]]`

Searches for packages in a CKAN data portal that satisfies a given search criteria.

### Parameters

* **base_url** - The base URL to search from. e.g. "https://catalog.data.gov/"
* **query (optional)** - The keyword string to search for. e.g. "police". Leaving empty will return all packages in the package list.
* **rows (optional)** - The maximum number of results to return. Leaving empty will return all results.
* **start (optional)** - Which result number to start at. Leaving empty will start at the first result.
* **kwargs (optional)** - Additional keyword arguments. For more information on acceptable keyword arguments and their function see <https://docs.ckan.org/en/2.10/api/index.html#ckan.logic.action.get.package_search>

### Return

The function returns a list of dictionaries containing matching package results.
