import smtplib
import os
import webbrowser
import speech_recognition as s
import datetime
import random
import pyttsx3
import wikipedia
from PlayYoutubevideos import playOnYoutube
import pywhatkit as kit
from Gideon import *

engine = pyttsx3.init('sapi5')

voice = engine.getProperty('voices')
# print(voice)

engine.setProperty('voice', voice[1].id)
engine.setProperty('rate', 150)


# speak("Hello There")
# wishMe()
# while True:
# def CommandActive():
def CommandActive(event):
    query = listen().lower()
    # query="send a message on whatsapp to Charan"
    # query="can you please open valorant"
    print(query)
    if 'wikipedia' in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        # print(query)
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        speak(results)
        speak("Hope that helped")
    elif 'play' in query:
        if 'music' in query:
            music_dir = "path"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'on youtube' in query:
            query = query.replace("play ", "")
            playOnYoutube(query)
    elif 'open youtube' in query:
        query = query.replace("open youtube", "")
        if query == "":
            webbrowser.open("youtube.com")
        else:
            webbrowser.open(
                "https://www.youtube.com/results?search_query="+query)
    elif 'youtube' in query:
        if 'on' in query:
            query = query.replace("on", "")
        query = query.replace(" youtube", "")
        if query == "":
            webbrowser.open("youtube.com")
        else:
            webbrowser.open(
                "https://www.youtube.com/results?search_query="+query)
    elif 'google' in query:
        query = query.replace("google", "")
        webbrowser.open("https://www.google.com/search?q="+query)

    elif 'time' in query:
        nowTime = datetime.datetime.now().strftime("%H:%M%p")
        speak(f"The time is {nowTime}")
    elif 'open code' in query:
        codepath = "C:\\Users\\Anisn\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
        os.startfile(codepath)
    elif 'send email' in query:
        try:
            speak("What should i send?")
            content = listen()
            to = "anishnimbalkar@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("There has been an error.")
    elif 'whatsapp' in query:
        # try:

        query = query.split(" ")
        if 'to' in query:
            receiver = query[query.index('to')+1]
            # speak(receiver)
        else:
            speak("Who do you want to send the message to?")
            receiver = listen()
        speak("What would you like to send to "+receiver)
        # m=listen()
        m = "why doesn't this shit work"
        print(m)
        kit.sendwhatmsg(
            "+919618152076", m, datetime.datetime.now().hour, datetime.datetime.now().minute+1)

        # except:
        # speak("I'm sorry, I didn't get you bro")

    elif 'open word' in query:
        try:
            os.startfile('winword')
        except Exception as e:
            print(e)
            speak("There has been an error")
    elif 'open powerpoint' in query:
        try:
            os.startfile('powerpnt')
        except Exception as e:
            print(e)
            speak("There has been an error")

    elif 'open' in query:
        try:
            temp = query.split()
            os.startfile(temp[temp.index("open")+1])
        except Exception as e:
            print(e)
            speak("I'm sorry, fuck you")

    else:
        speak("I'm not capable of doing that yet")
        print("I'm not capable of doing that yet")


# while True:
#     # command = listen()
#     command="gideon"
#     if "gideon" in command:
# CommandActive()
