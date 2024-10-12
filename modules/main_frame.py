import customtkinter as ctk
from .read_json import read_json

dict = read_json(filename="config.json")


width = dict["main_frame"]["width"]
height = dict["main_frame"]["height"]
title = dict["main_frame"]["title"]

app = ctk.CTk()

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x_coordinate = (screen_width // 2) - (width // 2)
y_coordinate = (screen_height // 2) - (height // 2)

app.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
app.title(title)

button1 = ctk.CTkButton(app, text="Button1")
button2 = ctk.CTkButton(app, text="Button2")
button1.grid(row=0, column=2)
button2.grid(row=2, column=1)

