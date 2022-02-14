import requests , bs4 
url = 'https://www.coursera.org/programs/manipal-education-tguaf?currentTab=CATALOG'
res = requests.get(url)
example_soup = bs4.BeautifulSoup(res.text, 'lxml')
elems = example_soup.select('body')
len_parse = len(elems) 
n = 0 
while n < len_parse :
    print(elems[n].getText())
    n = n + 1