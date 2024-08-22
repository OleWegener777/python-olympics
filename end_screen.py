import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk , Image
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


endscreen = ttk.Window(themename="superhero")
endscreen.title("Python Olympics")
endscreen.geometry("800x1200")

# Read the Image
image = Image.open("win.jpg")
resize_image = image.resize((400, 400))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.image = img
label1.pack(pady=20)

endscreen_text = Text(height="3", width = "50")
endscreen_text.pack()
endscreen_text.insert(END,"         according to score from data ")

play_button = ttk.Button(endscreen,text="Play again", width = 25, command=endscreen.destroy, bootstyle="secondary")
play_button.pack()

play_button = tk.Button(endscreen,text="Exit", width = 25, command=endscreen.destroy)
play_button.pack()


score = Label(endscreen, text = "Score: ")
score.pack()

score = Label(endscreen, text = "Name ")
score.pack()


endscreen.mainloop()