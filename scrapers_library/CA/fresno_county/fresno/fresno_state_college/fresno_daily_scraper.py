import os
import sys

import configs
from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_scrapers import list_pdf_v3

cur_dir = os.getcwd()
save_dir = "./data/"

list_pdf_v3(configs, save_dir, important=True, no_overwrite=True, add_date=True, flavor="lattice", configs_file=True)
