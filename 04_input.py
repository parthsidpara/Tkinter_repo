from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="grey", fg="white")
e.pack()
e.insert(0, "Enter Your Name") #smthing like placeholder

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    # myLabel = Label(root, text="Hello, " + e.get())
    myLabel.pack()
myButton = Button(root, text='Enter your name', command=myClick)


myButton.pack()
root.mainloop() 