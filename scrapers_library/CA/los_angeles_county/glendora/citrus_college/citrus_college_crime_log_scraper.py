import os
import sys

import configs_crime_log
from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_scrapers import list_pdf_v2

save_dir = "./data/crime_logs/"

list_pdf_v2(configs_crime_log, save_dir, configs_file=True)
