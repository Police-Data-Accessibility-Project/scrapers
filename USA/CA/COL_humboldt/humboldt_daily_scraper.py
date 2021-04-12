import sys
import os
import configs
import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/common")
from base_scrapers.crimegraphics.crimegraphics_scraper import crimegraphics_scraper


save_dir = "./data/"
data = []

if not os.path.exists(save_dir):
	os.makedirs(save_dir)

crimegraphics_scraper(configs, save_dir)
