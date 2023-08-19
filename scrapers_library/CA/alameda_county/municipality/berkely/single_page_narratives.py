import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from utils.pdf.list_pdf_scrapers import single_pdf_scraper

url_2 = [
    "https://data.cityofberkeley.info/api/views/k2nh-s5h5/files/tgCx9-LwzyULzas6ZSxGdPmc1f-0euS2Y6EVOrNH940?download=true&filename=01_Page_Narrative_Crime.pdf",
    "https://data.cityofberkeley.info/api/views/xi7q-nji6/files/b8b65e00-d902-4f27-9c9b-d2f083a106d7?download=true&filename=Berkeley%20Police%20Arrest%20Log.pdf",
    "https://data.cityofberkeley.info/api/views/7ykt-c32j/files/abac1e14-ce93-4dc4-99b9-9dafce210877?download=true&filename=Berkeley%20Police%20Jail%20Booking%20Log.pdf",
    "https://data.cityofberkeley.info/api/views/4tbf-3yt8/files/2ed1e25d-effc-4e3f-b74c-21599b22b85f?download=true&filename=Berkeley%20Stop%20Data.pdf",
    "https://data.cityofberkeley.info/api/views/ysvs-bcge/files/55a2ff99-a428-4ab0-bf6e-cfef2c22c6ad?download=true&filename=One%20Page%20Narrative%20for%20Stop%20Data%20(October%201,%202020).pdf",
    "https://data.cityofberkeley.info/api/views/efkp-2py4/files/ce5c3c1b-9786-447b-b550-55f473602db1?download=true&filename=Berkeley%20PD%20UCR%20-%20Annual%20Part%20I%20Crimes.pdf",
]
save_folder = [
    "cfs/",
    "arrests/",
    "jail_bookings/",
    "stop_data/historical/",
    "stop_data/",
    "annual_part1/",
]
save_directory = "./data/"

for i, row in enumerate(url_2):
    save_dir = save_directory + save_folder[i]
    filename = url_2[i].split("filename=")
    filename = filename[1].replace("%20", "_")
    single_pdf_scraper(save_dir, url_2[i], name_in_url=False, filename=filename)
