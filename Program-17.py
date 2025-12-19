# This program reads aloud the text entered by the user.

import pyttsx3

engine = pyttsx3.init()

text = input("Enter the text : ")

engine.say(text)

engine.runAndWait()
