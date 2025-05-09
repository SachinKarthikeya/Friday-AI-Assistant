import pyttsx3
import pywhatkit
import webbrowser
import wikipedia

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def searchYoutube(query):
        speak("Boss!! This is what I found")
        query = query.replace("youtube", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)

def searchWikipedia(query):
        print("Searching from Wikipedia..")
        query = query.replace("wikipedia", "").strip()
        if query:
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("Boss, according to Wikipedia..")
                print(results)
                speak(results)  
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Boss, there are multiple results. Be more specific.")
                print(f"DisambiguationError: {e}")
            except wikipedia.exceptions.PageError as e:
                speak("Boss, I could not find your query.")
                print(f"PageError: {e}")
            except Exception as e:
                speak("Boss, an error occured while searching")
                print(f"Exception: {e}")
        else:
             speak("Boss! could you please provide with a specific query?")