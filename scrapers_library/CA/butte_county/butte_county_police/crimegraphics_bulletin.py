import json
import os
import sys

import CG_configs as configs
import pandas as pd
import requests
from bs4 import BeautifulSoup
from from_root import from_root
from tqdm import tqdm

p = from_root('CODE_OF_CONDUCT.md').parent
sys.path.insert(1, str(p))

from scrapers_library.data_portals import crimegraphics_bulletin

save_dir = "./data/bulletin/"
data = []

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

crimegraphics_bulletin(configs, save_dir, configs_file=True)
