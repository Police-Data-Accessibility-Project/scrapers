import sys
import os
import admin_configs as configs
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from utils.pdf.list_pdf_scrapers import list_pdf_v2

save_dir = "./data/admin_investigations/"

list_pdf_v2(configs, save_dir, configs_file=True)
