# this makes a list of headers from all the CSV files found in the USA directory.
# fields are added to fields.txt.

import sys
import os
from pathlib import Path

p = Path(__file__).resolve().parents[1]
sys.path.insert(1, str(p))

from common.utils.demo_utils import data_truncater, field_extractor

directory = "./"

field_extractor(directory)
