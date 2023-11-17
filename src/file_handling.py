##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## File_handling
##

from src.open_file_dialog import open_file_dialog

def file_handling(button, var, path):
    selected_file_path = open_file_dialog()
    if selected_file_path:
        print("Selected file:", selected_file_path)
        button.config(text="selected_file")
        var.set(True)
        path.set(selected_file_path)
        print("the path", path.get())