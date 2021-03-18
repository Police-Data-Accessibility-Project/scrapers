import requests
from datetime import date
import os
import time
import json

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
