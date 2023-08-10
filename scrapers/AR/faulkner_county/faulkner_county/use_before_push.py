import sys
import os
from pathlib import Path

p = Path(__file__).resolve().parents[4]
sys.path.insert(1, str(p))

from utils.meta import data_truncator, field_extractor

directory = "./"

data_truncator(directory)
field_extractor(directory)
