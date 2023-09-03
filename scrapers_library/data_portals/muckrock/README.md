# Muckrock Scraper

## Introduction

This scraper can be used to download files from [https://www.muckrock.com](https://www.muckrock.com), a common place make foi requests from police departments and other agencies.

The scraper's functions can be found in `muckrock_scraper.py`. Check function documentation for more details on the its arguments.

Templates for various use cases can be found in the `template` folder.

## Use Cases

### I want to scrape an individual file from a foi request

See `template/single_file_template.py` for an example.

Call the `get_single_file()` function with a relative save directory and the download url for the file.

### I want to scrape all files from a foi request

See `template/foia_files_template.py` for an example.

Call the `get_foia_files()` function with a relative save directory and the url to the foi request.

### I want to scrape all files from an agency

See `template/agency_files_template.py` for an example.

Call the `get_all_agency_files()` function with a relative save directory and the url to the agency.
