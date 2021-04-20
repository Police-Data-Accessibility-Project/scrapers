import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p) + "/common")
from common import single_pdf_scraper

url_2 = "https://www.ci.brea.ca.us/DocumentCenter/View/116/CrimeStats_Brea"
save_dir = "./data"

single_pdf_scraper(save_dir, url_2)
