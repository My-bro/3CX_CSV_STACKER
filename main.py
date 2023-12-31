import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from customtkinter import *
from src.setup_function.base_function import Base_function
from src.setup_function.add_function import Add_function
from src.setup_function.set_up_windows import set_up_windows
from src.states_function.folder_states import folder_states
from src.file_function.open_folder_dialog import open_folder_dialog
from src.states_function.green_cross_states import green_cross_states

root = CTk()
set_up_windows(root)

Base_path = tk.StringVar(value="")
Add_path = tk.StringVar(value="")
Path = tk.StringVar(value="")

Base_bool = Base_function(root, Base_path)  # Set up Base element
Add_bool = Add_function(root, Add_path)  # Set up Add element
folder_bool = tk.BooleanVar(value=False)

Folder_label = CTkLabel(root, text="Select where is gonna be put", font=("Arial", 20, "bold"), pady=10)
Folder_button = CTkButton(root, text="Choose", font=("Arial", 20, "bold"), command=lambda: open_folder_dialog(Base_path, Add_path, Path))
Folder_bool = tk.BooleanVar(value=False)
Folder_path = tk.StringVar(value="")

image_file = PhotoImage(file="src/img/green_cross.png")
image_file = image_file.subsample(19,19)

green_cross1 = tk.Label(root, image=image_file)
green_cross2 = tk.Label(root, image=image_file)

folder_states(root, Base_bool, Add_bool, Folder_label, Folder_button, Folder_bool)  # If a file was selected on add and base, it will display the folder button
green_cross_states(root, green_cross1, green_cross2,Base_bool, Add_bool)

root.mainloop()