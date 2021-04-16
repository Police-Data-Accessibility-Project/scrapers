import sys
from pathlib import Path

# p = Path(__file__).resolve().parents[3]
# sys.path.insert(1, str(p) + "/common")
from common.single_pdf_scraper import single_pdf_scraper

url_2 = "https://www.antiochca.gov/fc/police/crime-maps/this-weeks-cfs.pdf"
save_dir = "./data/"

single_pdf_scraper(save_dir, url_2)
