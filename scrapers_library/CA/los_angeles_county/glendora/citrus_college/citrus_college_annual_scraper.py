import os
import sys

import configs_annual
from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_scrapers import list_pdf_v2

save_dir = "./data/annual/"

list_pdf_v2(configs_annual, save_dir, configs_file=True)
