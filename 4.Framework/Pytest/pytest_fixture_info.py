'''
✅ Question:
“What are PyTest fixtures? Explain with examples.”

📌 Core Conceptual Answer (what to say in an interview)
👉 Fixtures in PyTest are reusable setup and teardown helpers.
They:

Prepare the environment or data before a test runs

Clean up resources after the test finishes

Can be shared across multiple tests

Can pass data to tests

✅ They replace traditional setup and teardown methods with a flexible, powerful, and reusable system.

🧩 How to write a fixture
Basic fixture:

python
Copy
Edit
import pytest

@pytest.fixture
def my_fixture():
    print("\n[Setup] This runs before the test")
    yield
    print("[Teardown] This runs after the test")
Use it in a test:

python
Copy
Edit
def test_example(my_fixture):
    print("This is the actual test")
    assert True
✅ When you run:

bash
Copy
Edit
[Setup] This runs before the test
This is the actual test
[Teardown] This runs after the test
✅ How fixtures pass data
Fixtures can return data or objects for your test to use:

python
Copy
Edit
@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}

def test_data(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
📌 Key benefits:
Benefit	Why it’s useful
Reusability	Use same setup in many tests
Modularity	Combine fixtures for complex setups
Scoping	Run once per function, class, module, or session
Parametrization	Run same test with multiple data sets

🧩 Real-world QA Automation examples:
Use case	Example
Browser setup	Open a browser before test, quit after
API client	Create session, set headers, reuse connection
Test data	Load config or test data once
DB connection	Connect to DB, close after tests

✅ Scopes in real life
python
Copy
Edit
@pytest.fixture(scope="session")
def db():
    print("Connect to DB once for whole session")
    yield
    print("Disconnect DB")
python
Copy
Edit
@pytest.fixture(scope="function")
def browser():
    print("Open browser for each test")
    yield
    print("Quit browser")
✅ Summary to say in an interview:
“Fixtures are a core feature of PyTest for reusable test setup and teardown.
They help prepare test data, resources like browsers or DB connections, and ensure cleanup happens reliably. Fixtures make tests cleaner, modular, and easy to maintain.”
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