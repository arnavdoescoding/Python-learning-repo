import wikipediaapi
import pyttsx3
import sys



wiki = wikipediaapi.Wikipedia('en')
text_initialize = pyttsx3.init()
text_initialize.setProperty("rate", 200)


while True:
    search_term = input('Enter the search term:')

    if search_term == 'Quit':
        break

    else :

        page = wiki.page(search_term)

        voice_text = wiki.page(page.summary[:200])
        text_initialize.say(voice_text)
        text_initialize.runAndWait()







