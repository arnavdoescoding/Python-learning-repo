import json 
import requests
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=Manipal&cnt=3&APPID=1dcea30702916829672a4fe063886231'

data = requests.get(url)
print(data.text)