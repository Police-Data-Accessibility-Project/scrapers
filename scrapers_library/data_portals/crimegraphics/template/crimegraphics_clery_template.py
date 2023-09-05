import os
import sys

import CG_configs as configs
from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.crimegraphics import crimegraphics_clery

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