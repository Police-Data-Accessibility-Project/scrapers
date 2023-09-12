# Open Data Network Scraper

## Introduction

This scraper retrieves relevant datasets from the [Open Data Network](https://www.opendatanetwork.com/) and outputs them to a CSV for uploading to the `data sources` database

## How to run

1. clone the repository, or download the file
2. create a PDAP [API key](https://docs.pdap.io/api/introduction)
3. create a `.env` file in the project's root directory with the contents `PDAP_API_KEY = "[your API key]"`
4. `cd` into `open_data_network`, or the repository containing the scraper file
5. run `python3 open_data_network`

## Requirements

- `Python 3`
- `requests`
- `dotenv`
