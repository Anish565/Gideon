import pyautogui

def close():
    pyautogui.keyDown("alt")
    pyautogui.keyDown("f4")
    pyautogui.keyUp("alt")


def windowchange():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")

def escape():
    pyautogui.press("esc")

    
def desktopchangeLeft():
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("win")
    pyautogui.press("left")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("win")

def desktopchangeRight():
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("win")
    pyautogui.press("right")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("win")

def volumeUp():
    pyautogui.press("volumeup")

def volumeDown():
    pyautogui.press("volumedown")
def volumeMute():
    pyautogui.press("volumemute")

def playPause():
    pyautogui.press("playpause")

def nextTrack():
    pyautogui.press("nexttrack")

def prevTrack():
    pyautogui.press("prevtrack")


