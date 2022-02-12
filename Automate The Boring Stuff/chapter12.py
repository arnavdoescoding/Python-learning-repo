import requests , bs4 
url = 'https://www.jimcornette.com/'
res = requests.get(url)
example_soup = bs4.BeautifulSoup(res.text, 'lxml')
elems = example_soup.select('#js-SFNT > header > section')
print(elems[0].getText())