# Muckrock Scraper

## Introduction

This scraper can be used to download files from [https://www.muckrock.com](https://www.muckrock.com), a common place to make [FOIA](https://docs.pdap.io/activities/data-sources/foia) requests from police departments and other agencies.

The scraper's functions can be found in `muckrock_scraper.py`. Check function documentation for more details on its arguments.

Templates for various use cases can be found in the `template` folder.

## Use Cases

### I want to scrape an individual file from a FOIA request

See `template/single_file_template.py` for an example.

1. Copy `single_file_template.py` to your scraper directory.
2. Replace `link` with the download link to the file you wish to download.
3. Call the `get_single_file()` function with a relative save directory and the link.

### I want to scrape all files from a FOIA request

See `template/foi_files_template.py` for an example.

1. Copy `foi_files_template.py` to your scraper directory.
2. Replace `link` with the link to the FOIA request with files you wish to download.
3. Call the `get_foi_files()` function with a relative save directory and the link.

### I want to scrape all files from an agency

See `template/agency_files_template.py` for an example.

1. Copy `agency_files_template.py` to your scraper directory.
2. Replace `link` with the link to the agency with files you wish to download.
3. Call the `get_all_agency_files()` function with a relative save directory and the link.

## Ignoring Files

Certain files can be ignored with either of the two bulk scraper functions utilizing the `ignore` argument.

`ignore` is a list of strings that will skip over files with any those strings in common.

`ignore` is checked aginst the file title, download URL, and datetime.

### Ignoring by file types

To ignore all files of type `.jpg`, just add `[".jpg"]` to `ignore`.

### Ignoring by datetime

To ignore all files uploaded on March 28th, 2019, add `["2019-03-28"]` to `ignore`.

You can also add `["2019"]` to ignore all files uploaded in 2019 or `["2019-03"]` to ignore all files uploaded in March of 2019.

File upload dates are found above the file titles in Muckrock.

### Ignoring by title

To ignore all files with "Interim Response" in the title, add `["Interim Response"]` to `ignore`.
