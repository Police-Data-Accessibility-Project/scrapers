import requests
import json
import jmespath

# Search for existing datasets
owner, repo, branch = 'pdap', 'datasets', 'master'
state_iso = "CA"
city_input = "Los Angeles"
query = '''SELECT id, name, city, state_iso, homepage_url FROM `agencies` WHERE `state_iso` = "{}" and city = "{}"'''.format(state_iso, city_input)
# print(query)
res = requests.get('https://www.dolthub.com/api/v1alpha1/{}/{}/{}'.format(owner, repo, branch), params={'q': query})
jsoned = res.json()
# print(json.dumps(jsoned, indent=4))
# rows_expression = jmespath.compile('rows[].["id", "name","city","state_iso", "homepage_url"]')
# Filter out everything except the "rows" table
expression = jmespath.compile("rows[]")
searched = expression.search(jsoned)
print(json.dumps(searched, indent=4))
