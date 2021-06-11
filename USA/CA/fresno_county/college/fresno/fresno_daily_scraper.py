import sys
import os
import configs
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from common import list_pdf_v3

cur_dir = os.getcwd()
save_dir = "./data/"

list_pdf_v3(configs, save_dir, important=True, no_overwrite=True, add_date=True, flavor="lattice", configs_file=True)
