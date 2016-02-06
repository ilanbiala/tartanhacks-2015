import requests

r = requests.get('http://apis.scottylabs.org/dining/v1/locations')

d = r.json()