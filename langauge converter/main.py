from cgitb import text
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

data1=pandas.read_csv("data/french_words.csv")
dict=data1.to_dict(orient="records")
card={

}

def next_card():
    global card
    card=random.choice(dict)
    canvas.itemconfig(titel,text="French")
    canvas.itemconfig(word1,text=card["French"])
    # flip_card()
def flip_card():
    global card
    canvas.itemconfig(titel,text="English")
    canvas.itemconfig(word1,text=card["English"])
    canvas.itemconfig(set_image, image=back_image)
    canvas.itemconfig(set_image, image=front_img)
    window.after(3000,func=flip_card)


window=Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Langauge converter")
window.after(3000,func=flip_card)
canvas=Canvas(width=800,height=526)
front_img=PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
set_image=canvas.create_image(400,263,image=front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
titel=canvas.create_text(400,150,text="Title",font=("arial",20))
word1=canvas.create_text(400,263,text="Word",font=("arial",25))
canvas.grid(row=0,column=0,columnspan=2)
my_image_right = PhotoImage(file="images/right.png")
button_right = Button(image=my_image_right, highlightthickness=0,command=next_card)
button_right.grid(row=1,column=1)
my_image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=my_image_wrong, highlightthickness=0,command=next_card)
button_wrong.grid(row=1,column=0)
next_card()

window.mainloop()
