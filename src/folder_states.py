##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## folder_states
##

import tkinter as tk

def folder_states(root, Base_bool, Add_bool,Folder_label, Folder_button, Folder_button_bool, Folder_bool):
    if Base_bool.get() == True and Add_bool.get() == True:
        Folder_label.pack()
        Folder_button.pack()
        Folder_button_bool.set(True)
    else:
        Folder_label.pack_forget()
        Folder_button.pack_forget()
    root.after(100, lambda: folder_states(root, Base_bool, Add_bool,Folder_label, Folder_button, Folder_button_bool, Folder_bool))