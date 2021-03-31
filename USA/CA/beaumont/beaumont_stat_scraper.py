import requests
import os
from bs4 import BeautifulSoup
import urllib
import re
import time
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + '/common')
from bs_scrapers.get_files import get_files


__noted__ = 'fixes shamelessly stolen from dunnousername without credit' # Just don't delete this
webpage = "http://beaumontpd.org/crime-statistics/"
'''
Click the links that lead to the files, and copy their paths. **NOTE:** Ensure that files all match paths, otherwise remove a level until they match
Also ensure that domain stays the same
Verify on page that the href to the file contains the domain, if it doesn't, uncomment domain
'''
web_path = "/DocumentCenter/Index/"
domain = "https://www.beaumontca.gov"
sleep_time = 5   # Set to desired sleep time

cur_dir = os.getcwd()
save_dir = cur_dir + "/data/"

if not os.path.exists(save_dir):
	os.makedirs(save_dir)

html_page = requests.get(webpage).text
soup = BeautifulSoup(html_page, "html.parser")
#print(soup)

url_name = []
'''
Gets the urls that lead to the DocumentCenter, and saves them in source.txt
'''
def extract_source(soup):
	for link in soup.findAll('a'):
		if link.get('href') is None:
			continue
		if not "DocumentCenter" in link['href']:
			continue
		print(link.get('href'))
		url = str(link['href'])
		name = url[url.rindex('/'):]
		#name = name[:name.rindex('.')]
		with open("source.txt", 'a') as output:
			output.write(url + ", " + name.strip("/") +"\n")
            # Uncomment following line if domain is not in href, and comment out line above
            # output.write(domain + url + ", " + name.strip("/") + "\n")
		print("Done")

def extract_info(soup):
    for link in soup.findAll('a'):
        if link.get('href') is None:
            continue
        if not link['href'].startswith(web_path):
            continue
        print(link.get('href'))
        url = str(link['href'])
        name = url[url.rindex('/'):]
        #name = name[:name.rindex('.')]
        with open("url_name.txt", 'a') as output:
            # output.write(url)
            # Uncomment following line if domain is not in href, and comment out line above
            output.write(domain + url + ", " + name.strip("/") + "\n")
    print("Done")

def get_files(save_dir, sleep_time):
	if not os.path.isfile('source.txt'):
		return
	with open("s.txt", "r") as input_file:
		for line in input_file:
			print(line)

			line_list = line.split(', ')
			url_2 = line_list[0]
			file_name = line_list[1].replace(" ", "_")[:-1]
			#file_name = save_dir + file_name
			#document = requests.get(url_2, allow_redirects=True)

			if url_2.find(".pdf"):
				#save_path = os.path.join(save_dir, file_name+".pdf")
				print(file_name)
				if os.path.exists(save_dir + file_name) == False:
					pdf = urllib.request.urlopen(url_2)
					with open(save_dir + file_name, 'wb') as file:
						file.write(pdf.read())
					file.close()
			elif url_2.find(".doc"):
				#save_path = os.path.join(save_dir, file_name+".doc")
				if os.path.exists(save_dir + file_name) == False:
					document = requests.get(url_2, allow_redirects=True)
					with open(file_name, "w") as data_file:
						data_file.write(document.text)   # Writes using requests text 	function thing
					data_file.close()
			else:
				print("Unhandled documents type")
				print("Url: " + url_2)
			time.sleep(sleep_time)
			print("Sleep")
		input_file.close()
		os.remove("url_name.txt")

try:
	os.remove("url_name.txt")
except FileNotFoundError:
	pass
extract_source(soup)
with open("source.txt", 'r') as f:
	for line in f:
		# Iterates over path to DocumentCenter, to send to extract_info, which will then
		source_page = requests.get(line).text
		source_soup = BeautifulSoup(source_page, "html.parser")
		extract_info(source_soup)
		get_files(save_dir, sleep_time)

try:
	os.remove("source.txt")
except FileNotFoundError:
	pass
