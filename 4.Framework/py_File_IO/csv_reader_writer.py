'''
Reading CSV fil can be possible using file, csv, pandas library
Filtering of rows can be possible by looping through each row and apply a condition
— keeping only the rows that match condition
'''

import csv
employee_records = [
    ['name', 'email', 'role'],
    ['Ganesh', 'ganesh@bsc.com', 'QA Lead'],
    ['Dinesh', 'dinesh@bsc.com', 'QA Mngr'],
    ['Rakesh', 'rakesh@bsc.com', 'QA engg'],
    ['Anil', 'anil@bsc.com', 'Dev Lead'],
    ['Sunil', 'ganesh@bsc.com', 'Dev Engg'],
        ]

def write_csv_file(path):
    with open(path, 'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerows(employee_records)

def read_csv_file(path):
    with open(path, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter=',')  # or '\t' for tab-separated
        for row in csv_reader:
            if row:
                print(row)

def append_to_csv_file(path, employee_record):
    with open(path, 'a', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow(employee_record)

write_csv_file('employee_role.csv')
read_csv_file('employee_role.csv')
print("-----------------------------------------------------")
append_to_csv_file('employee_role.csv', ['abhi', 'abhi@bsc.com', 'Sr.Dev Lead'])
read_csv_file('employee_role.csv')


