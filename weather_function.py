import pyttsx3
import json
import requests

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_weather_data(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=39165204343341cb853163540230506&q={city}"

    response = requests.get(url)
    response.raise_for_status()
    weather_data = json.loads(response.text)

    try:
        t = weather_data['current']['temp_c']
        c = weather_data['current']['condition']['text']
        h = weather_data['current']['humidity']
        w = weather_data['current']['wind_kph']
        d = weather_data['current']['wind_dir']
        p = weather_data['current']['pressure_mb']
        v = weather_data['current']['vis_km']

        result = (f"{city}'s Temperature: {t} degrees\n"
                f"Humidity: {h}\n"
                f"Wind Speed: {w} kilometers per hour towards {d} direction\n"
                f"Pressure: {p}mb/n\n"
                f"Visibility: {v} km")
        
        print(result)
        speak(f"Boss, The current weather status of {city} is {t} degrees recorded and {c} with {h} humidity, {p} pressure, {v} kilometers visibility recorded and the wind speed of {w} kilometers per hour towards {d} direction.")

    except requests.exceptions.HTTPError as e:
        return f"Error: {e.response.status_code} - {e.response.reason}"