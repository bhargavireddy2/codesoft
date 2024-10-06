import random
from tkinter import *
from tkinter import messagebox
import pyperclip

gui = Tk()
gui.title('Password Generator by Bhargavi Reddy')
gui.geometry('400x300')
gui.resizable(0,0)

def process():
    length = int(string_pass.get())

    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['@', '#', '$', '%', '&', '*']
    all = lower + upper + num + special
    ran = random.sample(all,length)
    password = "".join(ran)
    messagebox.showinfo('Result', 'Thanks for Using Bhargavi Password Generator \n\nHere is Your password {} \n\nPassword Copied to Clipboard'.format(password))
    pyperclip.copy(password)

string_pass = StringVar()
label = Label(text="Choose Your Password Length By BR Manager").pack(pady=50)
txt = Entry(textvariable=string_pass).pack()
btn = Button(text="Click Here to Generate Password", command=process).pack(padx=50,pady=50)

gui.mainloop()

a = "Python"
print(a)
