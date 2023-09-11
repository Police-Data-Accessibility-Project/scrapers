# Scraper Index

## Introduction

This script generates the scrapers index (`INDEX.md`) in the root directory. 

The scraper index helps people find scrapers for datasets both inside and outside this repository.

## How to use

1. Create a PDAP [API key](https://docs.pdap.io/api/introduction)

2. Create a `.env` file in the project's root directory

    It should contain the following:

    ```py
    PDAP_API_KEY = "[your API key]"
    ```

3. Navigate to the `scraper_index` folder

    ```bash
    cd utils/meta/scraper_index
    ```

4. Run `python3 index.py`

## Requirements

- `Python 3`
- `requests`
- `from_root`
- `dotenv`
