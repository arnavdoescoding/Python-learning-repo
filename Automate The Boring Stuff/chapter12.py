import requests 
url = 'https://automatetheboringstuff.com/files/rj.txt'
res = requests.get(url)
new_file = open('Romeo and Juliet.txt', 'wb')
for chunk in res.iter_content(100000):
    new_file.write(chunk)
new_file.close()