import json
import requests

address = input('Enter the address: ')
api_key = 'AIzaSy___IDByT70'
base_url = 'http://py4e-data.dr-chuck.net/json?'

params =  { 
          'key' : api_key,
          'address' : address}

request = requests.get(base_url , params= params).json()
request.keys()

print(request)