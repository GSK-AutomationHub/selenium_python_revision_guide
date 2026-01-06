import csv

path = 'employee_role.csv'
employee_record = ['amit', 'amit@bsc.com', 'Manager']

def csv_reader_decorator(myfunc):
    def wrapper(*args):
        print(f"Arguments passed to {myfunc.__name__}:")
        print("Positional arguments:", args)
        myfunc(*args)
        with open(path, 'r', newline='') as file:
            csv_reader = csv.reader(file, delimiter=',')  # or '\t' for tab-separated
            for row in csv_reader:
                if row:
                    print(row)
    return wrapper

@csv_reader_decorator
def add_new_csv_record(file_path, record):
    with open(file_path, 'a', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow(record)


add_new_csv_record(path, employee_record)