from email.mime import image
import random
from textwrap import fill
from tkinter import *

root = Tk()
root.geometry("800x500")
my_label=Label(root, text="Lets play it...",font=('BOLD',50),bg="pink")
my_label.pack(fill=X)

LabelDisplay = Label(root,font=('bold',200))



def roll():
    Result = random.randint(1,6)
    LabelDisplay.config(text=Result)
    LabelDisplay.pack()
    
        
    
b1 = Button(root, text="Lets roll...", command=roll).pack()
root.mainloop()
