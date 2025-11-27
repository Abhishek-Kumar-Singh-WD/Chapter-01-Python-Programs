# This program speaks the given text.

import pyttsx3

engine = pyttsx3.init()

text = "My name is Abhishek Kumar Singh. I am from India."

engine.say(text)

engine.runAndWait()
