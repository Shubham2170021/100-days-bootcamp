from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(time_text,text="0:00")
    timer_label["text"]="Timer"
    timer_label.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def button_count():
    global reps
    reps+=1
    work_Sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps%8==0:
        counter(long_break_sec)
        timer_label["text"]="Long break"
        timer_label.config(text="Long break",fg=RED)
    elif reps%2==0:
        counter(short_break_sec)
        timer_label["text"]="Short break"
        timer_label.config(text="Short break",fg=PINK)
    else:
        counter(work_Sec)
        timer_label["text"]="Work time"
        timer_label.config(text="Work time")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):
    global reps
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(time_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,counter,count-1)
    else:
        button_count()
        # if reps%2==0:
        #     cheak_button["text"]="✔"
        #     cheak_button.config(text="✔")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Tamato timer")
window.config(padx=100,pady=50,bg=YELLOW)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tamoto_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tamoto_img)
time_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)
timer_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,30,"bold"))
timer_label.grid(row=0,column=1)
start_button=Button(text="start",highlightthickness=0,command=button_count)
start_button.grid(row=2,column=0)
reset_button=Button(text="reset",highlightthickness=0,command=reset)
reset_button.grid(row=2,column=2)
cheak_button=Label(fg=RED)
cheak_button.grid(column=1,row=3)

window.mainloop()