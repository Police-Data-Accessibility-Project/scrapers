'''
This is the scraper file, which is typically in Python.
'''


'''
You can use this if you want to reuse parts of our /common library. 
It adds your current working directory (this repo) /common to your sys path
temporarily so you can import the files like a regular pip installed module.

Note the 3 at the end. This is how many directories up to root (where /common is)
for example if this script is in /scrapers/CA/san_francisco, that is 3 directories to root
'''
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common.utils import get_files # example of importing one of those files


# Put your code here