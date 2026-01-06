import csv
import os

employee_dict = [
    {'Name':'Abhijit', 'Role':'Engg Manager', 'Sal':350000},
    {'Name':'Ganesh', 'Role':'QA Manager', 'Sal':300000},
    {'Name':'Sunil', 'Role':'Dev Lead', 'Sal':250000}
]


def write_dict_csv(path,record):
    with open(path,'w',newline='') as file:
        fieldnames = employee_dict[0].keys()
        csv_writer = csv.DictWriter(file,fieldnames=fieldnames,delimiter=',')
        csv_writer.writeheader()
        csv_writer.writerows(record)

def read_dict_csv(path):
    with open(path,'r',newline='') as file:
        content = csv.DictReader(file,delimiter=',')
        for row in content:
            if row['Name'].__eq__('Sunil'):
                print(row)

def append_dict_csv(path,record):
    with open(path,'a',newline='') as file:
        file_exists = os.path.isfile(path) and os.path.getsize(path) > 0
        fieldnames = employee_dict[0].keys()
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
        if not file_exists:
            csv_writer.writeheader()
        csv_writer.writerow(record)

def read_dict_csv_post_append(path):
    with open(path,'r',newline='') as file:
        content = csv.DictReader(file,delimiter=',')
        for row in content:
            if row['Name'].__eq__('Amol'):
                print(row)


write_dict_csv("sample_file.csv", employee_dict)
read_dict_csv("sample_file.csv")
append_dict_csv("sample_file.csv", {'Name': 'Amol', 'Role': 'QA Director', 'Sal':500000})
read_dict_csv_post_append("sample_file.csv")
