from tkinter import *
from tkinter import ttk
from playsound import playsound
from PIL import ImageTk, Image

def talk():
    playsound("how-about-no.mp3")

root = Tk()
root.title("No Button")

photo = ImageTk.PhotoImage(Image.open("nobutton.jpeg"))

button = ttk.Button(root, command=talk)
button.config(image=photo)
button.pack()

root.mainloop()