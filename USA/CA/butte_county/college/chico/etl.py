import json
import os
from pathlib import Path
import sys

# this will grab the libraries we need from /common/etl\
p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common.etl import main

'''
    schema_load:
        - schema file JSON
        - branch name
        - current directory (that houses the data)
'''
schema = main.schema_load(json.load(open('schema.json', 'r')), 'master', os.getcwd())