import sys
import os
import configs
import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from scrapers.data_portals.crimegraphics import crimegraphics_bulletin


save_dir = "./data/"
data = []

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

crimegraphics_bulletin(configs, save_dir, configs_file=True)
