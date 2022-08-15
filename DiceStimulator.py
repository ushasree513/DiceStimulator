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
l3 = Label(root,font=("normal",20))


def roll():
    Result = random.randint(1,6)
   
    LabelDisplay.config(text=Result)
    LabelDisplay.pack(side=RIGHT)
    if(Result == 6):
        l3.config(text="Congratulations!!it's 6, Play Again")
        l3.pack(side=TOP)
    else:
        l3.config(text=" ")
        l3.pack(side=TOP)
    

def rollRed():
    Output = random.randint(3,6)
    LabelDisplay.config(text=Output)
    LabelDisplay.pack(side=LEFT)
    if(Output == 6):
        l3.config(text="Congratulations!!it's 6, Play Again")
        l3.pack(side=TOP)
    else:
        l3.config(text=" ")
        l3.pack(side=TOP)
    
    


bR = Button(root,text="Play With Red",font="Normal,25",bg="red",command=rollRed).pack(side=LEFT)


b1 = Button(root,text="Play With Black",font="Normal,25",bg="grey", command=roll).pack(side=RIGHT)
root.mainloop()
