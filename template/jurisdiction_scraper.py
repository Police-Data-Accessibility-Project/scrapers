'''
This is the scraper file, which is typically in Python.
'''


'''
you can use this portion here if you want to reuse parts of our /common library
this adds your current working directory (this cloned repo) /common to your sys path
temporarily so you can import the files like a regular pip installed module

note the 3 at the end. This is how many directories up to root (where /common is)
for example if this script is in /USA/CA/san_francisco, that is 3 directories to root
'''
import sys
from pathlib import Path
cloned_repo_root = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(cloned_repo_root) + '/common')
from bs_scrapers.get_files import get_files # example of importing one of those files


# do your code specific for the jurisdiction here, be sure to check out some other scrapers
# you can call some of the modules in /common where some of frequently used methods are stored



# make sure the end of your file calls the etl.py file!
import etl