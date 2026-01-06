'''
✅ Summary to say in an interview:
“I use PyTest’s @pytest.mark.parametrize to run the same test with multiple data sets.
It’s very helpful for data-driven testing and covering edge cases without duplicating test code.
It keeps tests clean and increases coverage.”

🧑‍💻 Practical QA Automation usage
Use case	Example
API tests	Same endpoint, different payloads
UI tests	Same page, different login users
Edge cases	Run valid, invalid, boundary data easily

'''

'''
✅ Question:
“How do you parametrize tests in PyTest?”
- Parametrization in PyTest means running the same test multiple times with different data sets 
— without writing loops or duplicate test functions.

✅ This is very useful for:
Data-driven testing
Validating positive + negative inputs
Checking edge cases easily

🧩 How to parametrize
Use the @pytest.mark.parametrize decorator:
'''
import pytest

@pytest.mark.parametrize("x, y, result", [
    (2, 3, 5),
    (5, 5, 10),
    (10, -2, 8)
])
def test_add(x, y, result):
    assert x + y == result
#PyTest runs test_add 3 times, once for each tuple of values:
'''
📌 Key points:
✅ Feature	How it helps
Multiple test data	Cover more scenarios easily
Clear test IDs	PyTest shows each data set separately
Works with fixtures	You can parametrize a fixture too
'''

# Real Automation Project Example: Scenario: Data-driven API test with multiple payloads.
import pytest
import requests

users  = [(1, 200),(999, 404)]
@pytest.mark.parametrize("user_id, expected_status",users )
def test_get_user(user_id, expected_status):
    response = requests.get(f"https://api.example.com/user/{user_id}")
    assert response.status_code == expected_status
#  Same endpoint, multiple inputs — no duplicate code.

from selenium import webdriver
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")
    yield driver
    driver.quit()

user_creds  = [('admin', 'admin123'),('jr-engg', 'engg123')]
@pytest.mark.parametrize("username, password",users )
def test_valid_login(username, password):
    setup = driver
    driver.find_element("id", "username").send_keys(username)
    driver.find_element("id", "password").send_keys(password)
    driver.find_element("id", "loginBtn").click()
    assert "Dashboard" in driver.title