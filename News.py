import json
import requests
import pyttsx3

engine = pyttsx3.init('espeak')
engine.setProperty('rate', 105)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

x = requests.get('http://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=becffc3fb30a4bf29dda1d7f63dfcf75')

y = json.loads(x.text)

lst = y['articles']

speak("Here is some news from b b c")
for i in lst:
    speak(f"{lst.index(i) + 1}"+i["description"])
    print("\n")
speak("Thats it for the news, Thank you!")