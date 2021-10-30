import pyttsx3

engine = pyttsx3.init('sapi5')

voice = engine.getProperty('voices')
# print(voice)

engine.setProperty('voice',voice[1].id)
engine.setProperty('rate',150)
# print(voice[0].id)

# print(voice[1].id)

def input(audio):
    engine.say(audio)
    engine.runAndWait()


input("Hello There")