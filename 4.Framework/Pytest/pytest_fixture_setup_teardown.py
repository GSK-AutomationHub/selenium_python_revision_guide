'''
✅ Question:
“How do you use setup and teardown in PyTest?”

📌 Core Conceptual Answer (what to say in an interview)
👉 In PyTest, setup and teardown are done using fixtures — these are powerful reusable blocks for preparing and cleaning up test context.
👉 You can use:

Classic setup_method and teardown_method (like unittest style) → works for classes.

Modern @pytest.fixture → most common, more flexible!

🧩 1️⃣ Class-based setup/teardown
Example with setup_method and teardown_method:

python
Copy
Edit
class TestExample:
    def setup_method(self):
        print("\nSetup before each method")

    def teardown_method(self):
        print("\nTeardown after each method")

    def test_one(self):
        print("Running test one")
        assert True

    def test_two(self):
        print("Running test two")
        assert True
✅ When you run this:

pgsql
Copy
Edit
Setup before each method
Running test one
Teardown after each method

Setup before each method
Running test two
Teardown after each method
🧩 2️⃣ Fixture-based setup/teardown (Recommended)
✅ This is the PyTest best practice:

python
Copy
Edit
import pytest

@pytest.fixture
def setup_and_teardown():
    print("\nSetup: connect to DB / open browser")
    yield
    print("\nTeardown: disconnect DB / close browser")

def test_one(setup_and_teardown):
    print("Running test one")
    assert True

def test_two(setup_and_teardown):
    print("Running test two")
    assert True
✅ yield separates setup (before yield) and teardown (after yield).

✅ Why use fixtures over classic setup/teardown?
Classic	Fixture
Fixed names: setup_method	Flexible names: @pytest.fixture
Only for classes	Works for functions, classes, modules, session
Less powerful	Can pass data, parametrize, scope control

📌 Key scopes:
PyTest fixtures can have different scopes:

Scope	Runs...
function (default)	Before & after each test function
class	Once per test class
module	Once per file
session	Once per test run

Example:

python
Copy
Edit
@pytest.fixture(scope="module")
def db_connection():
    print("\n[Setup] Connect to DB")
    yield
    print("\n[Teardown] Disconnect DB")
✅ What to say in an interview:
“In PyTest, I use fixtures for setup and teardown — they’re more flexible than the classic setup_method.
Fixtures can prepare test data, open browsers, connect to DBs, and clean up after tests finish.
I can control their scope and reuse them across multiple tests or modules.”
'''

# Real Automation Project Example :  API tests with a reusable authenticated session.
import pytest
import requests

@pytest.fixture
def api_client():
    session = requests.Session()
    session.headers.update({"Authorization": "Bearer YOUR_TOKEN"})
    yield session
    session.close()

def test_get_user(api_client):
    response = api_client.get("https://api.example.com/user/1")
    assert response.status_code == 200
    assert "username" in response.json()

'''
The fixture prepares an authenticated API session.
After the test, the session is closed.
'''
# Real Automation Project Example :  UI tests

from selenium import webdriver
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")
    yield driver
    driver.quit()

def test_valid_login(setup):
    setup = driver
    driver.find_element("id", "username").send_keys("admin")
    driver.find_element("id", "password").send_keys("password")
    driver.find_element("id", "loginBtn").click()
    assert "Dashboard" in driver.title