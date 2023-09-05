'''
This is the scraper file, which is typically in Python.
'''


'''
You can use this if you want to reuse parts of our /utils library. 
It adds your current working directory (this repo) to your sys path
temporarily so you can import the files like a regular pip installed module.
'''
import sys

from from_root import from_root

p = from_root('CONTRIBUTING.md').parent
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_utils.get_files import get_files  # example of importing one of those files

# Put your code here
