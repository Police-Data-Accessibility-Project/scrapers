# Source info

Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if something has changed.

## Data refresh rate

[Police Incident Blotter Archive](https://data.wprdc.org/dataset/uniform-crime-reporting-data): Daily

[Police Incident Blotter (30 Day)](https://data.wprdc.org/dataset/police-incident-blotter): Daily

[Police Officer Training](https://data.wprdc.org/dataset/officer-training): Annually, none since 2016

[Police Arrest Records](https://data.wprdc.org/dataset/arrest-data): Daily

[Police Firearm Seizures](https://data.wprdc.org/dataset/pbp-fire-arm-seizures): Monthly

[Non-Traffic Citations](https://data.wprdc.org/dataset/non-traffic-citations): Daily

## Legal

[Creative Commons Attribution](http://www.opendefinition.org/licenses/cc-by)

[Terms of Use](https://www.wprdc.org/terms-of-use/)

## Fields being collected:

- `_id`
- `PK`: Incident ID number
- `CCR`: Incident report number
- `HIERARCHY`: Highest UCR hierarchy number
- `INCIDENTTIME`
- `INCIDENTLOCATION`
- `CLEARED_FLAG`: Whether the incident was cleared
- `INCIDENTNEIGHBORHOOD`
- `INCIDENTZONE`
- `HIERARCHYDESC`
- `INCIDENTHIERARCHYDESC`
- `OFFENSES`
- `INCIDENTTRACT`
- `COUNCIL_DISTRICT`
- `PUBLIC_WORKS_DIVISION`
- `X`
- `Y`

- `CLASS_NAME`
- `OFFICERS_TRAINED_2006`
- `OFFICERS_TRAINED_2007`
- `OFFICERS_TRAINED_2008`
- `OFFICERS_TRAINED_2009`
- `OFFICERS_TRAINED_2010`
- `OFFICERS_TRAINED_2011`
- `OFFICERS_TRAINED_2012`
- `OFFICERS_TRAINED_2013`
- `OFFICERS_TRAINED_2014`
- `OFFICERS_TRAINED_2015`
- `OFFICERS_TRAINED_2016`
- `TOTALS`
- `CLASS_HOURS_2006`
- `CLASS_HOURS_2007`
- `CLASS_HOURS_2008`
- `CLASS_HOURS_2009`
- `CLASS_HOURS_2010`
- `CLASS_HOURS_2011`
- `CLASS_HOURS_2012`
- `CLASS_HOURS_2013`
- `CLASS_HOURS_2014`
- `CLASS_HOURS_2015`
- `CLASS_HOURS_2016`
- `TOTAL_HOURS`

- `AGE`
- `GENDER`
- `RACE`
- `ARRESTTIME`
- `ARRESTLOCATION`

- `address`
- `total_count`
- `other_count`
- `pistol_count`
- `revolver_count`
- `rifle_count`
- `shotgun_count`
- `year`
- `month`
- `dow`: Day of week (0-6 starting Sunday)
- `neighborhood`
- `council_district`
- `ward`
- `tract`: 2010 Census tract location
- `public_works_division`
- `police_zone`
- `fire_zone`
- `latitude`
- `longitute`

- `CITEDTIME`

## Fields unobtainable within our legal guidelines:

Some data (such as `ARRESTLOCATION` and `INCIDENTLOCATION`) are generalized to protect the privacy of those involved.
Exact address data is not available to the public.

Some data (such as dates and locations) may be ommitted to protect ongoing investigations.

## Data uniformity

Some data only had .xls files available for download while the rest are in .csv format.

Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?

## Sample response

See `./data` folder
