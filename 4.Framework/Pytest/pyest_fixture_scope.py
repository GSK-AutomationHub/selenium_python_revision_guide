''' all 4 fixture scopes (function, class, module, session)
Each with: a non-parametrized real-life usage, a parametrized real-life usage

| Scope      | Non-Parametrized Example         | Parametrized Example              |
| ---------- | -------------------------------- | --------------------------------- |
| `function` | Open/close browser for each test | Cross-browser (Chrome, Firefox)   |
| `class`    | DB connection per test class     | User roles: admin, guest          |
| `module`   | API token for one file           | Environments: staging, production |
| `session`  | DB setup for whole suite         | API version: v1, v2               |
'''
######################## FUNCTION scope (default) ########################
# Runs before/after every single test function
#A) Non-parametrized: Function-scope browser


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_title(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title

#B) Parametrized: Function-scope multiple browsers

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")
    yield driver
    driver.quit()

def test_cross_browser(browser):
    browser.get("https://google.com")
    assert "Google" in browser.title
# Here, each test runs once for each browser.

######################## CLASS scope ########################
#Runs once per test class: setup before first method, teardown after last
#A) Non-parametrized: Class-scope DB connection

@pytest.fixture(scope="class")
def db_connection():
    print("\n[Connect DB]")
    conn = "db_connection_object"
    yield conn
    print("\n[Disconnect DB]")

class TestDB:
    def test_read_data(self, db_connection):
        print("Reading data using", db_connection)
        assert db_connection == "db_connection_object"

    def test_write_data(self, db_connection):
        print("Writing data using", db_connection)
        assert True
#One DB connection for the whole class.

#B) Parametrized: Class-scope user types

@pytest.fixture(scope="class", params=["admin", "guest"])
def user_role(request):
    print(f"\n[Setup user: {request.param}]")
    yield request.param
    print(f"\n[Teardown user: {request.param}]")

#pytest.mark.userfixtures("user_role")
class TestUserAccess:
    def test_access_dashboard(self, user_role):
        # dont need to pass fixture to function if used pytest.mark.usefixtures()
        print(f"Checking dashboard for {user_role}")
        assert user_role in ["admin", "guest"]

    def test_access_settings(self, user_role):
        if user_role == "guest":
            assert False, "Guests should not access settings"
        else:
            assert True
# Runs both tests once for admin, once for guest.

######################## Module scope ########################

# A) Non-parametrized: API token for all tests in file

@pytest.fixture(scope="module")
def api_token():
    print("\n[Get API token once for module]")
    token = "my_token"
    yield token
    print("\n[Expire token]")

def test_api_call_one(api_token):
    print(f"Call one with token: {api_token}")
    assert api_token == "my_token"

def test_api_call_two(api_token):
    print(f"Call two with token: {api_token}")
    assert api_token == "my_token"
# One token used for all tests in this file.

# B) Parametrized: Module-scope environment

@pytest.fixture(scope="module", params=["staging", "production"])
def environment(request):
    print(f"\n[Setup environment: {request.param}]")
    yield request.param
    print(f"\n[Teardown environment: {request.param}]")

def test_env_one(environment):
    print(f"Running in {environment}")
    assert environment in ["staging", "production"]

def test_env_two(environment):
    print(f"Also running in {environment}")
    assert environment in ["staging", "production"]
# Both tests run once for staging, once for production.