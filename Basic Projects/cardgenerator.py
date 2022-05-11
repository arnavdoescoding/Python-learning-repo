from playcardsrds import Deck , Card
import random 

while True:
    call = input('Enter N to terminate: ')
    if call == '':

        deck_numeral = random.randint(0,13) 
        suit_numeral = random.randint(0 , 3)
        player_card = Card ( value= deck_numeral , suit= suit_numeral )
        print(player_card.img)
        continue
    else:
        break
