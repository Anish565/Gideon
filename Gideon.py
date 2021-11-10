import smtplib
import os
import webbrowser
import speech_recognition as s
import datetime,random
import pyttsx3
import wikipedia
from PlayYoutubevideos import playOnYoutube
# import whatsapp as kit

engine = pyttsx3.init('sapi5')

voice = engine.getProperty('voices')
# print(voice)

engine.setProperty('voice',voice[1].id)
engine.setProperty('rate',150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def listen():
    r = s.Recognizer()
    with s.Microphone() as source:
        speak("I'm Listening")
        # print("Listening...")
        # r.phrase_threshold = 0.15
        r.pause_threshold = 0.75
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        speak("hmm")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        i = random.randint(1,2)
        if i == 1:
            speak("I am sorry. I didn't get that")
        elif i == 2:
            speak("Could you repeat that please.")
        return "None"
    return query        



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("email@gmail.com","password")
    server.sendmail("email@gmail.com",to,content)
    server.close()

# def sendwhats(m,n,h,mi):
    
#     kit.sendwhatmsg(n,m,h,mi)

def wishMe():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time <12:
        speak("Good Morning")
    elif time >= 12 and time <4:
        speak("Good Afternoon")
    elif time>= 4 and time <= 7:
        speak("Good Evening")
    else:
        speak("Good Night")

