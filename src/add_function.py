##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## add_function
##

import tkinter as tk
from tkinter import filedialog
from src.file_handling import file_handling

def Add_function(root, Add_path):
    Add_path_var = tk.BooleanVar(value=False)
    Add_text = tk.Label(root, text="Choose the file you gonna add in the base", font=("Arial", 20, "bold"))
    Add_text.pack(pady=10)
    Add_button = tk.Button(root, text="Choose", font=("Arial", 20, "bold"), command=lambda: file_handling(Add_button, Add_path_var,Add_path), width=18, height=2)
    Add_button.pack(pady=10)
    return Add_path_var
