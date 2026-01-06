import csv
import employee_table

with open('employee_record.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file,delimiter='\t')
    header = ['first_name', 'last_name', 'pay']
    csv_writer.writerow(header)
    employee_records = employee_table.setup_db_records()
    for record in employee_records:
        csv_writer.writerow(record)
        print('\n')

with open('employee_record.csv', 'r') as csv_read_file:
    csv_read = csv.reader(csv_read_file,delimiter='\t')
    for record in csv_read:
        if not record == []:
            print(record)
