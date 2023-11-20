##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## add_function
##

import tkinter as tk
from tkinter import filedialog
from src.file_function.file_handling import file_handling
from customtkinter import *

def Add_function(root, Add_path):
    Add_path_var = tk.BooleanVar(value=False)
    Add_text = CTkLabel(root, text="Choose the add file", font=("Arial", 20, "bold"))
    Add_button = CTkButton(root, text="Choose", corner_radius=5, font=("Arial", 20, "bold"), command=lambda: file_handling(Add_button, Add_path_var,Add_path))
    Add_text.place(x=350, y=10)
    Add_button.place(x=370, y=50)
    return Add_path_var
