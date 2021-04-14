import os
import configs_annual
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/common")
from base_scrapers.list_pdf_scrapers.list_pdf_v2 import list_pdf_v2

save_dir = "./data/annual/"

list_pdf_v2(configs_annual, save_dir)
