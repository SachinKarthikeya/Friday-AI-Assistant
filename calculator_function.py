import pyttsx3
import wolframalpha

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def WolfRamAlpha(query):
    apikey = "8GE525-LA563PGXTU"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except StopIteration:
        speak("Boss! I couldn't find an answer to this query.")
        return None
    except Exception as e:
        speak("Boss! An error occurred while fetching the result.")
        print(f"Error: {e}")
        return None

def Calculator(query):
    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")

    print(f"Modified Query: {Term}")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        if result:
            print(result)
            speak(f"Boss, the result of your calculation came out to be {result}")
        else:
            speak("Sorry boss, I couldn't calculate the result.")
    except Exception as e:
        speak("Boss! There was an error calculating the value.")
        print(f"Error: {e}")