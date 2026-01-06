'''
✅ Q🔟 — How do you implement data-driven testing in Selenium?
📌 Brief Info
Data-driven testing (DDT) means running the same test logic multiple times with different input data.
Benefits:

Covers more scenarios with less code

Easy to add new test cases just by changing data
Commonly done using:

Excel / CSV files

JSON / YAML

Database

Fixtures or parameterization in pytest

📌 General Example
CSV example (Python + pytest):

✅ Sample CSV: data.csv

pgsql
Copy
Edit
username,password
admin,admin123
guest,guest123
✅ Test:

python
Copy
Edit
import csv
import pytest

def read_csv():
    with open('data.csv') as f:
        rows = csv.DictReader(f)
        return [(row['username'], row['password']) for row in rows]

@pytest.mark.parametrize("username,password", read_csv())
def test_login(username, password):
    driver.get("https://example.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "loginBtn").click()
    # Assert login success
📌 Practical Automation Usage
✅ In real frameworks:

Put your test data in:

CSV → good for simple tabular data

JSON/YAML → better for nested data

DB query → live test data

✅ Use pytest @pytest.mark.parametrize — simplest & robust.

✅ Keep data files in a separate /testdata folder.

✅ CI/CD best practice: Validate with multiple data sets in one run.
'''