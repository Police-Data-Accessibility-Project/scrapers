# CKAN Scraper

## Introduction

This scraper can be used to retrieve package information from CKAN, which hosts open data projects such as <https://data.gov/>

The scraper's functions can be found in `ckan_scraper.py`.

A template can be found in the `template` folder.

## Definitions

* `Package` - Also called a dataset, is a page containing relevant information about a dataset. For example, this page is a package: <https://catalog.data.gov/dataset/electric-vehicle-population-data>.
* `Collection` - A grouping of child packages, related to a parent package. This is seperate from a group.
* `Group` - Also called a topic, is a grouping of packages. Packages in a group do not have a parent package. Groups can also contain subgroups.
* `Organization` - Organizations are what the data in packages belong to, such as "City of Austin" or "Department of Energy". Organization types are groups of organizations that share something in common with each other.

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

*NOTE: Some hosts use a different base URL for API requests. For example, Canada's Open Government Portal can be found at <https://search.open.canada.ca/opendata/> while the API access link is <https://open.canada.ca/data/en/api/3/action/package_search> as described in their [Access our API](https://open.canada.ca/en/access-our-application-programming-interface-api) page*

## Documentation

`ckan_package_search(base_url: str, query: Optional[str], rows: Optional[int], start: Optional[int], **kwargs) -> list[dict[str, Any]]`

Searches for packages (datasets) in a CKAN data portal that satisfies a given search criteria.

### Parameters

* **base_url** - The base URL to search from. e.g. "https://catalog.data.gov/"
* **query (optional)** - The keyword string to search for. e.g. "police". Leaving empty will return all packages in the package list.
* **rows (optional)** - The maximum number of results to return. Leaving empty will return all results.
* **start (optional)** - Which result number to start at. Leaving empty will start at the first result.
* **kwargs (optional)** - Additional keyword arguments. For more information on acceptable keyword arguments and their function see <https://docs.ckan.org/en/2.10/api/index.html#ckan.logic.action.get.package_search>

### Return

The function returns a list of dictionaries containing matching package results.

---

`ckan_group_package_show(base_url: str, id: str, limit: Optional[int]) -> list[dict[str, Any]]`

Returns a list of CKAN packages that belong to a particular group.

* **base_url** - The base URL of the CKAN portal. e.g. "https://catalog.data.gov/"
* **id** - The group's ID. This can be retrieved by searching for a package and finding the "id" key in the "groups" key.
* **limit** - The maximum number of results to return, leaving empty will return all results.

### Return

The function returns a list of dictionaries representing the packages associated with the group.

---

`ckan_collection_search(base_url: str, collection_id: str) -> list[Package]`

Returns a list of CKAN package information that belong to a collection. When querying the API, CKAN data portals are supposed to have relationships returned along with the rest of the data. However, in practice not all data portals have it set up this way. Since child packages are not able to be queried directly, they will not show up in any search results. To get around this, this function will manually scrape the information of all child packages related to the given parent.

* **base_url** - The base URL of the CKAN portal before the collection ID. e.g. "https://catalog.data.gov/dataset/"
* **collection_id** - The ID of the parent package. This can be found by querying the parent package and using the "id" key, or by navigating to the list of child packages and looking in the URL. e.g. In <https://catalog.data.gov/dataset/?collection_package_id=7b1d1941-b255-4596-89a6-99e1a33cc2d8> the collection_id is "7b1d1941-b255-4596-89a6-99e1a33cc2d8"

### Return

List of Package objects representing the child packages associated with the collection.
