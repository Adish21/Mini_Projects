from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Ditgital time")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)

Label(master,font=("Arial",50),text="Digital clock by Adish",fg="black",bg="white").pack()
clock = Label(master, font=("Aeial",125),bg="black",fg="white")
clock.pack()

get_time()

master.mainloop()
