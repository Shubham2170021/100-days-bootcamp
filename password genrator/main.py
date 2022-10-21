import json
from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_pass():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
  password_letters=[random.choice(letters) for _ in range(random.randint(8,10))]
  password_number=[random.choice(numbers) for _ in range(random.randint(2,4))]
  password_symbols=[random.choice(symbols) for _ in range(random.randint(2,4))]
  password_list=password_letters+password_number+password_symbols
  random.shuffle(password_list)
  password="".join(password_list)
#   password_text_box["text"]=password
  password_text_box.insert(0,password)
  
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=websit_text_box.get()
    username=username_text_box.get()
    password=password_text_box.get()
    new_data={
            website:{
              "email":username,
              "password":password
            }
    }
    if len(website)==0 or len(username)==0 or len(password)==0:
        messagebox.showinfo(title="opps",message="please fill all blanks box ")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"you entered email :{username}\n password :{password}")
        if is_ok:
          try:
            with open("data.json","r") as file:
              data=json.load(file)
          except FileNotFoundError:
            with open("data.json","w") as file:
              json.dump(new_data,file,indent=4)
          else:
              data.update(new_data)
              with open("data.json","w") as file:
                json.dump(data,file,indent=4)
          finally:
            websit_text_box.delete(0,END)
            password_text_box.delete(0,END)
def find_pass():
  website1=websit_text_box.get()
  try:
    with open("data.json","r") as file:
      data=json.load(file)
      key=data.keys()
  except FileNotFoundError:
    messagebox.showinfo(title="message",message="File does not exit")
  else:
    if website1 in key:
      username=data[website1]["email"]
      password=data[website1]["password"]
      messagebox.showinfo(title=website1,message=f"email:{username}\n password:{password}")
    else:
      messagebox.showerror(title="error",message="No data found ")


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Genrator")
window.config(padx=20,pady=20)
canvas=Canvas(width=200,height=200)
tamoto_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=tamoto_img)
canvas.grid(column=1,row=0)
website_label=Label(text="website",font=("Courier",15,"bold"))
website_label.grid(column=0,row=1)
email_label=Label(text="Email/username",font=("Courier",15,"bold"))
email_label.grid(column=0,row=2)
pasword_label=Label(text="Password",font=("Courier",15,"bold"))
pasword_label.grid(column=0,row=3)
websit_text_box=Entry(width=30)
websit_text_box.grid(column=1,row=1,columnspan=35)
username_text_box=Entry(width=30)
username_text_box.grid(column=1,row=2,columnspan=35)
password_text_box=Entry(width=15)
password_text_box.grid(column=1,row=3)
genrate_password_botton=Button(text="Genrate Password",command=random_pass)
genrate_password_botton.grid(column=2,row=3)
add_b=Button(text="Add",width=36,command=save)
add_b.grid(column=1,row=4,columnspan=36)
search_b=Button(text="Search",command=find_pass)
# search_b.config(padx=0)
search_b.grid(row=1,column=2)

window.mainloop()