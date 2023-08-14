'''
This is the scraper file, which is typically in Python.
'''


'''
You can use this if you want to reuse parts of our /utils library. 
It adds your current working directory (this repo) /utils to your sys path
temporarily so you can import the files like a regular pip installed module.

Note the 5 at the end. This is how many directories up to root (where /utils is)
for example if this script is in /scrapers/CA/san_francisco_county/municipal/san_francisco, that is 5 directories to root
'''
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_utils.get_files import get_files # example of importing one of those files


# Put your code here