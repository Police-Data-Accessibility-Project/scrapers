import os
import sys

from configs import week_report_configs as configs
from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_scrapers import list_pdf_v3

save_dir = "./data/weekly_reports/"

list_pdf_v3(configs, save_dir, configs_file=True)
