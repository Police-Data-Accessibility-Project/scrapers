import json
import os
import sys

import configs
import pandas as pd
import requests
from bs4 import BeautifulSoup
from from_root import from_root
from tqdm import tqdm

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals.crimegraphics import crimegraphics_clery

save_dir = "./data/daily_bulletins/"
data = []

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

crimegraphics_clery(configs, save_dir, configs_file=True)
