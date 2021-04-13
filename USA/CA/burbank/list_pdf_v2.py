import sys
import os
import configs
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/common")
from list_pdf_scrapers.list_pdf_v3 import list_pdf_v3

cur_dir = os.getcwd()
save_dir =  "./data/"

list_pdf_v3(configs, save_dir, extract_name=True)
