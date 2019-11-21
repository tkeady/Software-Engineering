import http.client
import requests
import json

conn = http.client.HTTPSConnection("api.sportradar.us")

# Test to retrieve driver info
url = requests.get('https://api.sportradar.us/formula1/trial/v2/en/competitors/sr:competitor:7135/profile.json?api_key=wb825w3qegqenjt95ue3muut')
data = json.dumps(url.json(), indent=4)
print(data)


