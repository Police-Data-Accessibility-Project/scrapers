import requests  
import os 
from bs4 import BeautifulSoup
import urllib
import re

cur_dir = os.getcwd()
save_dir = cur_dir + "/data/"

urllib.request.urlretrieve("http://daltonpd.com/statistics/", os.path.join(cur_dir, f'links.txt'))

with open('links.txt','r') as links:
	for line in links:
		if line.find('<a href="http://daltonpd.com/wp-content/uploads/'):
			line = line.strip('<a href=\"')
