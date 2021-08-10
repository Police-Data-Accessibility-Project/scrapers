import json
from pathlib import Path
import sys

# this will grab the libraries we need from /common/etl\
p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common.etl import main

'''
    schema_load:
        - schema file JSON
        - branch name (override)
'''
schema = main.schema_load(json.load(open('schema.json', 'r')))

# overwrite the schema.json with the changes from the etl
with open('schema.json', 'w+') as outfile:
    json.dump(schema, outfile, indent=4)