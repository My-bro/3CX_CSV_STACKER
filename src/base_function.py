##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## Base_function
##



import tkinter as tk
from tkinter import filedialog
from src.file_handling import file_handling

def Base_function(root, Base_path):
    Base_path_var = tk.BooleanVar(value=False)
    Base_text = tk.Label(root, text="Choose the base file", font=("Arial", 20, "bold"))
    Base_button = tk.Button(root, text="Choose", font=("Arial", 20, "bold"), command=lambda: file_handling(Base_button, Base_path_var, Base_path), width=18, height=2)
    Base_text.pack(pady=10)
    Base_button.pack(pady=10, padx=10)
    return Base_path_var
