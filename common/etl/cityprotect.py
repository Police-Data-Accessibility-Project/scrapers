'''
CityProtect Wrapper for API
https://github.com/EricTurner3
'''

import requests
import json

def fetch_agencies():
    url = "https://ce-portal-service.commandcentral.com/api/v1.0/public/agencies"
    print(" [*] Fetching agencies from {}".format(url))

    payload="{\"limit\":15000,\"offset\":0,\"geoJson\":{\"type\":\"MultiPolygon\",\"coordinates\":[[[[-180,90],[0,90],[0,-90],[-180,-90],[-180,90]]],[[[0,90],[180,90],[180,-90],[0,-90],[0,90]]]]},\"projection\":false,\"propertyMap\":{}}"
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    json_resp = json.loads(response.text)
    print(' [*] Agency List Fetched! {} agencies found'.format(len(json_resp['result']['list'])))
    return json_resp['result']['list']

'''
All the bulk download files are formatted as such:
crapiID_fromdate-todate.csv
so we can pass the crapiID to here and locate it from the full data dump of above
'''
def get_agency_by_crapiId(agencies, crapiID):
    for agency in agencies:
        if 'crapiId' in agency:
            if agency['crapiId'] == crapiID:
                print(' [!] Found Agency #{} - {} - {},{}'.format(agency['crapiId'], agency['name'], agency['city'], agency['state']))
                return agency
                
    return None # if not found