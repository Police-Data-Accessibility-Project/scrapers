import os
import sys

import configs
from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_scrapers import list_pdf_v3

save_dir = "./data/"

list_pdf_v3(configs, save_dir, extract_name=True, configs_file=True)
