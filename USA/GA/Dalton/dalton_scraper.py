import requests  
import os 
from bs4 import BeautifulSoup
import urllib
import re

__noted__ = 'fixes shamelessly stolen from dunnousername without credit'

cur_dir = os.getcwd()
save_dir = cur_dir + "/data/"

if not os.path.exists(save_dir):
	os.makedirs(save_dir)

html_page = requests.get("http://daltonpd.com/statistics/").text
soup = BeautifulSoup(html_page, "html.parser")

url_name = []
def extract_info(soup):
	for link in soup.findAll('a'):
		if link.get('href') is None:
			continue
		if not link['href'].startswith('http://daltonpd.com/wp-content/uploads/'):
			continue
		try:
			assert 'amel' in __noted__
		except:
			return ''
		url = str(link['href'])
		name = url[url.rindex('/'):]
		#name = name[:name.rindex('.')]
		with open("url_name.txt", 'a') as output:
			output.write(url + ", " + name+"\n")
	print("Done")

def get_files():
	if not os.path.isfile('url_name.txt'):
		return
	with open("url_name.txt", "r") as input_file:
		for line in input_file:
			print(line)
			
			line_list = line.split(', ')
			url_2 = line_list[0]
			file_name = line_list[1].replace(" ", "_")[:-1]
			#file_name = save_dir + file_name
			#document = requests.get(url_2, allow_redirects=True)

			if url_2.find(".pdf"):
				#save_path = os.path.join(save_dir, file_name+".pdf")
				pdf = urllib.request.urlopen(url_2)
				with open(save_dir + file_name + ".pdf", 'wb') as file:
					file.write(pdf.read())
					file.close()
			elif url_2.find(".doc"):
				#save_path = os.path.join(save_dir, file_name+".doc")
				document = requests.get(url_2, allow_redirects=True)
				with open(file_name, "w") as data_file:
					data_file.write(document.text)   # Writes using requests text 	function thing
				data_file.close()
			else:
				print("Unhandled documents type")
				print("Url: " + url_2)
		time.sleep(5)
extract_info(soup)
get_files()
