import pyttsx3
import pywhatkit
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
import datetime
from datetime import datetime
from datetime import timedelta

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def send_message():
    speak("Boss, what do you want to send?")
    a = int(input('''Person 1 -1 
    Person 2 -2'''))
    if a == 1:
        speak("Boss, what is the message?")
        message = str(input("Enter the message: "))
        pywhatkit.sendwhatmsg("+919701808528",message, time_hour=strTime, time_min=update)
    elif a == 2:
        pass