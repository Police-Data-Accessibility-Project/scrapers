import os
import sys

import CG_configs as configs
from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.crimegraphics import crimegraphics_bulletin

configs = {
    "url": "",
    "department_code": "",
}

save_dir = "./data/"
data = []

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

crimegraphics_bulletin(configs, save_dir)