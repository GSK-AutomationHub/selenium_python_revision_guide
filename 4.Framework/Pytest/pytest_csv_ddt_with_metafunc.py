'''

# metafunc and metafunc.fixturenames: PyTest’s powerful dynamic parametrization feature.
 - pytest_generate_tests = hook to generate dynamic test cases.
 - metafunc = object holds info about the test function(s) that need params
   i.e. test function collected & fixtures it needs
 - metafunc.fixturenames = it is a list of fixture names that test function uses.
 - metafunc.parametrize = attach params.

'''

import csv
import pytest

# Step 1: Load CSV data at test collection time
def pytest_generate_tests(metafunc):
    if 'userdata' in metafunc.fixturenames:
        with open('test_data.csv', newline='') as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
        metafunc.parametrize('userdata', data)

# Step 2: Use the CSV data as a fixture
def test_email_format(userdata):
    email = userdata['email']
    assert '@' in email and '.' in email, f"Invalid email: {email}"

def test_role_check(userdata):
    valid_roles = ['Sr.Dev Lead', 'Tester']
    assert userdata['role'] in valid_roles, f"Unexpected role: {userdata['role']}"

# Step 3: Write the test result to CSV
def test_csv_write_result():
    results = [
        {'Test': 'Email Format', 'Status': 'PASS'},
        {'Test': 'Role Check', 'Status': 'FAIL'}
    ]
    with open('results.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Test', 'Status'])
        writer.writeheader()
        writer.writerows(results)

