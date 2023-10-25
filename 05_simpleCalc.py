from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    now = e.get()
    e.delete(0, END)
    e.insert(0, str(now) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))


def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)


def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)


def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)


# Buttons adding

button_1 = Button(text="1", padx=30, pady=30, command=lambda: button_click(1))
button_2 = Button(text="2", padx=30, pady=30, command=lambda: button_click(2))
button_3 = Button(text="3", padx=30, pady=30, command=lambda: button_click(3))
button_4 = Button(text="4", padx=30, pady=30, command=lambda: button_click(4))
button_5 = Button(text="5", padx=30, pady=30, command=lambda: button_click(5))
button_6 = Button(text="6", padx=30, pady=30, command=lambda: button_click(6))
button_7 = Button(text="7", padx=30, pady=30, command=lambda: button_click(7))
button_8 = Button(text="8", padx=30, pady=30, command=lambda: button_click(8))
button_9 = Button(text="9", padx=30, pady=30, command=lambda: button_click(9))
button_0 = Button(text="0", padx=30, pady=30, command=lambda: button_click(0))

button_equal = Button(text="=", padx=70, pady=30, command=button_equal)
button_clear = Button(text="Clear", padx=60, pady=30, command=button_clear)
button_add = Button(text="+", padx=30, pady=30, command=button_add)

button_subtract = Button(text="-", padx=31, pady=30, command=button_subtract)
button_multiply = Button(text="*", padx=31, pady=30, command=button_multiply)
button_divide = Button(text="/", padx=31, pady=30, command=button_divide)


# Buttons placing

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_4.grid(row=2, column=0)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
root.mainloop()
