# Scraper Index

## Introduction

This script generates the scrapers index (`INDEX.md`) in the root directory. 

The scraper index helps people find scrapers for datasets both inside and outside this repository.

## How to use

1. Clone the repository

2. Create a PDAP [API key](https://docs.pdap.io/api/introduction)

3. Create an environment variable with your API key

    ```bash
    export PDAP_API_KEY="[your API key]"
    ```

4. Navigate to the `scraper_index` folder

    ```bash
    cd utils/meta/scraper_index
    ```

5. Run `python3 index.py`

## Requirements

- `Python 3`
- `requests`
- `from_root`
