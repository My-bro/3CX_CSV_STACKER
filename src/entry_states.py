##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## entry_states
##

import tkinter as tk

def entry_states(root, entry_label, entry_bar, entry_button, Folder_bool):

    if Folder_bool.get() == True:
        entry_label.pack()
        entry_bar.pack()
        entry_button.pack()
    else:
        entry_label.pack_forget()
        entry_bar.pack_forget()
        entry_button.pack_forget()

    root.after(100, lambda: entry_states(root, entry_label, entry_bar, entry_button, Folder_bool))