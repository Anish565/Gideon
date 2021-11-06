import pywhatkit as kit



def playOnYoutube(phrase):
    # phrase = listen()
    phrase = phrase.replace("on youtube","")
    kit.playonyt(phrase)


# state = "play winui 3 tutorial on youtube"
# state.replace("play ","")
# playOnYoutube(state)