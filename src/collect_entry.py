##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## collect_entry
##

from src.concatenation import concatenation

def collect_entry(Base_path, Add_path, Folder_path, entry_bar, event=None):
    filename = entry_bar.get()
    print(filename)
    concatenation(Base_path, Add_path, Folder_path, filename)