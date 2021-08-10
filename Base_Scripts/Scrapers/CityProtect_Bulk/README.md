CityProtect All Agencies Bulk Download
===

General Info
====
This script queries the public CityProtect api here: https://ce-portal-service.commandcentral.com/api/v1.0/public/agencies

It loops through every agency and checks for: "bulkDownload": true

If so, it downloads all of the reports attached to the agency into the following subdirectory scheme:
./data/<state>/<customerId>

For example:
./data/IN/carmel.in.gov
will contain all of the available csv files for the agency.

Columns
====
Fortunately, all files have the same columns:
* ccn - the agency's specfic Report ID, each agency has a differing scheme
* date - date of the incident
* updateDate - last time the incident was updated
* city - city the incident transpired in
* state - two char state code
* postalCode - ZIP Code, not always available
* blocksizedAddress - an address made more vague to protect PII, (like 4700 Block E 96th Street)
* incidentType - what the incident was (TRAFFIC STOP, ALARM - BURGLAR, )
* parentIncidentType - Parent category of above. (Proactive Policing, Traffic, Quality of Life.etc)
* narrative - more information (may just be a clone of incidentType)

Data Samples
====
Samples are in ./samples for a variety of states to show the slight discrepancies to be aware of (like ccn or incidentType)

Script Info
====
* Full Script will take several hours to run. There are about 355 agencies with bulk download enabled, and each agency can have 10+ files.
* There is a sleep of every 5 seconds between file retrieval to prevent a DoS attack from downloading too fast.