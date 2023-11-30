#imports all classes, functions, and constants from the tkinter module
from tkinter import *

# importing specific modules and classes from the Python Imaging Library (PIL)/Pillow library

from PIL import Image, ImageTk, ImageFilter
#1. Image: This is a class from the PIL (or Pillow) library that represents an image. It provides various methods for working with images, such as opening, saving, and manipulating them

#2. ImageTk: This is a module that provides support for creating Tkinter PhotoImage objects from PIL images. Tkinter is a GUI (Graphical User Interface) library in Python, and ImageTk helps integrate PIL images with Tkinter

#3. ImageFilter: This module provides a collection of image filters, such as blurring and sharpening, that can be applied to PIL images


# Function to center the window
def center_window(window, width, height):
    #Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the geometry of the window to center it on the screen
    window.geometry(f"{width}x{height}+{x}+{y}")
    # formatted string is commonly used to represent geometry information for a window in Tkinter
    # {width} and {height}: These are placeholders for the width and height values of the window, respectively. The values inside the curly braces will be replaced with the actual values passed as arguments when the string is formatted.
    # x: This is a literal character 'x' used to separate the width and height in the geometry string
    # {x} and {y}: These are placeholders for the x and y coordinates of the window, respectively. Similar to {width} and {height}, these will be replaced with the actual x and y values.

# Function to blur background images 
def blur_image(image_path, blur_radius):
    # Open the original image using PIL (Pillow)
    original_image = Image.open(image_path)

    # Apply Gaussian blur to the original image
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(blur_radius))
    # uses the Gaussian function to calculate the weighted average of pixel values

    # Return the blurred image
    return blurred_image

# Function to handle "Check pH Level" button click
def pHClick():
    # Create a new top-level window
    window2 = Toplevel(root)

    window2.withdraw()  # Hide the window initially 
    #to avoid it being visible during the setup.

    # Set the title and icon for the new window
    window2.title("Displaying pH Level")
    window2.iconbitmap('ui/logo.ico')

    # Center the new window on the screen
    center_window(window2, 300, 200)
    window2.resizable(False, False)  # Disable resizing

    # Create a Label to display "pH Level"
    pH_label = Label(window2, text="pH Level :", font=("Arial", 12))
    pH_label.grid(row=0, column=0, pady=10, padx=10)

    # Create an Entry widget
    # Later we will have to display pH level here instead of entery widget
    pH_entry = Entry(window2, font=("Arial", 12))
    pH_entry.grid(row=0, column=1, pady=10, padx=10)

    # Create a Back Button to destroy the current window
    back_button = Button(window2, text="Back", command=window2.destroy, bg='gray', font=("Arial", 12))
    back_button.grid(row=1, column=0, columnspan=2, pady=10)

    window2.deiconify()  # Make the window visible after setup.

# Function to handle "Check Pipe Condition" button click
def pipeClick():
    # Create a new top-level window
    window3 = Toplevel(root)

    window3.withdraw()  # Hide the window initially(same reason)

    # Set the title and icon for the new window
    window3.title("Displaying Pipe Condition")
    window3.iconbitmap('ui/logo.ico')

    # Center the new window on the screen
    center_window(window3, 300, 200)
    window3.resizable(False, False)  # Disable resizing

    # Create a Label to display "Pipe Condition"
    pipe_label = Label(window3, text="Pipe Condition :", font=("Arial", 12))
    pipe_label.grid(row=0, column=0, pady=10, padx=10, sticky='w')  # Adjusted sticky option

    # Define options for the pipe condition using a list
    pipe_options = ["Very Good", "Good", "Bad"]

    # Create a StringVar to store the selected pipe condition
    pipe_var = StringVar(window3)
    pipe_var.set(pipe_options[0])  # default value

    # Create an OptionMenu for selecting the pipe condition
    pipe_menu = OptionMenu(window3, pipe_var, *pipe_options)
    pipe_menu.config(font=("Arial", 12), width=12)  # Set a fixed width for the OptionMenu
    pipe_menu.grid(row=0, column=1, pady=10, padx=10, sticky='w')  # Adjusted sticky option

    # Create a Back Button to destroy the current window
    back_button = Button(window3, text="Back", command=window3.destroy, bg='gray', font=("Arial", 12))
    back_button.grid(row=1, column=0, columnspan=2, pady=10)

    window3.deiconify()  # Make the window visible after setup.

# initializes the main window 
root = Tk() #creates the main window using the Tk() constructor from the Tkinter library

root.title("Corrosion Level Project")
root.iconbitmap('ui/logo.ico')

center_window(root, 400, 300)  # Set the desired size
root.resizable(False, False)  # Disable resizing

# Load and blur the background image
background_image = blur_image('ui/background.jpg', blur_radius=0.0001)  # image file
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas for the background
canvas = Canvas(root, width=background_image.width, height=background_image.height)
canvas.pack(fill=BOTH, expand=YES)

# Place the background image on the canvas
canvas.create_image(0, 0, image=background_photo, anchor=NW)

mainTitle = Label(canvas, text="Corrosion Detector", font=("Arial", 16, "bold"))
mainTitle.place(relx=0.5, rely=0.1, anchor=CENTER)

# Create a frame for the buttons
button_frame = Frame(canvas)
button_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Button 1:
pH_button = Button(button_frame, text="pH Level", command=pHClick, fg="white", bg='black', pady=15, padx=50, font=("Arial", 14))
pH_button.pack()

# Button 2:
pipe_Button = Button(button_frame, text="Pipe Condition", command=pipeClick, fg="white", bg='black', padx=25, pady=19, font=("Arial", 14))
pipe_Button.pack()

root.mainloop()
