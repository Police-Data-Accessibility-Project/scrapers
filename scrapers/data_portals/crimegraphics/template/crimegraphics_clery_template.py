import sys
import os
import CG_configs as configs
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from scrapers.data_portals.crimegraphics import crimegraphics_clery

configs = {
    "url": "",
    "department_code": "",
    "list_header": [
        "ChargeDescription",
        "CaseNum",
        "ReportDate",
        "OffenseDate",
        "Location",
        "ChargeDisposition",
    ],
}

save_dir = "./data/"
data = []

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

crimegraphics_clery(configs, save_dir)