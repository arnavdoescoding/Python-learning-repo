import json
import requests
import urllib.request , urllib.parse , urllib.error

address = input('Enter the address: ')
api_key = '42'
base_url = 'http://py4e-data.dr-chuck.net/json?'

params =  { 
          'key' : api_key,
          'address' : address}
url = base_url + urllib.parse.urlencode(params)
uh = urllib.request.urlopen(url)
data1 = uh.read().decode()
js = json.loads(data1)
          

request = requests.get(base_url , params= params).json()
palcer = request['results'][0]['place_id']
print(palcer)
