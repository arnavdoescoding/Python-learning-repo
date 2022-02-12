import requests 
url = 'https://automatetheboringstuff.com/files/rj.txt'
res = requests.get(url)
len_text = len(res.text)
print(len_text)
print(res.text[: 2000 ])