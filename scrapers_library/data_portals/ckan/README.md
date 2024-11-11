# CKAN Scraper

## Introduction

This scraper can be used to retrieve package information from [CKAN](https://ckan.org/), which hosts open data projects such as <https://data.gov/>. CKAN API documentation can be found at <https://docs.ckan.org/en/2.9/api/>.

Running the scraper will output a list of packages to a CSV file using the search terms.

## Definitions

* `Package` - Also called a dataset, is a page containing relevant information about a dataset. For example, this page is a package: <https://catalog.data.gov/dataset/electric-vehicle-population-data>.
* `Collection` - A grouping of child packages, related to a parent package. This is seperate from a group.
* `Group` - Also called a topic, is a grouping of packages. Packages in a group do not have a parent package. Groups can also contain subgroups.
* `Organization` - Organizations are what the data in packages belong to, such as "City of Austin" or "Department of Energy". Organization types are groups of organizations that share something in common with each other.

## Files

* `scrape_ckan_data_portals.py` - The main scraper file. Running this will execute a search accross multiple CKAN instances and output the results to a CSV file.
* `search_terms.py` - The search terms and CKAN portals to search from.
* `ckan_scraper_toolkit.py` - Toolkit of functions that use ckanapi to retrieve packages from CKAN data portals.

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
4. Run the multi-portal CKAN scraper
    ```cmd
    python scrape_ckan_data_portals.py
    ```

## How can I tell if a website I want to scrape is hosted using CKAN?

There's no easy way to tell, some websites will reference CKAN or link back to the CKAN documentation while others will not. There doesn't seem to be a database of all CKAN instances either.

The best way to determine if a data catalog is using CKAN is to attempt to query its API. To do this:

1. In a web browser, navigate to the website's data catalog (e.g. for data.gov this is at <https://catalog.data.gov/dataset/>)
2. Copy the first part of the link (e.g. <https://catalog.data.gov/>)
3. Paste it in the browser's URL bar and add `api/3/action/package_search` to the end (e.g. <https://catalog.data.gov/api/3/action/package_search>)

*NOTE: Some hosts use a different base URL for API requests. For example, Canada's Open Government Portal can be found at <https://search.open.canada.ca/opendata/> while the API access link is <https://open.canada.ca/data/en/api/3/action/package_search> as described in their [Access our API](https://open.canada.ca/en/access-our-application-programming-interface-api) page*

Another way to tell is by looking at the page layout. Most CKAN instances have a similar layout to one another. You can see an example at <https://catalog.data.gov/dataset/> and <https://opendata.swiss/en/group/gove>. Both catalogues have a sidebar on the left with search refinement options, a search box on the top below the page title, and a list of datasets to the right of the sidebar among other similarities.

## Documentation for ckan_scraper_toolkit.py

### On ckanapi return data

Accross CKAN instances, the ckanapi return data is largely the same in terms of layout. The key difference among these instances is in the `extras` key, where an instance may define its own custom keys. An example ckanapi return is provided below with truncation to save on space. This is the general layout that is returned by most of the toolkit's functions:

```json
{
      "author": null,
      "author_email": null,
      "id": "f468fe8a-a319-464f-9374-f77128ffc9dc",
      "maintainer": "NYC OpenData",
      "maintainer_email": "no-reply@data.cityofnewyork.us",
      "metadata_created": "2020-11-10T17:05:36.995577",
      "metadata_modified": "2024-10-25T20:28:59.948113",
      "name": "nypd-arrest-data-year-to-date",
      "notes": "This is a breakdown of every arrest effected in NYC by the NYPD during the current year.\n This data is manually extracted every quarter and reviewed by the Office of Management Analysis and Planning. \n Each record represents an arrest effected in NYC by the NYPD and includes information about the type of crime, the location and time of enforcement. \nIn addition, information related to suspect demographics is also included. \nThis data can be used by the public to explore the nature of police enforcement activity. \nPlease refer to the attached data footnotes for additional information about this dataset.",
      "organization": {
          "id": "1149ee63-2fff-494e-82e5-9aace9d3b3bf",
          "name": "city-of-new-york",
          "title": "City of New York",
          "description": "",
          ...
      },
      "title": "NYPD Arrest Data (Year to Date)",
      "extras": [
          {
              "key": "accessLevel",
              "value": "public"
          },
          {
              "key": "landingPage",
              "value": "https://data.cityofnewyork.us/d/uip8-fykc"
          },
          {
              "key": "publisher",
              "value": "data.cityofnewyork.us"
          },
          ...
      ],
      "groups": [
          {
              "description": "Local Government Topic - for all datasets with state, local, county organizations",
              "display_name": "Local Government",
              "id": "7d625e66-9e91-4b47-badd-44ec6f16b62b",
              "name": "local",
              "title": "Local Government",
              ...
          }
      ],
      "resources": [
          {
              "created": "2020-11-10T17:05:37.001960",
              "description": "",
              "format": "CSV",
              "id": "c48f1a1a-5efb-4266-9572-769ed1c9b472",
              "metadata_modified": "2020-11-10T17:05:37.001960",
              "name": "Comma Separated Values File",
              "no_real_name": true,
              "package_id": "f468fe8a-a319-464f-9374-f77128ffc9dc",
              "url": "https://data.cityofnewyork.us/api/views/uip8-fykc/rows.csv?accessType=DOWNLOAD",
              ...
          },
          {
              "created": "2020-11-10T17:05:37.001970",
              "describedBy": "https://data.cityofnewyork.us/api/views/uip8-fykc/columns.rdf",
              "describedByType": "application/rdf+xml",
              "description": "",
              "format": "RDF",
              "id": "5c137f71-4e20-49c5-bd45-a562952195fe",
              "metadata_modified": "2020-11-10T17:05:37.001970",
              "name": "RDF File",
              "package_id": "f468fe8a-a319-464f-9374-f77128ffc9dc",
              "url": "https://data.cityofnewyork.us/api/views/uip8-fykc/rows.rdf?accessType=DOWNLOAD",
              ...
          },
          ...
      ],
      "tags": [
          {
              "display_name": "arrest",
              "id": "a76dff3f-cba8-42b4-ab51-1aceb059d16f",
              "name": "arrest",
              "state": "active",
              "vocabulary_id": null
          },
          {
              "display_name": "crime",
              "id": "df442823-c823-4890-8fca-805427bd8dd9",
              "name": "crime",
              "state": "active",
              "vocabulary_id": null
          },
          ...
      ],
      "relationships_as_subject": [],
      "relationships_as_object": [],
      ...
}
```

---
`ckan_package_search(base_url: str, query: Optional[str], rows: Optional[int], start: Optional[int], **kwargs) -> list[dict[str, Any]]`

Searches for packages (datasets) in a CKAN data portal that satisfies a given search criteria.

### Parameters

* **base_url** - The base URL to search from. e.g. "https://catalog.data.gov/"
* **query (optional)** - The keyword string to search for. e.g. "police". Leaving empty will return all packages in the package list. Multi-word searches should be done with double quotes around the search term. For example, '"calls for service"' will return packages with the term "calls for service" while 'calls for service' will return packages with either "calls", "for", or "service" as keywords.
* **rows (optional)** - The maximum number of results to return. Leaving empty will return all results.
* **start (optional)** - Which result number to start at. Leaving empty will start at the first result.
* **kwargs (optional)** - Additional keyword arguments. For more information on acceptable keyword arguments and their function see <https://docs.ckan.org/en/2.10/api/index.html#ckan.logic.action.get.package_search>

### Return

The function returns a list of dictionaries containing matching package results.

---

`ckan_package_search_from_organization(base_url: str, organization_id: str) -> list[dict[str, Any]]`

Returns a list of CKAN packages from an organization. Due to CKAN limitations, only 10 packages are able to be returned.

### Parameters

* **base_url** - The base URL to search from. e.g. "https://catalog.data.gov/"
* **organization_id** - The ID of the organization. This can be retrieved by searching for a package and finding the "id" key in the "organization" key.

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

*NOTE: This function has only been tested on <https://catalog.data.gov/>. It is likely it will not work properly on other platforms.*

* **base_url** - The base URL of the CKAN portal before the collection ID. e.g. "https://catalog.data.gov/dataset/"
* **collection_id** - The ID of the parent package. This can be found by querying the parent package and using the "id" key, or by navigating to the list of child packages and looking in the URL. e.g. In <https://catalog.data.gov/dataset/?collection_package_id=7b1d1941-b255-4596-89a6-99e1a33cc2d8> the collection_id is "7b1d1941-b255-4596-89a6-99e1a33cc2d8"

### Return

List of Package objects representing the child packages associated with the collection.
