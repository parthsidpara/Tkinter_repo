from tkinter import * 
from PIL import Image, ImageTk, ImageFilter

# Function to center the window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

# Function to blur background images 
def blur_image(image_path, blur_radius):
    original_image = Image.open(image_path)
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(blur_radius))
    return blurred_image

# Function to handle "Check pH Level" button click
def pHClick():
    window2 = Toplevel(root)
    window2.withdraw()  # Hide the window initially
    window2.title("Displaying pH Level")
    window2.iconbitmap('ui/logo.ico')
    center_window(window2, 300, 200)
    window2.resizable(False, False)  # Disable resizing

    pH_label = Label(window2, text="pH Level :", font=("Arial", 12))
    pH_label.grid(row=0, column=0, pady=10, padx=10)

    pH_entry = Entry(window2, font=("Arial", 12))
    pH_entry.grid(row=0, column=1, pady=10, padx=10)

    back_button = Button(window2, text="Back", command=window2.destroy, bg='gray', font=("Arial", 12))
    back_button.grid(row=1, column=0, columnspan=2, pady=10)

    window2.deiconify()  # Make the window visible after setup

# Function to handle "Check Pipe Condition" button click
def pipeClick():
    window3 = Toplevel(root)
    window3.withdraw()  # Hide the window initially
    window3.title("Displaying Pipe Condition")
    window3.iconbitmap('ui/logo.ico')
    center_window(window3, 300, 200)
    window3.resizable(False, False)  # Disable resizing

    pipe_label = Label(window3, text="Pipe Condition :", font=("Arial", 12))
    pipe_label.grid(row=0, column=0, pady=10, padx=10, sticky='w')  # Adjusted sticky option

    pipe_options = ["Very Good", "Good", "Bad"]
    pipe_var = StringVar(window3)
    pipe_var.set(pipe_options[0])  # default value

    pipe_menu = OptionMenu(window3, pipe_var, *pipe_options)
    pipe_menu.config(font=("Arial", 12), width=12)  # Set a fixed width for the OptionMenu
    pipe_menu.grid(row=0, column=1, pady=10, padx=10, sticky='w')  # Adjusted sticky option

    back_button = Button(window3, text="Back", command=window3.destroy, bg='gray', font=("Arial", 12))
    back_button.grid(row=1, column=0, columnspan=2, pady=10)

    window3.deiconify()  # Make the window visible after setup

# Main Window
root = Tk()
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