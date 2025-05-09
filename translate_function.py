import pyttsx3
from gtts import gTTS
from googletrans import Translator, LANGUAGES
import os
import time
from playsound import playsound

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def translate_text(query):
    speak("Of course, Boss!")
    print(LANGUAGES)
    translator = Translator()
    speak("Boss, choose the language code to which you want to translate.")
    target_language = input("Enter the Language code: ").lower()

    try:
        translated = translator.translate(query, src="auto", dest=target_language)
        text = translated.text
        print(f"Translated Text: {text}")

        speakgl = gTTS(text=text, lang=target_language, slow=False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")

        time.sleep(5)
        os.remove("voice.mp3")

    except Exception as e:
        speak("Boss, unable to translate.")
        print(f"Error: {e}")