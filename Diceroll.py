import random
from tkinter import *

root=Tk()
root.geometry("650x350")
root.title("Dice Roller")

t1 = Label(root,font=("timesnewroman",300))

def roll_dice():
    code=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    t1.config(text=f'{random.choice(code)}{random.choice(code)}')
    t1.pack()

def close():
    root.quit()

b1=Button(root,text="Roll the Dice",command=roll_dice)
b1.place(x=250,y=0)

root.mainloop()