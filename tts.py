import os
import gtts
from gtts import gTTS

read = 'okay on god bro dont close this hear me out. i know you did some fucky wucky shit right about now.\n' \
         'i know you be tryin to cheat in fortnite. that aint cool bro. you dont have to ruin the game for everyone else homie.\n' \
         'its all good though. since this isnt a bad virus its not like its here to stay. you can just delete this.\n' \
         'dont go download another one tho fr lol.'

language = 'en'

objyo = gTTS(text = read, lang = language, slow = False)

objyo.save("fortnite.mp3")

os.system("fortnite.mp3")
