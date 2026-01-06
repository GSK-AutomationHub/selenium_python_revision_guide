'''

| Feature                     | Typical usage                                                                     | Will be covered?                                            |
| --------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `pytest.mark.usefixtures` | Attach a fixture to all tests in a class or module without passing it explicitly. | ✔️ *In Automation Framework questions & real sample class*  |
| `autouse=True`            | Make a fixture run automatically for all tests in scope, no explicit use needed.  | ✔️ *We’ll show autouse for session login, DB cleanup, etc.* |
| `request.cls`             | When using class-level fixtures, bind resources to the test class instance.       | ✔️ *Will show this with Selenium driver at class level.*    |

'''
# Practical Example #1 — UI Automation with usefixtures + request.cls
# Scenario: Selenium driver for each test class, without repeating fixture args.

import pytest
from selenium import webdriver

# 🔑 CLASS-scoped fixture that sets up browser and binds it to the class
@pytest.fixture(scope="class")
def init_browser(request):
    print("\n[Setup Browser]")
    driver = webdriver.Chrome()
    request.cls.driver = driver   # <-- attach to class instance
    yield
    print("\n[Teardown Browser]")
    driver.quit()

# 🔑 `usefixtures` auto-applies `init_browser` to all tests in this class
@pytest.mark.usefixtures("init_browser")
class TestLogin:

    def test_valid_login(self):
        self.driver.get("https://example.com/login")
        assert "Login" in self.driver.title

    def test_forgot_password(self):
        self.driver.get("https://example.com/forgot-password")
        assert "Forgot" in self.driver.title

'''
Key points:
request.cls.driver → attaches driver to self for all methods.
@pytest.mark.usefixtures("init_browser") → no need to pass init_browser explicitly to each test method.
Scope is class → runs once for all methods in this class.
'''

# Practical #2 — API Automation with autouse=True
# Scenario:# Log API test start/end without adding fixture to each test.

# 🔑 Session-scoped API client
@pytest.fixture(scope="session")
def api_client(requests):
    session = requests.Session()
    session.headers.update({"Authorization": "Bearer secret_token"})
    yield session
    session.close()

# 🔑 Autouse fixture — runs before/after every test automatically
@pytest.fixture(autouse=True)
def log_test_info():
    print("\n[Start Test]")
    yield
    print("[End Test]")

def test_get_user(api_client):
    response = api_client.get("https://api.example.com/user/1")
    assert response.status_code == 200

def test_get_post(api_client):
    response = api_client.get("https://api.example.com/post/1")
    assert response.status_code == 200
'''
Key points:
 - autouse=True → log_test_info runs before and after every test automatically.
 - api_client → reused for all API calls.
 - No need to explicitly call log_test_info.
'''

#  Practical #3 — Combo: UI test with both usefixtures + autouse

# 🔑 Autouse logging fixture
@pytest.fixture(autouse=True)
def log_test_step():
    print("\n[Start Test Step]")
    yield
    print("[End Test Step]")

# 🔑 Class-scoped driver fixture with request.cls
@pytest.fixture(scope="class")
def browser_setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.mark.usefixtures("browser_setup")
class TestSearch:

    def test_google(self):
        self.driver.get("https://google.com")
        assert "Google" in self.driver.title

    def test_bing(self):
        self.driver.get("https://bing.com")
        assert "Bing" in self.driver.title

'''
log_test_step auto-logs every step.
browser_setup runs once per class.
usefixtures makes all methods get the driver automatically.
'''
'''Key Takeaway
| Technique      | What it solves                                                                      |
| -------------- | ----------------------------------------------------------------------------------- |
| `usefixtures`  | Attach a fixture to all tests in a class or module **without passing it each time** |
| `autouse=True` | Force a fixture to run for every test in scope — no explicit mention                |
| `request.cls`  | Bind resource to the test class — makes `self.driver` or `self.client` available    |

'''