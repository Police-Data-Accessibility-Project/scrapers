import sys
import os
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common.utils.demo_utils import data_truncater, field_extractor

directory = "./"

data_truncater(directory)
field_extractor(directory)
