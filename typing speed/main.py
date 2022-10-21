import tkinter as t
import random
from time import *
with open("text.txt") as txt:
    text=txt.readlines()
screen=t.Tk()
screen.minsize(width=500,height=300)
screen.title("Typing speed Calculator")
label=random.choice(text)
my_label=t.Label(text=label)
my_label.pack()
time_1=time()
inputtext=t.Entry()
inputtext.pack()
getinput=inputtext.get()
time_2=time()
time=time_2-time_1
time_r=round(time,0)
speed=len(text)/time_r
# speedtype=speed(time_1,time_2,getinput)
text_label=t.Label(text=speed)
text_label.pack()
screen.mainloop()
def speed(time_s,time_e,text):
    time=time_e-time_s
    time_r=round(time,2)
    speed=len(text)/time_r
    return round(speed,2)