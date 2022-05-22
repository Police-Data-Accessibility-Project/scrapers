# Source info

Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if something has changed.

## Data refresh rate

[Police Incident Blotter Archive](https://data.wprdc.org/dataset/uniform-crime-reporting-data): Daily

## Legal

Include the Terms of Service or robots.txt (or link to them). How does your code account for or meet the legal guidelines?

## Fields being collected:

- `_id`
- `PK`: Incident ID number
- `CCR`: Incident report number
- `HIERARCHY`: Highest UCR hierarchy
- `INCIDENTTIME`
- `INCIDENTLOCATION`
- `CLEARED_FLAG`: Whether the incident was closed
- `INCIDENTNEIGHBORHOOD`
- `INCIDENTZONE`

## Fields unobtainable within our legal guidelines:

## Data uniformity

Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?

## Sample response

In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.
