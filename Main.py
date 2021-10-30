import smtplib
import os
import webbrowser
import speech_recognition as s
import datetime,random
import pyttsx3
import wikipedia

engine = pyttsx3.init('sapi5')

voice = engine.getProperty('voices')
print(voice)

engine.setProperty('voice',voice[1].id)
engine.setProperty('rate',150)


def output(audio):
    engine.say(audio)
    engine.runAndWait()


def input():
    r = s.Recognizer()
    with s.Microphone() as source:
        output("I'm Listening")
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)

    try:
        # output("hmm")
        query = r.recognize_google(audio, language='en-us')
        print(query)
    except Exception as e:
        i = random.randint(1,2)
        if i == 1:
            output("I am sorry. I didn't get that")
        elif i == 2:
            output("Could you repeat that please.")
        return "None"
    return query        



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("email@gmail.com","password")
    server.sendmail("email@gmail.com",to,content)
    server.close()

def wishMe():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time <12:
        output("Good Morning")
    elif time >= 12 and time <4:
        output("Good Afternoon")
    elif time>= 4 and time <= 7:
        output("Good Evening")
    else:
        output("Good Night")



# output("Hello There")
# wishMe()
# while True:
if 1:
    query = input().lower()

    if 'wikipedia' in query:
        output("Searching Wikipedia")
        query = query.replace("wikipedia","")
        # print(query)
        results = wikipedia.summary(query, sentences=2)
        output("So according to wikipedia")
        output(results)
        output("Hope that helped")

    elif 'open youtube' in query:
        query = query.replace("open youtube","")
        if query == "":
            webbrowser.open("youtube.com")
        else:
            webbrowser.open("https://www.youtube.com/results?search_query="+query)
    elif 'youtube' in query:
        query = query.replace("youtube","")
        if query == "":
            webbrowser.open("youtube.com")
        else:
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
        output(f"The time is {nowTime}")
    elif 'open code' in query:
        codepath = "C:\\Users\\Anisn\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
        os.startfile(codepath)
    elif 'send email' in query:
        try:
            output("What should i send?")
            content = input()
            to = "anishnimbalkar@gmail.com"
            sendEmail(to, content)
            output("Email has been sent")
        except Exception as e:
            print(e)
            output("There has been an error.")

