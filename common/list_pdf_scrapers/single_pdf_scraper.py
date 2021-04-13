import sys
from pathlib import Path
p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/common")
from base_scrapers.file_downloaders.downloaders import get_pdf


def single_pdf_scraper(save_dir, configs, try_overwite=False, no_overwrite=True):

    url_2 = configs.webpage

    file_name = url_2[url_2.rindex("/") :]
    print(file_name)

    get_pdf(
        save_dir,
        file_name,
        url_2,
        debug=False,
        sleep_time=configs.sleep_time,
        try_overwite=False,
        no_overwrite=True,
    )
