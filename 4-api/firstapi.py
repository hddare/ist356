'''curl -X 'GET' \
  'https://cent.ischool-iot.net/api/funnyname/random?n=3' \
  -H 'accept: application/json'''

import requests
url = "https://cent.ischool-iot.net/api/funnyname/search"
querystring = {"q":"Mi"}
response = requests.get(url, params=querystring)
print(response.url)
names = response.json()
for name in names:
    print(name['first'], name['last'])
