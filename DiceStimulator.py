from email.mime import image
import random
from textwrap import fill
from tkinter import *
from turtle import color
from unittest import result
from PIL import ImageTk,Image

root = Tk()
root.geometry("800x500")
my_label=Label(root, text="Lets play it...",font=('BOLD',50),bg="light green")
my_label.pack(fill=X)

LabelDisplay = Label(root,font=('bold',200))



def roll():
    Result = random.randint(1,6)
    LabelDisplay.config(text=Result)
    LabelDisplay.pack()

def rollRed():
    Output = random.randint(3,6)
    LabelDisplay.config(text=Output)
    LabelDisplay.pack()
    
ImageRed = ImageTk.PhotoImage(Image.open('Red.PNG'))

bR = Button(root,image=ImageRed,command=rollRed).pack()
b1 = Button(root, text="Lets roll...",font=('Normal'), command=roll).pack()
root.mainloop()
