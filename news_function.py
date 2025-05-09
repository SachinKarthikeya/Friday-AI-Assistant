import requests
import json
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def latest_news():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=e28291177c1d44eeba323789221e170c",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=e28291177c1d44eeba323789221e170c",
            "health" : "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=e28291177c1d44eeba323789221e170c",
            "sports" :"https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=e28291177c1d44eeba323789221e170c",
            "technology" :"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=e28291177c1d44eeba323789221e170c"
}

    content = None
    url = None
    speak("Boss, from which field do you want to hear the latest news?, [business] , [health] , [technology], [sports] , [entertainment]")
    field = input("Type field that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")