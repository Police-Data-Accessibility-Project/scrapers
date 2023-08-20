import os
import sys

from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.crimegraphics.crimegraphics_clery import crimegraphics_clery

configs = {
    "url": "https://hsupd.crimegraphics.com/2013/default.aspx",
    "department_code": "HSUPD",
    "list_header": [
        "ChargeDescription",
        "CaseNum",
        "Reported",
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
