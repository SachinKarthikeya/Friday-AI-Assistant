import pyttsx3 
import speech_recognition as sr
import datetime
import os
from search_functions import searchYoutube, searchWikipedia
from weather_function import get_weather_data
from calculator_function import WolfRamAlpha
from calculator_function import Calculator 
from news_function import latest_news
from whatsapp_function import send_message
from rps_function import play_game
from translate_function import translate_text

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            return text
        except sr.UnknownValueError:
            speak("Boss, I did not get you. Say that again.")
            return listen()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon Boss")
    else:
        speak("Good Evening Boss")

if __name__ == "__main__":
    speak("Activating Friday... Welcome back Boss!")  
    
    while True:
        query = listen().lower()
        
        if "morning" in query or "afternoon" in query or "evening" in query:
            greetMe()
            speak("What can I do for you?")

        if "time now" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Boss, the time is {strTime}")

        if "calculate" in query:
            query = query.replace("calculate", "")
            Calculator(query)

        if "weather" in query:
            get_weather_data(query)

        if "youtube" in query:
            searchYoutube(query)

        if "wikipedia" in query:
            searchWikipedia(query)

        if "news" in query:
            latest_news()

        if "whatsapp" in query:
            send_message()

        if "translate" in query:
            query = query.replace("translate","")
            translate_text(query)

        if "remember that" in query:
            rememberMessage = query.replace("friday remember that", "")
            speak("Got it boss")
            with open("Remember.txt", "w") as remember:
                remember.write(rememberMessage)

        if "shutdown the system" in query:
            speak("Boss, are you sure you want to shutdown the device?")
            shutdown = input("Do you want to shutdown the device? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")
            else:
                break

        if "game" in query:
            play_game()

        if "thank you" in query or "catch you" in query:
            speak("You're Welcome Boss! If you have anything, your Friday is always here.")
            break