from tkinter import *
from PIL import ImageTk, Image  #(#*1)

root = Tk()
root.title("IIE")

# Icon
root.iconbitmap('img/xlogo.ico')

# Exit Button
button_exit = Button(root, text="Exit", command=root.quit)
button_exit.pack()

# Using Images with tkinter
'''
Tkinter has built in system for using images but it only supports limited types of img :(
So to use other formats like jpg, png etc we are going to use other python modules like pillow     #(#*1)
<  pip install Pillow  > 
'''

my_img = ImageTk.PhotoImage(Image.open("img/wallpaper.jpg"))
label = Label(image=my_img)
label.pack()
# 3 Step process for adding image
# Step 1: define image
# Step 2: add image in something like label, button or any widget
# Step 3: Use grid or pack to display that widget
root.mainloop()