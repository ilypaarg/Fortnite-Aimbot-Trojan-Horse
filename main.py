import time
import random
import sys
import os
import enum
from enum import Enum
import array
import json
import pymsgbox
import ctypes
from os import system
import numpy
import numpy as np
import logging
import datetime
from datetime import datetime
import colorama
from colorama import Fore, Style
import webbrowser
import pynput
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import gtts
from gtts import gTTS

date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")

title = "The Fortnite Aimbot [Awaiting Authentication]..."

system("title " + title)

os.system('cls')

print(Fore.WHITE + "Acces key: 'public' ")
time.sleep(1)
pymsgbox.alert('You need an access key in order to access the Fortnite Aimbot \n Public key: public', 'WARNING!')
response = pymsgbox.prompt('Please enter the access key: ')
if response == "public" or "Public":
    pass
else:
    print(Fore.RED + "invalid key, closing.")
    exit()

title1 = "The Fortnite Aimbot [AUTHENTICATED]..."
os.system("title " + title1)
#carray = np.chararray((3, 3))
#carray[:] = 'a'
# Character array:
#[[b'a' b'a' b'a']
 #[b'a' b'a' b'a']
 #[b'a' b'a' b'a']]

logging.basicConfig(format = '%(asctime)s %(message)s', filename = 'logs.log', encoding = 'utf-8', level = logging.DEBUG)
logging.debug(' Launched... ' + "[DEBUG]")
x = '{ "application":"Fortnite Aimbot v1.0 [Stable]", "version":"v1.0", "status":"[Status]: active", "status2":"[Status]: running", "status3":"[Status]: closed"}'
y = json.loads(x)
logging.debug(' JSON Parsed [COMPLETED SUCCESSFULLY]... ' + "[DEBUG]")
os.system('pause')
print(y["status"] + " " + Fore.GREEN + "(^-^)")
logging.debug(' Application status sent... ' + "[DEBUG]")
for activity in range(5):
    print(Fore.LIGHTRED_EX + "(?_?) " + Fore.WHITE + "Thinking...")
    time.sleep(0.5)
    os.system('cls')
    print(Fore.LIGHTGREEN_EX + "(?_?) " + Fore.WHITE + "Thinking...")
    time.sleep(0.5)
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + "(?_?) " + Fore.WHITE + "Thinking...")
    time.sleep(0.5)
    os.system('cls')

time.sleep(1)
print(Fore.WHITE + "[!] " + Fore.LIGHTRED_EX + "DONE! " + Fore.LIGHTGREEN_EX + "(^_^)")
time.sleep(2)
title2 = "Fortnite Aimbot " + Fore.WHITE + "[ " + Fore.LIGHTRED_EX + "INJECTION READY " + Fore.WHITE + "]"
os.system('title ' + title2)
time.sleep(1)
os.system('cls')
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "Reparsing JSON, Standby.")
time.sleep(1)
print(Fore.LIGHTRED_EX + str(y))
logging.debug(' { "application":"Fortnite Aimbot v1.0 [Stable]", "version":"v1.0", "status":"[Status]: active", "status2":"[Status]: running", "status3":"[Status]: closed"} ' + "[DEBUG]")
time.sleep(2)
os.system('cls')
print(Fore.GREEN + "(0_0) " + Fore.WHITE + "Operation completed successfully!")
time.sleep(2)
os.system('cls')

# MAIN AREA FOR TROLL
f = open("logs.log", "r")
logging.debug(' Injecting main args... ')
time.sleep(0.08)
logging.debug(' File directories found... ')
time.sleep(0.08)
logging.debug(' Injecting dynamic link libraries... ')
time.sleep(0.08)
logging.debug(' Adding to PATH... ')
time.sleep(0.08)
logging.debug(' Reloading dependencies... ')
time.sleep(0.08)
logging.debug(' Creating blob storage... ')
time.sleep(0.08)
logging.debug(' Emptying libraries... ')
time.sleep(0.08)
logging.debug(' Including dynamic strings... ')
time.sleep(0.08)
logging.debug(' Excluding static strings... ')
time.sleep(0.08)
logging.debug(' Patching old files... ')
time.sleep(0.08)
logging.debug(' Destroying constructors... ')
time.sleep(0.08)
logging.debug(' Opening locations... ')
time.sleep(0.08)
logging.debug(' Finding args... ')
time.sleep(0.08)
logging.debug(' Injection concluded... ')
time.sleep(3)
os.system('cls')

print(Fore.WHITE + "Press any key to start the Fortnite hacks.")
os.system('pause')
logging.debug(' Launched "cheats"... ')
time.sleep(1)
url1 = "https://www.fortnite.com"
url2 = "https://www.virustotal.com/gui/"

for w in range(10):
    time.sleep(1)
    webbrowser.open(url1)
    time.sleep(1)
    webbrowser.open_new(url2)
    time.sleep(1)

os.startfile('Notepad.exe')
logging.debug(' creating dummy window to bait priority... ')
pymsgbox.alert('', '')
logging.debug(' Launched Notepad... ')
keyboard = Controller()


def type_string_in_notepad(string):
    for character in string:
        keyboard.type(character)
        delay = random.uniform(0.08, 0.09)
        time.sleep(delay)

    logging.debug(' Getting ready to type... ')
    type_string_in_notepad("Why would you download this? I mean really, is cheating that important to you?\n"
                           "It's not like you're going to wake up one day and be just shit at the game is it?\n"
                           "Well, if I'm being honest, you are since you're trying to cheat. But whatever.\n"
                           "I don't ever want to see you download something like this again. Got it?")

time.sleep(3)
logging.debug(' TTS reading... ')
read = 'okay on god bro dont close this hear me out. i know you did some fucky wucky shit right about now.\n' \
         'i know you be tryin to cheat in fortnite. that aint cool bro. you dont have to ruin the game for everyone else homie.\n' \
         'its all good though. since this isnt a bad virus its not like its here to stay. you can just delete this.\n' \
         'dont go download another one tho fr lol.'

language = 'en'

objyo = gTTS(text = read, lang = language, slow = False)
logging.debug(' Preparing to save audio file... ')

objyo.save("fortnite.mp3")
logging.debug(' audio file saved... ')
logging.debug(' opening audio file... ')

os.system("fortnite.mp3")
logging.debug(' audio file opened... ')

time.sleep(3)

logging.debug(' Starting clicking thread... ')
delay = 0.001
button = Button.left
start_stop_key = KeyCode(char = 'n')
exit_key = KeyCode(char = 'o')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            mouse.click(self.button)
            time.sleep(self.delay)
        time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press = on_press) as listener:
    listener.join()
logging.debug(y['status3'] + '...')
logging.debug(' program aborted... ')








