'''
| Correct                                                             | Pitfall                                            |
| ------------------------------------------------------------------- | ----------------------------------------------------- |
| Always use `newline=''` when opening files for CSV on Windows.      | Forgetting `newline` can cause extra blank lines.     |
| Use `DictReader`/`DictWriter` for clarity with column names.        | Using plain `reader` makes column order matter a lot. |
| Use `with open(...)` to auto-close files.                           | Forgetting to close files manually.                   |
| Validate data types if needed (e.g., convert strings to int/float). | Assuming all fields are valid without checks.         |
| Use CSV for config/test data in automation.                         | Hardcode data in scripts.                             |


| Tool             | Use                                                |
| ---------------- | -------------------------------------------------- |
| `csv.reader`     | Simple row-by-row reading (lists)                  |
| `csv.writer`     | Simple row-by-row writing                          | writerow(list), writerows([list1, list2...)
| `csv.DictReader` | Read rows as dicts (column name access)            |
| `csv.DictWriter` | Write rows as dicts                                | writerow(dict), writerows(dict1, dict2...)
| Filter rows      | Use `if` conditions                                |
| Best practice    | `with open(..., newline='')`, parametrize in tests |

'''

# data.csv
# Name,Email,Role
# Abhijit,abhijit@bsc.com,Sr.Dev Lead
# John,john@bsc.com,Tester
# conftest.py for pytest
import csv
#import pytest

def pytest_generate_tests(metafunc):
    if 'userdata' in metafunc.fixturenames:
        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
        metafunc.parametrize('userdata', data)

def test_user_data(userdata):
    assert '@bsc.com' in userdata['Email']
