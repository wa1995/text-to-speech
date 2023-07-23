#First Install 'pip install pyttsx3'

import pyttsx3

s = input("Enter anything to speech")

engine = pyttsx3.init()
engine.say(s)
engine.runAndWait()