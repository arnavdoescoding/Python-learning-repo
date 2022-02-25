import wikipediaapi
import requests
import  json


wiki = wikipediaapi.Wikipedia('en')
search_term = input('Enter the search term:')
page = wiki.page(search_term)

print(page.text)