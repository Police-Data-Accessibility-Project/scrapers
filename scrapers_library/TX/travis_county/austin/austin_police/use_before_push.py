import os
import sys

from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from utils.meta import data_truncator, field_extractor

dir = "./"

data_truncator(dir)
field_extractor(dir)
