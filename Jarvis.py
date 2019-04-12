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
            talk("Good Afternoon")
        else:
            talk("Good Evening")


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
        strquery = input('Type your question:')
        query = str(strquery)

    return query

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

greetMe()
today = datetime.datetime.now()
text = "Today is" + str(today.strftime("%A"))

talk(text)
talk("I am Friday your virtual assistant")

client = wolframalpha.Client("App_ID")

while True:
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
    elif "what\'s up" in query or 'how are you' in query:
        Msgs = ['I am always fine', 'ya good!', 'Awesome', 'I am nice and full of energy']
        talk(random.choice(Msgs))
    elif 'bye friday' in query or 'by friday' in query:
        talk("Bye man")
        sys.exit()
    elif 'stop' in query or 'abort' in query:
        talk('Bye Sir, have a good day.')
        sys.exit()
    else:
        query = query
        print("Searching Query:" + query)
        talk("Searching")
        try:
            try:
                res = client.query(query)
                result = next(res.results).text
                talk("Jarvis says")
                talk(result)
            except:
                result = wikipedia.summary(query,sentences=2)
                talk("Wiki says")
                talk(result)
        except:
            webbrowser.open("www.google.co.in")

    talk("Next command")
