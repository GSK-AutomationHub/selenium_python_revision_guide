'''
validating a large CSV file might include:
 - Checking headers are correct
 - Checking row count
 - Checking for duplicate rows or IDs
 - Checking for empty / missing required columns
 - Checking for specific content (e.g. status = ‘PASS’ only)
 - Spot-checking values using pytest assertions
'''

import csv

def validate_csv(file_path):
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)

        # Check header
        expected_header = ['ID', 'Name', 'Status']
        if reader.fieldnames != expected_header:
            raise ValueError(f"Header mismatch! Found: {reader.fieldnames}")

        # Initialize checks
        seen_ids = set()
        row_count = 0
        fail_count = 0

        for row in reader:
            row_count += 1

            # Check for empty fields
            for key in expected_header:
                if not row[key]:
                    raise ValueError(f"Missing value for '{key}' in row {row_count}: {row}")

            # Check duplicate ID
            if row['ID'] in seen_ids:
                raise ValueError(f"Duplicate ID found: {row['ID']}")
            seen_ids.add(row['ID'])

            # Count failed status
            if row['Status'] == 'FAIL':
                fail_count += 1

        print(f"File: {file_path}")
        print(f"Total rows: {row_count}")
        print(f"Unique IDs: {len(seen_ids)}")
        print(f"Failures found: {fail_count}")


# Call it:
validate_csv('results.csv')
print("-----------------------------------------------------------------------")

import csv
import pytest

def test_large_csv():
    with open('results.csv', newline='') as f:
        reader = csv.DictReader(f)

        expected_header = ['ID', 'Name', 'Status']
        assert reader.fieldnames == expected_header

        seen_ids = set()
        row_count = 0

        for row in reader:
            row_count += 1
            for key in expected_header:
                assert row[key] != '', f"Missing value for {key} in row {row_count}"

            assert row['ID'] not in seen_ids, f"Duplicate ID {row['ID']}"
            seen_ids.add(row['ID'])

        assert row_count > 0, "CSV should not be empty"
