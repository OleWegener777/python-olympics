import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json
import random


# function to load and save from and to json

def load_data(filename):
    with open(filename, "r") as file:
        contents = file.read()
        content = json.loads(contents)
    return content


def write_to_json(data, json_file: str) -> None:

    from json import dumps

    with open(json_file, "w") as file:
        contents = dumps(data, indent=2)
        file.write(contents)


data = load_data("data.json")
highscores = load_data("highscores.json")

# some variables to start

text = "                      Welcome to Python Olympics! \n       Compete with the best Python coders for the win!\n "
text_quote = "      The Pythonian Decathlon is on, earn your medal!"
round_no = 0
scorecount = 0
name = ""
current_difficulty = "easy"
current_question = ""
used_answers = []


# tkinter main window with theme

root = ttk.Window(themename="superhero")
root.title("Python Olympics")
root.geometry("800x1200")

# start image
image = Image.open("start.jpeg")
resize_image = image.resize((400, 400))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.image = img
label1.grid(row=2, column=2, pady=20)

# Questions image

image2 = Image.open("compete2.png")
resize_image = image2.resize((300, 300))
img2 = ImageTk.PhotoImage(resize_image)
label2 = Label(image=img2)
label2.image2 = img2


# end screen image

image3 = Image.open("win.jpg")
resize_image = image3.resize((400, 400))
img3 = ImageTk.PhotoImage(resize_image)
label3 = Label(image=img3)
label3.image3 = img3

intro_text = Text(height="3", width="48")
intro_text.grid(row=3, column=2)
intro_text.insert(END, text)

question_text = Text(height=10, width=60)

# starting the quiz , changing tkinter pictures and elements

def start():
    global current_question
    global text_quote
    current_question = get_question(current_difficulty)
    label1.grid_forget()
    label2.grid(row=2, column=2, pady=20)
    intro_text.delete(1.0, END)
    intro_text.insert(END, text_quote)
    play_button.grid_forget()
    question_text.grid(row=4, column=2, pady=10)
    question_text.delete(1.0, END)
    question_text.insert(END, current_question["question"])
    intro_text.configure(height=1)
    frame.grid(row=5, column=2, pady=10)
    Answer_button_1.grid(row=1, column=1)
    Answer_button_2.grid(row=1, column=2)
    Answer_button_3.grid(row=2, column=1, pady=20)
    Answer_button_4.grid(row=2, column=2, padx=20)
    Answer_button_1.config(text=current_question["options"][0])
    Answer_button_2.config(text=current_question["options"][1])
    Answer_button_3.config(text=current_question["options"][2])
    Answer_button_4.config(text=current_question["options"][3])
    fifty_fifty_joker.grid(row=2,column=3)
    new_joker.grid(row=2,column=1)
# tkinter elements 

play_button = tk.Button(root, text="Play", width=60, height=10, command=start)
play_button.grid(row=4, column=2, pady=60)

score = Label(root, text=f"Score: {str(scorecount)}", width=13)
score.grid(row=1, column=1, padx=20, pady=20)

name_entry = Entry(root, state="cc", width=12)
name_entry.grid(row=1, column=3, padx=20, pady=20)

image4 = Image.open("fiftyfifty.jpeg")
resize_fifty = image4.resize((75, 75))
fifty = ImageTk.PhotoImage(resize_fifty)

image4 = Image.open("new.png")
resize_new = image4.resize((75, 75))
new = ImageTk.PhotoImage(resize_new)

def fifty_fifty():
    fifty_fifty_joker.grid_forget()
    count = 0
    if current_question["options"][0] != current_question["answer"]:
        Answer_button_1.grid_forget()
        count += 1
    if current_question["options"][1] != current_question["answer"]:
        Answer_button_2.grid_forget()
        count +=1
    if count == 2 :
        return
    if count == 1 :
        Answer_button_3.grid_forget()
        
    

def question_joker():
    global current_question
    new_joker.grid_forget()
    current_question = get_question(current_difficulty)
    intro_text.delete(1.0, END)
    intro_text.insert(END, text_quote)
    question_text.delete(1.0, END)
    question_text.insert(END, current_question["question"])
    Answer_button_1.config(text=current_question["options"][0])
    Answer_button_2.config(text=current_question["options"][1])
    Answer_button_3.config(text=current_question["options"][2])
    Answer_button_4.config(text=current_question["options"][3])
    

fifty_fifty_joker = tk.Button(root,image = fifty, compound = TOP, text = "50% Joker", command = fifty_fifty)
new_joker = tk.Button(root,image = new, compound = TOP, text = "New Question", command = question_joker)


frame = Frame(root)

# resetting old variables , starting again using start function

def play_again():

    label3.grid_forget()
    label1.grid(row=2, column=2, pady=20)
    play_again_button.grid_forget()
    Exit_button.grid_forget()
    play_button.grid(row=4, column=2, pady=60)
    intro_text.configure(height=3)
    frame.grid_forget()
    question_text.delete(1.0, END)
    question_text.insert(END, text)
    global round_no
    round_no = 0
    global scorecount
    global current_difficulty
    scorecount = 0
    current_difficulty = "easy"
    start()

# buttons for end screen

play_again_button = tk.Button(frame, text="Play again", width=25, command=play_again)
Exit_button = tk.Button(frame, text="Exit", width=25, command=exit)

#get a random question

def get_question(difficulty):
    global used_answers
    global data
    global current_difficulty

    question = random.choice((data[difficulty]))

    if question["question"] in used_answers:
        return get_question(current_difficulty)

    else:
        used_answers.append(question["question"])
    return question



current_question = get_question(current_difficulty)

# main 'quiz-loop' 11 times 

def proceed():

    global current_difficulty
    global current_question
    global scorecount
    global current_answer
    global round_no
    global image2
    global resize_image
    global img2
    global label2
    score.config(text=f"Score : {scorecount}")
    round_no += 1
    if round_no == 11:
        to_end()
        return

    image2 = Image.open(random.choice(data["pictures"]))
    resize_image = image2.resize((300, 300))
    img2 = ImageTk.PhotoImage(resize_image)
    label2 = Label(image=img2)
    label2.image2 = img2

    label2.grid_forget()
    label2.grid(row=2, column=2, pady=20)

    current_difficulty = change_difficulty()
    current_question = get_question(current_difficulty)
    intro_text.delete(1.0, END)
    intro_text.insert(END, text_quote)
    question_text.delete(1.0, END)
    question_text.insert(END, current_question["question"])
    Answer_button_1.config(text=current_question["options"][0])
    Answer_button_2.config(text=current_question["options"][1])
    Answer_button_3.config(text=current_question["options"][2])
    Answer_button_4.config(text=current_question["options"][3])
    Answer_button_1.grid(row=1, column=1)
    Answer_button_2.grid(row=1, column=2)
    Answer_button_3.grid(row=2, column=1, pady=20)
    Answer_button_4.grid(row=2, column=2, padx=20)

# 4 functions for the 4 answer buttons

def answer_0():
    global scorecount
    global text_quote
    global current_answer
    global current_difficulty
    if current_question["options"][0] == current_question["answer"]:
        if current_difficulty == "easy":
            scorecount += 10
        elif current_difficulty == "medium":
            scorecount += 25
        elif current_difficulty == "hard":
            scorecount += 50
        text_quote = "Your answer was correct , score increased"
        current_answer = True
        proceed()
    else:
        text_quote = "Your answer was wrong!"
        current_answer = False
        proceed()


def answer_1():
    global scorecount
    global text_quote
    global current_answer
    if current_question["options"][1] == current_question["answer"]:
        if current_difficulty == "easy":
            scorecount += 10
        elif current_difficulty == "medium":
            scorecount += 25
        elif current_difficulty == "hard":
            scorecount += 50
        text_quote = "Your answer was correct , score increased"
        current_answer = True
        proceed()
    else:
        text_quote = "Your answer was wrong!"
        current_answer = False
        proceed()


def answer_2():
    global scorecount
    global text_quote
    global current_answer
    if current_question["options"][2] == current_question["answer"]:
        if current_difficulty == "easy":
            scorecount += 10
        elif current_difficulty == "medium":
            scorecount += 25
        elif current_difficulty == "hard":
            scorecount += 50
        text_quote = "Your answer was correct , score increased"
        current_answer = True
        proceed()
    else:
        text_quote = "Your answer was wrong!"
        current_answer = False
        proceed()


def answer_3():
    global scorecount
    global text_quote
    global current_answer
    if current_question["options"][3] == current_question["answer"]:
        if current_difficulty == "easy":
            scorecount += 10
        elif current_difficulty == "medium":
            scorecount += 25
        elif current_difficulty == "hard":
            scorecount += 50
        text_quote = "Your answer was correct , score increased"
        current_answer = True
        proceed()
    else:
        text_quote = "Your answer was wrong!"
        current_answer = False
        proceed()

# 4 answer buttons for the tkinter window

Answer_button_1 = tk.Button(
    frame, text=current_question["options"][0], width=20, height=2, command=answer_0
)
Answer_button_2 = tk.Button(
    frame, text=current_question["options"][1], width=20, height=2, command=answer_1
)
Answer_button_3 = tk.Button(
    frame, text=current_question["options"][2], width=20, height=2, command=answer_2
)
Answer_button_4 = tk.Button(
    frame, text=current_question["options"][3], width=20, height=2, command=answer_3
)





# more variables^^

current_question = get_question(current_difficulty)
question_text.insert(END, current_question["question"])

# change difficult after each question

def change_difficulty():
    global current_difficulty
    if current_difficulty == "easy" and current_answer == True:
        current_difficulty = "medium"
    elif current_difficulty == "medium" and current_answer == True:
        current_difficulty = "hard"
    elif current_difficulty == "medium" and current_answer == False:
        current_difficulty = "easy"
    elif current_difficulty == "hard" and current_answer == False:
        current_difficulty = "medium"
    return current_difficulty


name = name_entry.get()

# after 11 rounds creating "end screen"

def ending(score):
    global text_quote
    global question_text
    global name
    global image3
    global img3
    global label3
    global label2
    global resize_image
    intro_text.delete(1.0, END)
    intro_text.insert(END, f"Your score after 10 Rounds is {scorecount}")

    if score < 50:
        question_text.delete(1.0, END)
        question_text.insert(
            END,
            f" {name}... You finished last in the competition , practice more and you can achieve a medal!",
        )
        image3 = Image.open("workharder.png")
        resize_image = image3.resize((400, 400))
        img3 = ImageTk.PhotoImage(resize_image)
        label3 = Label(image=img3)
        label3.image3 = img3
        label2.grid_forget()
    elif score > 49 and score < 100:
        question_text.delete(1.0, END)
        question_text.insert(
            END,
            f"You made it to the Podium {name}! You are rewarded with a bronze medal!        Good job!",
        )
        image3 = Image.open("goodjob.png")
        resize_image = image3.resize((400, 400))
        img3 = ImageTk.PhotoImage(resize_image)
        label3 = Label(image=img3)
        label3.image3 = img3
    elif score > 99 and score < 200:
        question_text.delete(1.0, END)
        question_text.insert(
            END,
            f"You made it to the Podium {name}! You are rewarded with a bronze medal!        Good job!",
        )
        image3 = Image.open("bronze.jpeg")
        resize_image = image3.resize((400, 400))
        img3 = ImageTk.PhotoImage(resize_image)
        label3 = Label(image=img3)
        label3.image3 = img3
    elif score > 199 and score < 485:
        question_text.delete(1.0, END)
        question_text.insert(
            END,
            f"Gratulations {name} you finished 2nd Place! You earned a silver medal!              Very good job!",
        )
        image3 = Image.open("silver.png")
        resize_image = image3.resize((400, 400))
        img3 = ImageTk.PhotoImage(resize_image)
        label3 = Label(image=img3)
        label3.image3 = img3

    elif score > 484:
        question_text.delete(1.0, END)
        question_text.insert(
            END, f"You won the Gold medal {name} ! Awesome result ! Amazing job!"
        )
        image3 = Image.open("win.jpg")
        resize_image = image3.resize((400, 400))
        img3 = ImageTk.PhotoImage(resize_image)
        label3 = Label(image=img3)
        label3.image3 = img3
        label2.grid_forget()

# showing "endscreen" saving to highscores.json

def to_end():
    global name
    name = name_entry.get()
    global scorecount
    ending(scorecount)
    label2.grid_forget()
    label3.grid(row=2, column=2, pady=20)
    Answer_button_1.grid_forget()
    Answer_button_2.grid_forget()
    Answer_button_3.grid_forget()
    Answer_button_4.grid_forget()
    play_again_button.grid(row=1, column=1)
    Exit_button.grid(row=1, column=2)
    fifty_fifty_joker.grid_forget()
    new_joker.grid_forget()

    highscores.append({name: scorecount})

    write_to_json(highscores, "highscores.json")

# exit button function

def exit():

    root.destroy()


root.mainloop()
