import csv

with open('employee_role.csv', 'r', newline='') as infile, \
     open('filtered.csv', 'w', newline='') as outfile:

    reader = csv.DictReader(infile, delimiter=',')
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=',')
    writer.writeheader()

    for row in reader:
        if row['role'] == 'Sr.Dev Lead':
            writer.writerow(row)

print("----------------------------------------------------------------------------------")

with open('actor_movie.csv', 'r', newline='') as input_file:
    with open('selected_movie.csv', 'w', newline='') as output_file:
        records = csv.DictReader(input_file,delimiter=',')
        fieldnames = records.fieldnames
        csv_writer = csv.DictWriter(output_file,fieldnames=fieldnames,delimiter=',')
        csv_writer.writeheader()
        #csv_writer.writerows(records)
        for record in records:
            if record['movie'] == 'DDLG':
                csv_writer.writerow(record)

print("----------------------------------------------------------------------------------")

import csv

# Open CSV file
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # Read rows as dictionaries

    # Filter: Keep rows where department == "QA"
    qa_rows = [row for row in reader if row['department'] == 'QA']

print(qa_rows)
# Output:
# [{'name': 'Alice', 'age': '30', 'department': 'QA'},
#  {'name': 'Charlie', 'age': '35', 'department': 'QA'}]

print("----------------------------------------------------------------------------------")

# pandas version
import pandas as pd

# Read CSV into DataFrame
df = pd.read_csv('data.csv')

# Filter rows: department == "QA"
qa_df = df[df['department'] == 'QA']

print(qa_df)
