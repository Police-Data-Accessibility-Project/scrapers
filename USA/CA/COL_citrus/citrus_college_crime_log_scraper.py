import os
import sys
import configs_crime_log
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/common")
from list_pdf_scrapers.list_pdf_v2 import list_pdf_v2

save_dir = "./data/crime_logs/"

list_pdf_v2(configs_crime_log, save_dir)
