from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Button")

# Defining integer variables in Tkinter:
# VarName = IntVar()

r = IntVar()
r.set("2")


def clicked(value):
    myLabel = Label(root, text=value).pack()

Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2).pack()

myLabel = Label(root, text=r.get()).pack()

mainloop()