
import csv
import xml.etree.ElementTree as ET

# Read CSV rows
with open('actor_movie.csv', newline='') as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader]

# Create XML structure
root = ET.Element('Actors')

for row in rows:
    actor = ET.SubElement(root, 'Actor')
    for key, value in row.items():
        child = ET.SubElement(actor, key)
        child.text = value

# Write XML file
tree = ET.ElementTree(root)
tree.write('actor_movie.xml')

print("CSV converted to XML")
