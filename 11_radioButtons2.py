from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Button")

# r = IntVar()
# r.set("2")
MODES = [
    ("red", "red"),
    ("yellow", "yellow"),
    ("blue", "blue")
]

colour = StringVar()
colour.set("Red")

for text, mode in MODES:
    Radiobutton(root, text = text , variable=colour, value=mode).pack()

def clicked(value):
    myLabel = Label(root, text=value).pack(anchor=W)

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2).pack()

myLabel = Label(root, text=colour.get()).pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(colour.get())).pack()


mainloop()