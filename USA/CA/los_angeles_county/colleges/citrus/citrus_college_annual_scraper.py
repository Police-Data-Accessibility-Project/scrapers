import os
import configs_annual
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from common import list_pdf_v2

save_dir = "./data/annual/"

list_pdf_v2(configs_annual, save_dir, configs_file=True)
