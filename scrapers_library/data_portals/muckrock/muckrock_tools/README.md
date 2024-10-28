# Muckrock Toolkit

## Description

This repo provides tools for searching Muckrock FOIA requests, it includes scripts for downloading data from MuckRock, generating CSV files per PDAP database requirements, and automatic labeling

## Installation

### 1. Clone the `scrapers` repository and navigate to the `muckrock_tools` directory.

```
git clone git@github.com:Police-Data-Accessibility-Project/scrapers.git
cd scrapers/scrapers_library/data_portals/muckrock/muckrock_tools
```

### 2. Create a virtual environment.

If you don't already have virtualenv, install the package:

```

pip install virtualenv

```

Then run the following command to create a virtual environment (ensure the python version is as below):

```

virtualenv -p python3.12 venv

```

### 3. Activate the virtual environment.

```

source venv/bin/activate

```

### 4. Install dependencies.

```

pip install -r requirements.txt

```

## Uses

### 1. Simple Search Term

- `muck_get.py`
- script to perform searches on MuckRock's database, by matching a search string to title of request. Search is slow due to rate limiting (cannot multi thread around it).

### 2. Clone Muckrock database & search locally

~~- `download_muckrock_foia.py` `search_local_foia_json.py`~~ (deprecated)

- scripts to clone the MuckRock foia requests collection for fast local querying (total size <2GB at present)

- `create_foia_data_db.py` creates and populates a SQLite database (`foia_data.db`) with all MuckRock foia requests. Various errors outside the scope of this script may occur; a counter (`last_page_fetched.txt`) is created to keep track of the most recent page fetched and inserted into the database. If the program exits prematurely, simply run `create_foia_data_db.py` again to continue where you left off. A log file is created to capture errors for later reference.

- After `foia_data.db` is created, run `search_foia_data_db.py`, which receives a search string as input and outputs a JSON file with all related foia requests for later processing by `generate_detailed_muckrock_csv.py`. For example,

```
python3 search_foia_data_db.py --search_for "use of force"
```

produces 'use_of_force.json'.

### 3. County Level Search

- `get_allegheny_foias.py`, `allegheny_county_towns.txt`
- To search for any and all requests in a certain county (e.g. Allegheny in this case) you must provide a list of all municipalities contained within the county. Muckrock stores geographic info in tiers, from Federal, State, and local level. At the local level, e.g. Pittsburgh and Allegheny County are in the same tier, with no way to determine which municipalities reside within a county (without providing it yourself).

The `get_allegheny_foias.py` script will find the jurisdiction ID for each municipality in `allegheny_county_towns.txt`, then find all completed FOIA requests for those jurisdictions.

### 4. Generate detailed FOIA data in PDAP database format

- `generate_detailed_muckrock_csv.py`
- Once you have a json of relevant FOIA's, run it through this script to generate a CSV that fulfills PDAP database requirements.

### 5. ML Labeling

- `muckrock_ml_labeler.py`
- A tool for auto labeling MuckRock sources. This script is using [fine-url-classifier](https://huggingface.co/PDAP/fine-url-classifier) to assign 1 of 36 record type labels. At present, script is expecting each source to have associated header tags, provided via `html-tag-collector/collector.py`. (TODO: For muckrock sources, `collector.py` insufficient, does not grab main text of the request)
