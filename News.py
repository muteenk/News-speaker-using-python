import json        #importing json module - decoding json data
import requests     #importing request module - get request from newsAPI
import pyttsx3      #importing pyttsx3 module - for speaking

engine = pyttsx3.init('espeak')     #using espeak as speaking engine
# engine = pyttsx3.init("sapi5")    #using sapi5 as speak engine

engine.setProperty('rate', 105)     #speed of speech

#function to hear audio
def speak(audio):
    engine.say(audio)
    #for news subtitles
    print(audio);
    engine.runAndWait()

#using get request from newsAPI
x = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=becffc3fb30a4bf29dda1d7f63dfcf75')

#decoding json data
y = json.loads(x.text)

# list of dictionaries
lst = y['articles']

speak("Here is some news from India")

# using for loop on the list of dictionaries 
for i in lst:
    if(i["description"] == None):
        speak(f"{lst.index(i) + 1} "+i["title"])
    else:
        speak(f"{lst.index(i) + 1} "+i["description"])
    print("\n")
speak("Thats it for the news, Thank you!")