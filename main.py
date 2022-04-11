from tkinter import *

import pandas
from pandas import *
import random
import time


current_card={}
to_dict={}

BACKGROUND_COLOR = "#B1DDC6"


try:
    data_1=pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_dict=original_data.to_dict(orient="records")

else:


    to_dict= data_1.to_dict(orient="records")
print(to_dict)

def next_card():
    global current_card,time_progress
    windows.after_cancel(time_progress)
    current_card = random.choice(to_dict)

    canvas.itemconfig(text,text=f'{current_card["French"]}',fill="black")
    canvas.itemconfig(title, text=f'French',fill="black")
    canvas.itemconfig(light_one, image=light_photo)
    time_progress=windows.after(3000, func=flip)

# with open(,"r") as data:


# title.config(text=raw)
def flip():
    canvas.itemconfig(light_one,image=dark_photo)
    canvas.itemconfig(text,text=f'{current_card["English"]}',fill="white")
    canvas.itemconfig(title, text=f'English',fill="white")



def is_known():
    to_dict.remove(current_card)
    data_3=pandas.DataFrame(to_dict)
    data_3.to_csv("data/words_to_learn.csv",index=False)
    next_card()


windows=Tk()
windows.config(padx=50,pady=50 ,bg=BACKGROUND_COLOR)
light_photo=PhotoImage(file="images/card_front.png")
correct_photo=PhotoImage(file="images/right.png")
wrong_photo=PhotoImage(file="images/wrong.png")
dark_photo=PhotoImage(file="images/card_back.png")

time_progress=windows.after(3000,func=flip)


canvas=Canvas(width=800,height=526)
light_one=canvas.create_image(400,263,image=light_photo)
canvas.grid(column=0,row=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
title=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
text=canvas.create_text(400,263,text=f"text",font=("Ariel",60,"bold"))


# canvas.create_image(100,500,image=correct_photo)
# canvas.grid(column=0,row=1)

correct_button=Button(image=correct_photo,highlightthickness=0,command=is_known)
correct_button.grid(column=1,row=1)

wrong_Button=Button(image=wrong_photo,highlightthickness=0,command=next_card)
wrong_Button.grid(column=0,row=1)

# -----------------------------------------------------------------------------------------------

next_card()











windows.mainloop()