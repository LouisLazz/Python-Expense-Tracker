# Imports

import customtkinter as ctk
import matplotlib.pyplot as plt
import math
from customtkinter import CTkButton, CTkEntry, CTkLabel, CTkTextbox, CTkFrame, CTkScrollbar, CTkOptionMenu, CTkComboBox, CTkProgressBar, CTkSlider

# Functions

totalFunds = 0

def slider_event(value):
    print(value)

def button_callback():
    totalFunds = 1
    totalFunds += 1
    print(totalFunds)

def setting_callback1():
    print("checkbox 1 pressed!")

def setting_callback2():
    print("checkbox 2 pressed!")

app = ctk.CTk()
app.title("LA Finance")
app.geometry("400x150")
app.grid_columnconfigure((0, 1), weight=1)

app.grid_columnconfigure(0, weight=1)
button = ctk.CTkButton(app, text="BUTTON", fg_color="red", border_color="black", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

checkbox_1 = ctk.CTkCheckBox(app, text="checkbox 1")
checkbox_1 = ctk.CTkCheckBox(app, text="checkbx", command=setting_callback1)
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

checkbox_2 = ctk.CTkCheckBox(app, text="checkbox 2")
checkbox_2 = ctk.CTkCheckBox(app, text="checkbox 2", command=setting_callback2)
checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

slider = ctk.CTkSlider(app, from_=-100, to=100, command=slider_event)
slider.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")
app.mainloop()