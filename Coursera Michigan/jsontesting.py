import json
import requests
location = input('Enter your location: ')
apikey = input('Enter your api key: ')
url = "https://api.openweathermap.org/data/2.5/weather?q="+location+"appid="+apikey


data = requests.get(url)
weatherdata = json.loads(data.text)
print(weatherdata)
