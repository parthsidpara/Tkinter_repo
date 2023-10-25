# 1. Pack method(done in first lesson)
# 2. Grid method --> gives more power

# resize window for both methods and see the difference 

from tkinter import *  #import everything from tkinter

root = Tk()

# Creating a label widget
myLabel1 = Label(root, text="Hello Tkinter!")
myLabel2 = Label(root, text="Kem chho?")
# Showing it onto the screen by grid method
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)

# Also true but not a good practice
# myLabel1 = Label(root, text="Hello Tkinter!").grid(row=0, column=0)


root.mainloop()