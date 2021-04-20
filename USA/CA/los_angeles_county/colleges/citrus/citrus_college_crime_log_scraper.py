import os
import sys
import configs_crime_log
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from common import list_pdf_v2

save_dir = "./data/crime_logs/"

list_pdf_v2(configs_crime_log, save_dir)
