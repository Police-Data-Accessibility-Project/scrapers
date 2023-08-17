import os
import sys

import configs
from from_root import from_root

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from scrapers.data_portals.crimegraphics.crimegraphics_clery import \
    crimegraphics_clery

save_dir = "./data/"
data = []

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

crimegraphics_clery(configs, save_dir, configs_file=True)
