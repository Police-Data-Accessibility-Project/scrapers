import sys
from pathlib import Path
import os
p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p))
from common.utils import get_pdf


def single_pdf_scraper(save_dir, url_2, try_overwite=False, no_overwrite=True):

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
        add_date=True
    )

    import etl
    from etl import pdf_extract
    # Pass save_dir to pdf_extract's pdf_directory param
    try:
        etl.pdf_extract(save_dir, configs.csv_dir)
    except AttributeError:
        if debug:
            print("  [INFO] csv_dir is not defined in the configs.")
            print("      If you want to save in a different location for some reason, ")
            print("      define it in the configs as `csv_dir=\"<folder>\"`")
        etl.pdf_extract(save_dir)
        pass
        
    # import etl.py
