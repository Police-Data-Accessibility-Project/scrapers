import sys

from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from utils.meta.all_fields_extractor.field_extractor import field_extractor
from utils.meta.data_truncator.truncate import data_truncator

directory = "./"

data_truncator(directory)
field_extractor(directory)
