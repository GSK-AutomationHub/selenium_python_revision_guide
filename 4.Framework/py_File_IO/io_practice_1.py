import csv
employee_records = [
    ['name', 'email', 'role'],
    ['Ganesh', 'ganesh@bsc.com', 'QA Lead'],
    ['Dinesh', 'dinesh@bsc.com', 'QA Mngr'],
    ['Rakesh', 'rakesh@bsc.com', 'QA engg'],
    ['Anil', 'anil@bsc.com', 'Dev Lead'],
    ['Sunil', 'ganesh@bsc.com', 'Dev Engg'],
        ]

def write_to_csv(path,record):
    with open(path,'w',newline='') as file:
        writer = csv.writer(file,delimiter=',')
        writer.writerows(record)

def read_from_csv(path):
    with open(path,'r',newline='') as file:
        content = csv.reader(file,delimiter=',')
        for line in content:
            if line.__contains__('Ganesh'):
                print(line)


def append_to_csv(path,record):
    with open(path,'a',newline='') as file:
        writer = csv.writer(file,delimiter=',')
        writer.writerow(record)

#write_to_csv(".\\sample_file.csv",["Name","role","sal"])

write_to_csv("sample_file.csv", employee_records)

read_from_csv("sample_file.csv")

#append_to_csv(".\\sample_file.csv",["abhijit","sr.Dev Lead","100000"])


