from gtts import gTTS
import os

def langOutput(text, lang):
    # text = "yo tiene un fiesta que esta muy divertido"

    # language = "es"
    myobj = gTTS(text,lang=lang,slow=True)
    myobj.save("sampleAudio.mp3")
    os.system("start sampleAudio.mp3")