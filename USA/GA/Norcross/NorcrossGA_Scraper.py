import requests
import os
import json
import urllib


cur_dir = os.getcwd()
save_dir = cur_dir + "/USA/GA/Norcross/pdfs/"

if not os.path.exists(save_dir):
	os.makedirs(save_dir)


def scrape_urls():
	with open("response.json", "r") as json_file:
		response = json.load(json_file)
		r_data = response['data']
		total = response['total']
		base_url = 'https://www.norcrossga.net'
		for p in range(total):
			doc_url = r_data[p]['URL']
			output_url = base_url + doc_url

			with open('urls.txt','a') as output:
				output.write(output_url + '\n')
	output.close()

def get_name(line):
	try:
		with open("response.json", "r") as json_file:
			response = json.load(json_file)
			r_data = response['data']
			#total = response['total']

			doc_name = r_data[line]['DisplayName']
			return doc_name
	except IndexError:
		print("Done, verify that last document matches last url")


def download_data():
	with open('urls.txt', 'r') as in_url:
		for num, line in enumerate(in_url):
			try:
				pdf = urllib.request.urlopen(line) # Gets the pdf
				file_name = get_name(num)
				print("Getting " + file_name)
				file_name = file_name.replace(' ', '_')
				with open(save_dir + file_name + '.pdf', 'wb') as file:
					file.write(pdf.read())
					file.close()
			except TypeError:
				print("Done, verify that last document matches last url")
				break

download_data()
