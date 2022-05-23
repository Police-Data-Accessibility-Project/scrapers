import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common.utils import get_xls

save_dir = "./data/officer_training/"
file_name = "training-report-hours-total.xls"
url = "https://data.wprdc.org/dataset/8a7d1d09-c8d3-4a0b-9812-11f72bb22103/resource/8c810512-007e-4d10-bfb9-a027a4fd682c/download/training-report-hours-total.xls"

get_xls(save_dir, file_name, url, sleep_time=15)

import etl
