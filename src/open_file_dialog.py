##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## open_file_dialog
##

from tkinter import filedialog

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("csv files", "*.csv"), ("All files", "*.*")])
    return file_path