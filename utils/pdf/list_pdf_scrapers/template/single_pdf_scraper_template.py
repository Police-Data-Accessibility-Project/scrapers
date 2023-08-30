import sys

from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_scrapers.single_pdf_scraper import single_pdf_scraper

url_2 = "https://www.ci.brea.ca.us/DocumentCenter/View/116/CrimeStats_Brea"
save_dir = "./data"

single_pdf_scraper(save_dir, url_2)
