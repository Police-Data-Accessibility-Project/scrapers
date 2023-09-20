import os
import sys

import admin_configs as configs
from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_scrapers import list_pdf_v3

save_dir = "./data/admin_investigations/"
configs = {
    "webpage": "http://www.el-cerrito.org/1343/Administrative-Investigation-12-21",
    "web_path": "/DocumentCenter/View/",
    "domain_included": False,
    "domain": "http://www.el-cerrito.org/",
    "sleep_time": 5,
    "non_important": ["emergency", "training", "guidelines"],
    "debug": False,
}

list_pdf_v3(configs, save_dir)
