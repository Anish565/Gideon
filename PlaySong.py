import webbrowser
import pyautogui as pg

def playSong(song):
    # song = song.()
    width, height = pg.size()
    webbrowser.open("https://open.spotify.com/search/" + song)
    pg.click(width*0.4, height - height / 10)

# playSong("Shape of you")