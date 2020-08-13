from tkinter import *
from tkinter import ttk
from playsound import playsound
from PIL import ImageTk, Image

def talk():
    while(True):
        playsound("annoying.mp3", block=False)

root = Tk()
root.title("Easy Button")

photo = ImageTk.PhotoImage(Image.open("jpgbutton.jpg"))

button = ttk.Button(root, command=talk)
button.config(image=photo)
button.pack()

root.mainloop()
