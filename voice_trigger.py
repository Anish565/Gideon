
from Gideon import listen, speak
from Main import CommandActive


TRIGGER_WORD = "hey raju"


while True:
    text = listen().lower()

    if text.count(TRIGGER_WORD) > 0:
        speak("Hello")

        CommandActive()