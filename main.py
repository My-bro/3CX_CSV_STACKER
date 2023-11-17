##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## csv_stacker
##

import tkinter as tk
from ttkthemes import ThemedTk
import sys
from src.base_function import Base_function
from src.add_function import Add_function
from src.folder_states import folder_states
from src.entry_states import entry_states
from src.open_folder_dialog import open_folder_dialog
from src.collect_entry import collect_entry
from src.set_up_windows import set_up_windows



root = ThemedTk(theme="arc")
set_up_windows(root)

Base_path = tk.StringVar(value="")
Add_path = tk.StringVar(value="")

Base_bool = Base_function(root, Base_path)
Add_bool = Add_function(root, Add_path)
folder_bool = tk.BooleanVar(value=False)

Folder_label = tk.Label(root, text="Select where is gonna be put", font=("Arial", 20, "bold"), pady=10)
Folder_button = tk.Button(root, text="Choose", font=("Arial", 20, "bold"), command= lambda: open_folder_dialog(Folder_path,Folder_bool))
Folder_bool = tk.BooleanVar(value=False)
Folder_button_bool = tk.BooleanVar(value=False)
Folder_path = tk.StringVar(value="")

entry_label = tk.Label(root, text="Enter file name")
entry_label.pack(pady=10)
entry_bar = tk.Entry(root, width=30)
entry_bar.pack(pady=10)

entry_button = tk.Button(root, text="Go stack")
entry_button.pack(pady=10)

folder_states(root, Base_bool, Add_bool,Folder_label, Folder_button, Folder_button_bool, Folder_bool)
entry_states(root, entry_label, entry_bar, entry_button, Folder_bool)

entry_bar.bind("<Return>", lambda event: collect_entry(Base_path, Add_path, Folder_path, entry_bar, event))
entry_button.config(command=lambda: collect_entry(Base_path, Add_path, Folder_path, entry_bar))


root.mainloop()
