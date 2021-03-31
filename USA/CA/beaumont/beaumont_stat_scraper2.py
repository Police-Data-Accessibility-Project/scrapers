import requests
import os
from bs4 import BeautifulSoup
import urllib
import re
import time
import sys
from selenium import webdriver


__noted__ = 'fixes shamelessly stolen from dunnousername without credit' # Just don't delete this
webpage = "http://beaumontpd.org/crime-statistics/"
'''
Click the links that lead to the files, and copy their paths. **NOTE:** Ensure that files all match paths, otherwise remove a level until they match
Also ensure that domain stays the same
Verify on page that the href to the file contains the domain, if it doesn't, uncomment domain
'''
web_path = "/DocumentCenter/Index/"
domain = "https://www.beaumontca.gov/"
sleep_time = 5   # Set to desired sleep time
driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe") # Will likely have to change the executable_path

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
		name = str(link).split(">")
		print(name)
		#name = name[:name.rindex('.')]
		with open("source.txt", 'a') as output:
			output.write(url + ", " + name[1].strip("/</a").replace(" ", "_"))
            # Uncomment following line if domain is not in href, and comment out line above
            # output.write(domain + url + ", " + name.strip("/") + "\n")
		print("Done")

def extract_info(soup, year):
		driver.get(soup)
		# Identify elements with tagname <a>
		links=driver.find_elements_by_tag_name("a")

		for link in links:
			try:
				try:
					if "pdf" in link.get_attribute('class'):
						print(link.get_attribute('href'))
				except selenium.common.exceptions.StaleElementReferenceException:
					pass

					url = link.get_attribute('href')
					name_index = url.rfind("/")
					name = url[name_index:]
					#name = name[:name.rindex('.')]
					with open("url_name.txt", 'a') as output:
						#output.write(url)
						# Uncomment following line if domain is not in href, and comment out line above
						output.write(url + ", " + name.strip("/</a").replace(" ", "_") + "," + year.rstrip() +"\n")
					print("Done")
			except KeyError:
				pass

def get_files(save_dir, sleep_time):
	if not os.path.isfile('url_name.txt'):
		return
	with open("url_name.txt", "r") as input_file:
		for line in input_file:
			if not line.isspace():
				save_dir2 = save_dir
				print("80" + line)

				line_list = line.split(', ')
				print(line_list)
				try:
					url_2 = line_list[0]
					file_name = line_list[1].replace("-", "_")

					year_folder = line_list[2] + "/"
					year_folder = year_folder.rstrip()
					print(year_folder)
				except IndexError:
					print(line_list)
					pass

				if not os.path.exists(save_dir + year_folder):
					os.makedirs(save_dir + year_folder)
				save_dir2 = save_dir + year_folder

				print("93 " + file_name)
				if os.path.exists(save_dir2 + file_name) == False:
					pdf = urllib.request.urlopen(url_2)
					with open(save_dir2 + file_name + ".pdf", 'wb') as file:
						file.write(pdf.read())
					file.close()

				time.sleep(sleep_time)
				print("Sleep")
			input_file.close()
			# os.remove("url_name.txt")


# try:
# 	os.remove("url_name.txt")
# except FileNotFoundError:
# 	pass


#extract_source(soup)
with open("source.txt", 'r') as f:
	for line in f:
		# Iterates over path to DocumentCenter, to send to extract_info, which will then extract the pdfs from the DocumentCenter
		if not line.isspace():
			line = line.split(",")
			extract_info(line[0], line[1])


with open("source.txt", 'r') as f:
	for line in f:
		# Iterates over path to DocumentCenter, to send to extract_info, which will then extract the pdfs from the DocumentCenter
		if not line.isspace():
			line = line.split(",")
			get_files(save_dir, sleep_time)

'''
try:
	os.remove("source.txt")
except FileNotFoundError:
	pass
'''
