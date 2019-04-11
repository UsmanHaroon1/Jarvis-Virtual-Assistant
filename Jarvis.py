import pyttsx3
import os
import datetime
import smtplib
import webbrowser
import sys
import wolframalpha
import random
import wikipedia
import speech_recognition as sr
import pyaudio

def greetMe():
        currenttime = int(datetime.datetime.now().hour)
        print(currenttime)
        if (0 <= currenttime and currenttime <= 12):
            talk("Good Morning")
        elif(12 < currenttime and currenttime <= 17):
            talk("Good Evening")
        else:
            talk("Good Night")


def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        input = r.listen(source)
    try:
        query = r.recognize_google(input,language='en-in')
        print('I said:' + query)
    except sr.UnknownValueError:
        talk("Sorry sir!,I don't understand.Please type your query")
        query = str(input('Type your question:'))

    return query

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

greetMe()
talk("I am Friday your virtual assistant")

client = wolframalpha.Client("Your Client-ID")

query = myCommand()
query = query.lower()

if 'open google' in query:
    talk('As you wish')
    webbrowser.open("www.google.co.in")
elif 'open youtube' in query:
    talk('Enjoy youtube')
    webbrowser.open("www.youtube.com")
elif 'open my github' in query:
    talk('Opening your profile')
    webbrowser.open("https://github.com/UsmanHaroon1")
elif 'bye friday' or 'by friday' in query:
    talk("See you soon")
    sys.exit()
