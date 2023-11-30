from tkinter import *
from tkinter import messagebox #Importing messagebox

root = Tk()
root.title("Message box/ Title box")
# Diff types of message box:
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
	response = messagebox.showinfo("This is my Popup!", "Hello World!")
	Label(root, text=response).pack()
	#if response == "yes":
	#	Label(root, text="You Clicked Yes!").pack()
	#else:
	#	Label(root, text="You Clicked No!!").pack()

Button(root, text="Popup", command=popup).pack()



mainloop()