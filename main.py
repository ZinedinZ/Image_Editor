import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

screen = tk.Tk()
screen.title("Image Editor App")
screen.geometry("600x450")
screen.configure(bg="lightblue")


def img():
    global screen, tk_image
    image_location = upload_entry.get()
    image = Image.open(image_location)
    tk_image = ImageTk.PhotoImage(image.resize((380, 300)))

    image_label = tk.Label(screen, image=tk_image, background="lightblue")
    image_label.grid(column=1, row=5)


def edit():
    global screen, edited_image
    # Drawing watermark on image
    image = Image.open(upload_entry.get())
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    font_size = (image_width + image_height) / 50
    font = ImageFont.truetype(font="arial.ttf", size=int(font_size))
    x = image_width * 0.8
    y = image_height * 0.9
    draw.text((x, y), "Zinedin", fill=(255, 255, 255, 128), font=font)

    # Create image on screen
    edited_image = ImageTk.PhotoImage(image.resize((380, 300)))
    new_label = tk.Label(screen, image=edited_image, background="lightblue")
    new_label.grid(column=1, row=5)
    try:
        path = simpledialog.askstring("Save", "Where you want to save your image: ")
        image.save(path)
        messagebox.showinfo("Info", "Image is Successfully saved")
    except (FileNotFoundError, ValueError, OSError):
        messagebox.showinfo("Alert", "Path doesn't exis, please try again")


def upload():
    global screen, tk_image
    try:
        image_location = upload_entry.get()
        image = Image.open(image_location)
        tk_image = ImageTk.PhotoImage(image.resize((380, 300)))

        image_label = tk.Label(screen, image=tk_image, background="lightblue")
        image_label.grid(column=1, row=5)

        image_button = tk.Button(text="Your Image", background="red", command=img)
        image_button.grid(column=0, row=5)

        edit_button = tk.Button(text="Edit Image", width=9, background="green", command=edit)
        edit_button.grid(column=2, row=5, padx=2)

    except (FileNotFoundError, AttributeError, OSError):
        messagebox.showinfo("Alert", "Image path is not correct or image doesn't exist")

# Creating screen look


title_label = tk.Label(text="Image Editor", width=25, height=1, bg="lightblue", font=("Courier", 30, "bold"))
title_label.grid(column=0, row=0, columnspan=3)

entry_label = tk.Label(text="Type location of your Image", bg="lightblue", font=("Arial", 10))
entry_label.grid(column=0, row=1, columnspan=3)

upload_entry = tk.Entry(width=60)
upload_entry.grid(column=1, row=2)

empty_label = tk.Label(bg="lightblue")
empty_label.grid(column=2, row=2)

upload_button = tk.Button(text="Upload Image", command=upload)
upload_button.grid(column=1, row=3, pady=10)

screen.mainloop()
