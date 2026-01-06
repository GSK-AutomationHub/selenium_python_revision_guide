import csv
import json
'''
- csv.DictReader makes conversion simple:
- JSON: json.dump(rows) ---> note here need to use json.dump() and not json.dumps()
- json.dump(list_of_dict, file_name, indent-4)
'''
# Read CSV rows
with open('actor_movie.csv', 'r', newline='') as csv_file:
    records = csv.DictReader(csv_file)
    rows = [row for row in records]
    print(rows)

# Write to JSON file
with open('actor_movie.json', 'w', newline='') as json_file:
    json.dump(rows,json_file,indent=4)
