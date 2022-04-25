'''W. Alec Akin
Police Data Accessibility Project
PDAP CKAN Python Project
main.py
April 13, 2022
https://pdap.io
Based on information from https://www.pythonsherpa.com/tutorials/2/
Intended for use with https://data.wprdc.org/dataset/officer-training
and other CKAN-based Open Data Portals'''


#Import libraries required
import pprint
import requests
import json     #Allows us to work with JSON objects
import pandas   #Popular data science libraries
from colorama import Fore, Style #Allows color coded responses to terminal/stdout
import welcome
import sys

#Give us a fancy welcome banner :)
welcome.welcomeBanner()

#Get root URL of CKAN Data Portal we want to get data from
print(Fore.LIGHTBLUE_EX + 'Please enter the base URL of the data portal you want to connect to: ')
userDataPortal = input()

#Define packages location at URL path

try:
    packages = '/api/3/action/package_list'
    packagesPath = userDataPortal + packages
    print('The full URL created is: ', packagesPath)
    #Let's make the request for the package list from the desired portal URL
    respose = requests.get(packagesPath)
except:
    print(Fore.RED + 'An error occured with the base URL you provided. Please try again with a base URL.')
    sys.exit()



#Using the JSON module to load the response into a dictionary data structure
response_dict = json.loads(respose.content)

#Check if the contents from the response is valid JSON
try:
    assert response_dict['success'] is True
except AssertionError:
    print("The response was not successful.")

#Titles of the datasets are the key value in the dictionary; this will provide a list of those dataset names
#This extracts just the dataset names from the dictionary data structure
datasets = response_dict['result']

#This prints the names (off by default) of the number of datasets and then the number of datasets (optional - commented out by default)
print("The number of datasets discovered is: ")
packageCount = len(datasets)
print(Fore.YELLOW + "", packageCount)
print("The following datasets were found at the Data Portal you provided: \n")

for key in datasets:
    print(key)

print(type(datasets))

