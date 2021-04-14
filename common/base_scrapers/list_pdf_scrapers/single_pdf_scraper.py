import sys
from pathlib import Path
p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/common")
from common.file_downloaders.downloaders import get_pdf


def single_pdf_scraper(save_dir="./data", url_2, try_overwite=False, no_overwrite=True):

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    file_name = url_2[url_2.rindex("/") :]
    print(file_name)

    get_pdf(
        save_dir,
        file_name,
        url_2,
        debug=False,
        sleep_time=0,
        try_overwite=False,
        no_overwrite=True,
    )

    # import etl
