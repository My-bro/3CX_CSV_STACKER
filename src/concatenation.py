##
## ANTARES PROJECT, 2023
## 3CX csv_stacker
## File description:
## concatenation
##

import csv

def concatenation(Base_path, Add_path, Folder_path, filename):
    Base_data = []
    Add_data = []
    New_data = []
    i = 0
    with open(Base_path.get(), 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            Base_data.append(row)

    with open(Add_path.get(), 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            Add_data.append(row)
    for line in Base_data:
        if(line[0] == 'Total:'):
            break
        New_data.append(line)
    for line in Add_data:
        if i < 5:
            i += 1
            continue
        New_data.append(line)

    csv_file = filename + ".csv"
    path = Folder_path.get()
    path = path + '/' + csv_file
    with open(path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in New_data:
            csvwriter.writerow(row)
    return New_data
