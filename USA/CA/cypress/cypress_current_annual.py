import sys
import os
import configs_annual as configs
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/common")
from list_pdf_scrapers.list_pdf_v2 import list_pdf_v2

save_dir = "./data/"

list_pdf_v2(configs, save_dir)
