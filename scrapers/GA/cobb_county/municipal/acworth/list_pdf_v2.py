import sys
import os
import configs
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from utils.pdf.list_pdf_scrapers import list_pdf_v2

save_dir = "./data/annual_reports/"

list_pdf_v2(configs, save_dir, configs_file=True)
