from tkinter import *
from PIL import ImageTk, Image  #(#*1)

root = Tk()
root.title("Image Viewer")


my_img1 = ImageTk.PhotoImage(Image.open("img/iv1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("img/iv2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("img/iv3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("img/iv4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("img/iv5.jpg"))

img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# Creating a statusbar in image viewer application
status = Label(root, text = "Image 1 of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)

label = Label(image = my_img1)
label.grid(row = 0, column = 0, columnspan = 3)

def forward(image_number):
	global label
	global button_next
	global button_back

	label.grid_forget()
	label = Label(image=img_list[image_number-1])
	button_next = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))
	
	if image_number == 5:
		button_next = Button(root, text=">>", state=DISABLED)

	label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_next.grid(row=1, column=2)

	status = Label(root, text="Image " + str(image_number) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=W+E)


def back(image_number):
	global label
	global button_next
	global button_back

	label.grid_forget()
	label = Label(image=img_list[image_number-1])
	button_next = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)

	label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_next.grid(row=1, column=2)

	status = Label(root, text="Image " + str(image_number) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=W+E)
    

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_next = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_next.grid(row=1, column=2)
status.grid(row=2, column = 0, columnspan=3, pady=10, padx=10, sticky=W+E)

root.mainloop()