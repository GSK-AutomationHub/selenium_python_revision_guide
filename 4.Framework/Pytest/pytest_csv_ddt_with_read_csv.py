import csv
import pytest

def read_csv():
    with open('test_data.csv', newline='') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

@pytest.mark.parametrize("userdata", read_csv())
def test_email_format(userdata):
    email = userdata['email']
    assert '@' in email and '.' in email

@pytest.mark.parametrize("userdata", read_csv())
def test_role_check(userdata):
    valid_roles = ['Sr.Dev Lead', 'Tester']
    assert userdata['role'] in valid_roles
