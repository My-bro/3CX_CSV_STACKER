##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## open_folder_dialog
##

from tkinter import filedialog

def open_folder_dialog(Folder_path,Folder_bool):
    Folder_path.set(filedialog.askdirectory(title="Select a folder"))
    Folder_bool.set(True)