import requests
#supabase
#local env 

url="https://services.pacourts.us/public/v1/cases/MJ-05213-LT-0000011-2021"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
#what is user agent


resp = requests.get(url, headers=headers)
print(resp.json())