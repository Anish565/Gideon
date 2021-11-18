import os
import tkinter as tk
import time
from tkinter.constants import W
top = tk.Tk()
top.geometry("700x700")
top.title("Gideon")
top.iconbitmap("C:\\Users\\Anisn\\Desktop\\codes\\Gideon\\icons\\GideonIcon.ico")
mic_off = tk.PhotoImage(file="C:\\Users\\Anisn\\Desktop\\codes\\Gideon\\icons\\mic_off.png")
mic_on = tk.PhotoImage(file="C:\\Users\\Anisn\\Desktop\\codes\\Gideon\\icons\\mic_on.png")

count = 0
size = 26

def expand(but):
    global count,size
    if count< 10:
        size += 2
        # but.configure(image=mic_on)
    
    # but.configure(image=mic_off)
    pass





mic_button = tk.Button(top,image=mic_off,height=250,width=150,command=lambda : expand(mic_button))
mic_button.pack(pady=150)



top.mainloop()