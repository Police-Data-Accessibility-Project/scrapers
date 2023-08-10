import sys
import os
from configs import weekly_configs as configs
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from utils.pdf.list_pdf_scrapers import list_pdf_v3

save_dir = "./data/cobra/"

list_pdf_v3(configs, save_dir, add_date=True, name_in_url=False, configs_file=True)
