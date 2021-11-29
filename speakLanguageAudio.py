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
    # os.system("mp3 sampleAudio.mp3")
    # playsound.playsound('sampleAudio.mp3',False)
    # pygame.mixer.init()
    # pygame.mixer.music.load('sampleAudio.mp3')
    # pygame.mixer.music.play(999)
    # play_thread = Thread(target=lambda: playsound("sampleAudio.mp3"))
    # play_thread.start()
    # mixer.init()
    # mixer.music.load("sampleAudio.mp3")
    # mixer.music.play()
    # p = multiprocessing.Process(target=playsound,args="sampleAudio.mp3")
    # p.start()
    os.system("start sampleAudio.mp3")
    

# langOutput(None,None)

