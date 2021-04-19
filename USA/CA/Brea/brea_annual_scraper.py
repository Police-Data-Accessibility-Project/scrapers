import sys
from pathlib import Path
p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/common")
from base_scrapers.list_pdf_scrapers.single_pdf_scraper import single_pdf_scraper

url_2 = "https://www.ci.brea.ca.us/DocumentCenter/View/116/CrimeStats_Brea"

single_pdf_scraper(url_2)
