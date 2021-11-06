import smtplib
import os
import webbrowser
import speech_recognition as s
import datetime,random
import pyttsx3
import wikipedia
from PlayYoutubevideos import playOnYoutube
import whatsapp as kit
from Gideon import *

engine = pyttsx3.init('sapi5')

voice = engine.getProperty('voices')
# print(voice)

engine.setProperty('voice',voice[1].id)
engine.setProperty('rate',150)



# speak("Hello There")
# wishMe()
# while True:
def CommandActive():
    query = listen().lower()
    # query="send a message on whatsapp to Charan"

    if 'wikipedia' in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia","")
        # print(query)
        results = wikipedia.summary(query, sentences=2)
        speak("So according to wikipedia")
        speak(results)
        speak("Hope that helped")

    elif 'open youtube' in query:
        query = query.replace("open youtube","")
        if query == "":
            webbrowser.open("youtube.com")
        else:
            webbrowser.open("https://www.youtube.com/results?search_query="+query)
    elif 'youtube' in query:
        if "play" in query:
            query = query.replace("play ","")
            playOnYoutube(query)
        query = query.replace(" youtube","")
        if query == "":
            webbrowser.open("youtube.com")
        else:
            query = query[:-3]
            webbrowser.open("https://www.youtube.com/results?search_query="+query)
    elif 'google' in query:
        query = query.replace("google","")
        webbrowser.open("https://www.google.com/search?q="+query)
    elif 'play music' in query:
        music_dir = "path"
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    elif 'the time' in query:
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
        try:
            query=query.split(" ")
            if 'to' in query:
                receiver=query[query.index('to')+1]
                speak(receiver)
            else:
                speak("Who do you want to send the message to?")
                receiver=listen()
            speak("What would you like to send to "+receiver)
            m=listen()
            print(m)
            kit.sendwhatmsg("+919618152076",m,datetime.datetime.now().hour,datetime.datetime.now().minute+1)

        except:
            speak("I'm sorry, I didn't get you")

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
    elif 'open excel' in query:
        try:
            os.startfile('excel')
        except Exception as e:
            print(e)
            speak("There has been an error")
    elif 'open outlook' in query:
        try:
            os.startfile('outlook')
        except Exception as e:
            print(e)
            speak("There has been an error")

    
            





while True:
    command = listen()
    if "gideon" in command:
        CommandActive()