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
from datetime import date
import Weather as Wr
import ctypes
from Whatsapp import sendMessage
from languagesDB import retrieveCode
from system_calls import *
import translate as t
from languagesDB import retrieveCode,conn
from translate import trans
from random_selector import *



engine = pyttsx3.init('sapi5')

voice = engine.getProperty('voices')
# print(voice)

engine.setProperty('voice', voice[1].id)
engine.setProperty('rate', 150)


# speak("Hello There")
# wishMe()
# while True:
contacts={'afrah':'Afraaaaaaaahhhhhh','ananya':'Ananyaaaaaaaaa','charan':'Charan','anish':'Anish','surya':'Surya','anant':'Anant'}
def CommandActive():
    
    # speak("Hello")
# def CommandActive(event):
    query = listen().lower()
    # query = "play tic tac toe"
    # query="send a message on whatsapp to "
    # query="can yo"
    # query="translate"
    print(query)
    if 'wikipedia' in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        # print(query)
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        speak(results)
        speak("Hope that helped")
    
    elif 'play' == query or 'pause' == query:
        playPause()
    elif 'esc' == query:
        escape()
    elif 'next' == query:
        nextTrack()
    elif 'prev' == query:
        prevTrack()
    elif 'play' in query:
        if 'tic tac toe' in query:
            os.system("start cmd /c python tictac.py")

        
        elif 'music' in query:
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
            receiver = query[query.index('to')+1].lower()
            # speak(receiver)
        else:
            speak("Who do you want to send the message to?")
            receiver = listen().lower()
        speak("What would you like to send to "+receiver)
        m=listen()
        
        name=contacts[receiver]
        sendMessage(name,message=m)
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
            speak("I'm sorry, i didn't quite get that")
    
    elif 'the date' in query:
        try:
            today = date.today()
            speak(today)
        except Exception as e:
            print(e)
            speak("There has been an error")
    elif 'weather in' in query:
        try:
            temp=query.split()
            c=temp[temp.index("weather")+2]
            w=Wr.find_weather(c)
            speak(w)
        except Exception as e:
            print(e)
            speak("There has been an error")    
    elif 'shutdown system' in query:
        try:
            os.system("shutdown /s /t 1")
        except Exception as e:
            print(e)
            speak("There has been an error")
    elif 'restart system' in query:
        try:
            os.system("shutdown /r /t 1")
        except Exception as e:
            print(e)
            speak("There has been an error")    
    elif 'lock the system' in query:
        try:
            ctypes.windll.user32.LockWorkStation()
        except Exception as e:
            print(e)
            speak("There has been an error")    
    
    elif 'translate' in query:
        try:
            speak("Please speak the text you would like to translate")
            te=listen()
            # tt=t.trans(te)
            speak("What language do you want to translate it to?")
            lsp=listen().lower()
            lsp=retrieveCode(conn=conn,lang=lsp)
            speak("The translated text is")
            trans(t=te,frm=None,to=lsp)
            # speak(tt)
        except Exception as e:
            print(e)
            speak("There has been an error")
    
    elif 'random' in query:
        if 'agent' in query:
            speak(valorant())
        elif 'number between' in query:
            speak("Please mention the range of the numbers")
            ##nu = listen()
            nu = "1 and 20"
            randnum = number_selector(nu)
            speak(randnum)
        elif 'guns' in query:
            speak(guns())
    
    elif 'roll a dice' in query:
        speak(dice())

    

    
    elif 'volume' in query:
        try : 
            if "by" in query:
                    query = query.split()
                    count = int(query[query.index("by")+1])
            else:
                count = 1
        except:
            speak("Not sure by how much")
            count = 1

        if 'increase' in query:
            for i in range(count):
                volumeUp()

        elif 'decrease' in query or 'reduce' in query:
            for i in range(count):
                volumeDown()
    elif 'mute' == query:
        volumeMute()
    
    elif 'change' in query:
        if 'window' in query or 'tab' in query:
            windowchange()
        elif 'desktop' in query:
            if 'left' in query:
                desktopchangeLeft()
            elif 'right' in query:
                desktopchangeRight()
        # elif 'tab' in query:
        #     windowchange()
    

    else:
        speak("I didn't get you? could you repeat that")
        CommandActive()
        # print("I'm not capable of doing that yet")


# while True:
#     # command = listen()
#     command="gideon"
#     if "gideon" in command:
# CommandActive()




