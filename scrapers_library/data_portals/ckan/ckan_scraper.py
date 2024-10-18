#import pprint
#import requests
import json
#import pandas 
#from colorama import Fore, Style
import sys
from ckanapi import RemoteCKAN

remote = RemoteCKAN("https://catalog.data.gov/", get_only=True)
packages = remote.action.package_list(fq="tags:police", rows=1000)
print(len(packages["results"]))
input()


try:
    packages = '/api/3/action/package_list?fq=tags:police&rows=10000'
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
datasets = response_dict['result']['results']

#This prints the names (off by default) of the number of datasets and then the number of datasets (optional - commented out by default)
print("The number of datasets discovered is: ")
packageCount = len(datasets)
print(Fore.YELLOW + "", packageCount)
print("The following datasets were found at the Data Portal you provided: \n")

for key in datasets:
    continue
    print(key)

#This is to help provide degugging information as to the type of data the datasets variable is (list vs. dictionary vs. dataframe, etc)
print(type(datasets))

