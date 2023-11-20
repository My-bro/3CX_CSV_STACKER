##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## csv_stacker
##

import tkinter as tk
from customtkinter import *
from src.setup_function.base_function import Base_function
from src.setup_function.add_function import Add_function
from src.setup_function.set_up_windows import set_up_windows
from src.states_function.folder_states import folder_states
from src.open_folder_dialog import open_folder_dialog

root = CTk()
set_up_windows(root)

Base_path = tk.StringVar(value="")
Add_path = tk.StringVar(value="")
Path = tk.StringVar(value="")

Base_bool = Base_function(root, Base_path)
Add_bool = Add_function(root, Add_path)
folder_bool = tk.BooleanVar(value=False)

Folder_label = CTkLabel(root, text="Select where is gonna be put", font=("Arial", 20, "bold"), pady=10)
Folder_button = CTkButton(root, text="Choose", font=("Arial", 20, "bold"), command=lambda: open_folder_dialog(Base_path, Add_path, Path))
Folder_bool = tk.BooleanVar(value=False)
Folder_path = tk.StringVar(value="")

folder_states(root, Base_bool, Add_bool,Folder_label, Folder_button, Folder_bool)

root.mainloop()