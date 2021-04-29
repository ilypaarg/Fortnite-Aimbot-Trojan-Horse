import os
import time
import pynput
import random
from pynput.keyboard import Controller
import pymsgbox

os.startfile('Notepad.exe')
pymsgbox.alert('','')
keyboard = Controller()


def type_string_in_notepad(string):
    for character in string:
        keyboard.type(character)
        delay = random.uniform(0.08, 0.09)
        time.sleep(delay)


type_string_in_notepad("Why would you download this? I mean really, is cheating that important to you?\n"
                       "It's not like you're going to wake up one day and be just shit at the game is it?\n"
                       "Well, if I'm being honest, you are since you're trying to cheat. But whatever.\n"
                       "I don't ever want to see you download something like this again. Got it?")
