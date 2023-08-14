import sys
from pathlib import Path
p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from utils.pdf.list_pdf_scrapers import single_pdf_scraper

url_2 = "https://www.antiochca.gov/fc/police/crime-maps/this-weeks-cfs.pdf"
save_dir = "./data/cfs/"

single_pdf_scraper(save_dir, url_2)
