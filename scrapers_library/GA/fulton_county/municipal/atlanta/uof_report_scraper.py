import sys
import os
from configs import uof_configs as configs
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from utils.pdf.list_pdf_scrapers import list_pdf_v2

save_dir = "./data/UOF/"

list_pdf_v2(configs, save_dir, name_in_url=False, configs_file=True)
