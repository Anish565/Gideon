from gtts import gTTS
import os
import multiprocessing, time
from playsound import playsound
# from pygame import mixer
from threading import Thread
def langOutput(text, lang):
    # text = "yo tiene un fiesta que esta muy divertido"

    # lang = "es"
    myobj = gTTS(text,lang=lang,slow=True)
    myobj.save("sampleAudio.mp3")
    os.system("start sampleAudio.mp3")
    

# langOutput(None,None)

