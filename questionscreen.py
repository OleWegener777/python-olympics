import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk , Image


questionscreen = tk.Tk()
questionscreen.title("Python Olympics")
questionscreen.geometry("800x1200")

# Read the Image
image = Image.open("compete2.png")
resize_image = image.resize((400, 400)) 
img = ImageTk.PhotoImage(resize_image) 
label1 = Label(image=img)
label1.image = img
label1.pack(pady=20)

quote_text = Text(height="1", width = "50")
quote_text.pack()
quote_text.insert(END,"         ''random quote from data'' ")

question_text = Text(height="5", width = "80")
question_text.pack(pady = 40)
question_text.insert(END,"         ''random quote from data'' ")

score = Label(questionscreen, text = "Score ")
score.pack()

score = Label(questionscreen, text = "Name ")
score.pack()

Answer_button_1 = tk.Button(questionscreen,text="Play again", width = 25, command=questionscreen.destroy)
Answer_button_1.pack()
Answer_button_2 = tk.Button(questionscreen,text="Play again", width = 25, command=questionscreen.destroy)
Answer_button_2.pack()
Answer_button_3 = tk.Button(questionscreen,text="Play again", width = 25, command=questionscreen.destroy)
Answer_button_3.pack()
Answer_button_4 = tk.Button(questionscreen,text="Play again", width = 25, command=questionscreen.destroy)
Answer_button_4.pack()

#style = Style(frame)
#style.configure("TRadiobutton", background = "blue", 
 #               foreground = "white", font = ("arial", 24, "bold"))


def question_screen():
    questionscreen = tk.Tk()
    questionscreen.title("Python Olympics")
    questionscreen.geometry("800x1200")

    questionscreen.mainloop()
    
if __name__ == "__main__":
    question_screen()