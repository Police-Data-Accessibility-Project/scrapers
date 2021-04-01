import os
import urllib
import re
import time
import requests

def get_files(save_dir, sleep_time, delete=True):
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
		
		# Used for debugging
		if delete != False:
			os.remove("url_name.txt")
