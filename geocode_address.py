# using census to geocode address
# ttps://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html
# https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=4600+Silver+Hill+Rd%2C+Suitland%2C+MD+20746&benchmark=9&format=json

import json
import requests

address = '1600 Amphitheatre Parkway, Mountain View, CA'

base_uri = 'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address='
term_uri = '&benchmark=9&format=json'

# process address
address = address.replace(' ', '+').replace(',', '')
request_uri = base_uri + address + term_uri

# get address info from the Census
response = requests.get(request_uri)

json_response = json.loads(response.text)

lat = json_response['result']['addressMatches'][0]['coordinates']['y']
lon = json_response['result']['addressMatches'][0]['coordinates']['x']

print(lat)
print(lon)
