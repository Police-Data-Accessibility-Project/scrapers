import json
import os
from pathlib import Path
import sys

# this will grab the libraries we need from /common/etl
# prevents having to keep cloning the libraries everywhere (copied from CaptainStabs' usage on scrapers)
p = Path().resolve().parents[4]
pdap_library = os.path.join(p, "common")  # fix for windows
print('\ncommon path: ' + pdap_library + '\n')
sys.path.insert(1, pdap_library)  

from common.etl import main

'''
    schema_load:
        - schema file JSON
        - branch name
        - current directory (that houses the data)
'''
schema = main.schema_load(json.load('schema.json', 'r'), 'master', os.getcwd())