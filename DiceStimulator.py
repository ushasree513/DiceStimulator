import random
from tkinter import *

root = Tk()
root.geometry("800x500")
my_label=Label(root, text="Lets play it...")
my_label.pack()


def roll():

    value = True

    while(value):
        Result = random.randint(1,6)
        print(Result)
        ##CollectInfo = input("Do you want to play again? (n/y)")
        
        if(Result == 6):
            continue
        else:
            break   
b1 = Button(root, text="Lets roll...", command=roll).pack()
root.mainloop()
