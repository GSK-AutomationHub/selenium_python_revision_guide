'''
Knowing the type helps choose the correct handling strategy.
Real Framework Structure — UI & API in PyTest
📌 Concept
👉 Real-world robust PyTest project:

Follows Page Object Model (POM) for UI

Separates API layer

Uses conftest.py for fixtures

Uses markers, parametrize, reports

✅ Example Folder Layout
Copy
Edit
project_root/
 ├── tests/
 │   ├── ui/
 │   │   ├── test_login.py
 │   │   ├── test_checkout.py
 │   ├── api/
 │   │   ├── test_users.py
 │   │   ├── test_orders.py
 ├── pages/
 │   ├── login_page.py
 │   ├── checkout_page.py
 ├── conftest.py
 ├── pytest.ini
 ├── requirements.txt
✅ Key Parts
✅ pages/login_page.py
python
Copy
Edit
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "loginBtn")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
✅ tests/ui/test_login.py
python
Copy
Edit
from pages.login_page import LoginPage

def test_valid_login(browser):
    login_page = LoginPage(browser)
    browser.get("https://example.com/login")
    login_page.login("admin", "password")
    assert "Dashboard" in browser.title
✅ tests/api/test_users.py
python
Copy
Edit
import requests

def test_get_user():
    response = requests.get("https://api.example.com/user/1")
    assert response.status_code == 200
✅ conftest.py
python
Copy
Edit
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
✅ pytest.ini
ini
Copy
Edit
[pytest]
markers =
    smoke: Quick checks
    regression: Detailed suite
addopts = -v --html=reports/result.html --self-contained-html
testpaths = tests
✅ What to say in interview
“I design PyTest frameworks with a clear folder structure, POM for UI, REST calls for API, reusable fixtures in conftest.py, and separate tests by type.
I use markers, parametrize, Allure, and CI pipelines for robust test automation.”


'''