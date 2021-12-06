
from Gideon import listen, speak
from Main import CommandActive


TRIGGER_WORD = "gideon"
# TRIGGER_WORD = "jarvis"

while True:
    text = listen().lower()

    if text.count(TRIGGER_WORD) > 0:
        speak("Hello")

        CommandActive()