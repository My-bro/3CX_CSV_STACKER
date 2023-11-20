##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## open_folder_dialog
##

from tkinter import filedialog
from src.concatenation import concatenation

def save_file_dialog():
    options = {
        'defaultextension': '.csv',
        'filetypes': [('CSV files', '*.csv'), ('All files', '*.*')],
        'initialdir': '/',
        'title': 'Save As'
    }

    file_path = filedialog.asksaveasfilename(**options)
    if file_path:
        return file_path
    else:
        return None

def open_folder_dialog(Base_path, Add_path, Path):
    temp_path = save_file_dialog()
    if temp_path:
        Path.set(temp_path)
        print("path: ", Path.get())
        concatenation(Base_path, Add_path, Path)