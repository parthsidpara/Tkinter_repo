from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frame")

# Frame is just a widget and we can create it like any other
frame = LabelFrame(root, text="This is a frame.....", padx=50, pady=50) #Inside pad
# var = LabelFrame(.......)
frame.pack(padx=100, pady=100)  # Outside pad

# Note: We can't use pack and grid at the same time but we can use
# grid inside a fram even if we have used pack for that frame

b = Button(frame, text = "Button in a frame")
b.pack()

root.mainloop()