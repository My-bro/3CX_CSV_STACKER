##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## folder_states
##

import tkinter as tk

def folder_states(root, Base_bool, Add_bool,Folder_label, Folder_button, Folder_bool):
    if Base_bool.get() == True and Add_bool.get() == True:
        Folder_label.place(x=150, y=150)
        Folder_button.place(x=240, y=200)
    else:
        Folder_label.place_forget()
    root.after(100, lambda: folder_states(root, Base_bool, Add_bool,Folder_label, Folder_button, Folder_bool))