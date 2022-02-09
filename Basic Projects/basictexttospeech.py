print('''Hello and welcome to a basic text to speech program. Kindly ensure that you have installed the 'pyttsx3' module.
Command List - 
1. GOOD MORNING- Basic voice message 
2. QUIT- Stops the program 
3. Have you ever heard the tragedy of Darth Plagueis the Wise ?
4. Tyrion, Do you wish to confess?''')

import sys 
import pyttsx3

text_initialize = pyttsx3.init()
while True :
    user_text = input('Enter text: ')

    if user_text == 'GOOD MORNING' :
        final_text = '''Hello User. My name is Jarvis. I was named after Tony Stark's voice assistant because my owner is very lazy.
        How may I help you?'''
        text_initialize.say(final_text)
        text_initialize.runAndWait()
    elif user_text == 'Have you ever heard the tragedy of Darth Plagueis the Wise ?':
        final_text = '''Did you ever hear the Tragedy of Darth Plagueis the wise? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life... He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. It's ironic he could save others from death, but not himself.'''
        text_initialize.say(final_text)
        text_initialize.runAndWait()
    
    
    elif user_text == 'Tyrion, Do you wish to confess?':
        final_text = '''I saved you all, Tyrion thought. I saved this vile city and all your worthless lives. There were hundreds in the throne room, every one of them laughing but his father. Or so it seemed. Even the Red Viper chortled, and Mace Tyrell looked like to bust a gut, but Lord Tywin Lannister sat between them as if made of stone, his fingers steepled beneath his chin.

Tyrion pushed forward. "MY LORDS!" he shouted. He had to shout, to have any hope of being heard.
His father raised a hand. Bit by bit, the hall grew silent.

"Get this lying whore out of my sight," said Tyrion, "and I will give you your confession."

Lord Tywin nodded, gestured. Shae looked half in terror as the gold cloaks formed up around her. Her eyes met Tyrion's as they marched her from the wall. Was it shame he saw there, or fear? He wondered what Cersei had promised her. You will get the gold or jewels, whatever it was you asked for, he thought as he watched her back recede, but before the moon has turned she'll have you entertaining the gold cloaks in their barracks.

Tyrion stared up at his father's hard green eyes with their flecks of cold bright gold. "Guilty," he said, "so guilty. Is that what you wanted to hear?"

Lord Tywin said nothing. Mace Tyrell nodded. Prince Oberyn looked mildly disappointed. "You admit you poisoned the king?"
"Nothing of the sort," said Tyrion. "Of Joffrey's death I am innocent. I am guilty of a more monstrous crime." He took a step toward his father. "I was born. I lived. I am guilty of being a dwarf, I confess it. And no matter how many times my good father forgave me, I have persisted in my infamy."

"This is folly, Tyrion," declared Lord Tywin. "Speak to the matter at hand. You are not on trial for being a dwarf."

"That is where you err, my lord. I have been on trial for being a dwarf my entire life."

"Have you nothing to say in your defense?"

"Nothing but this: I did not do it. Yet now I wish I had." He turned to face the hall, that sea of pale faces. "I wish I had enough poison for you all. You make me sorry that I am not the monster you would have me be, yet there it is. I am innocent, but I will get no justice here. You leave me no choice but to appeal to the gods. I demand trial by battle."

"Have you taken leave of your wits?" his father said.

"No, I've found them. I demand trial by battle!"'''
        text_initialize.say(final_text)
        text_initialize.runAndWait()
    elif user_text == 'QUIT' :
        final_text = 'Thank You.'
        text_initialize.say(final_text)
        text_initialize.runAndWait()
        text_initialize.exit()
        break
    else :
        final_text = user_text
        text_initialize.say(final_text)
        text_initialize.runAndWait()



