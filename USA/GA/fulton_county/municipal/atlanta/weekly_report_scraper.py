import sys
import os
from configs import week_report_configs as configs
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from common import list_pdf_v3

save_dir = "./data/weekly_reports/"

list_pdf_v3(configs, save_dir)
