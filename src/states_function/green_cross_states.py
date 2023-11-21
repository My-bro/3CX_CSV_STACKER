##
## ANTARES PROJECT, 2023
## 3CX_CSV_STACKER
## File description:
## green_cross_states
##

def green_cross_states(root, image, image2,Base_bool, Add_bool):
    if Base_bool.get() == True:
        image.place(x=210, y=45)
    else:
        image.place_forget()

    if Add_bool.get() == True:
        image2.place(x=520, y=45)
    else:
        image2.place_forget()
    root.after(100, lambda: green_cross_states(root, image, image2,Base_bool, Add_bool))