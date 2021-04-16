import sys
import os
import configs
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p))
from common import list_pdf_v3

save_dir = "./data/"

list_pdf_v3(configs, save_dir)
