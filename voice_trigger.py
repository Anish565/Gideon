
from Gideon import listen
from Main import CommandActive


TRIGGER_WORD = "gideon"

while True:
    text = listen().lower()

    if text.count(TRIGGER_WORD) > 0:
        CommandActive()