from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()
myButton = Button(root, text='click here', command=myClick)
# myButton = Button(root, text='click here', command=myClick()) #Already clicked ^_^
# myButton = Button(root, text='click here', state=DISABLED)
# myButton = Button(root, text='click here', padx=50, pady=20)




# fg = "colour" : for forground colour
# bg = "colour" : for background colour
myButton = Button(root, text="Click, Here!", command=myClick, fg="yellow", bg='black')




myButton.pack()
root.mainloop() 