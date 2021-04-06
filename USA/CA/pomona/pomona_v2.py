import sys
import configs
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/common")
from list_pdf_scrapers.list_pdf_v2 import list_pdf_v2

list_pdf_v2(configs)
