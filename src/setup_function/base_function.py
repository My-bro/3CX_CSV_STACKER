##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## Base_function
##

import tkinter as tk
from tkinter import filedialog
from src.file_function.file_handling import file_handling
from customtkinter import *

def Base_function(root, Base_path):
    Base_path_var = tk.BooleanVar(value=False)
    Base_text = CTkLabel(root, text="Choose the base file", font=("Arial", 20, "bold"))
    Base_button = CTkButton(root, text="Choose", corner_radius=5, font=("Arial", 20, "bold"), command=lambda: file_handling(Base_button, Base_path_var, Base_path))
    Base_text.place(x=40 , y=10)
    Base_button.place(x=60 , y=50)
    return Base_path_var