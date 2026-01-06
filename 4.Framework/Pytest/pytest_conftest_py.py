'''
 What is conftest.py — purpose & best practices?
📌 Concept
👉 conftest.py is a special PyTest file for:

Shared fixtures

Shared hooks

Local plugins

✅ It applies automatically to all tests in the same folder and subfolders — no import needed!

✅ Generic Example
python
Copy
Edit
# conftest.py

import pytest

@pytest.fixture
def login_data():
    return {"username": "admin", "password": "secret"}
✅ Any test in this folder can use login_data without importing it.

✅ Real Automation Example
Use-case:
Centralize Selenium browser setup.

python
Copy
Edit
# conftest.py

import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
Any test:

python
Copy
Edit
def test_homepage(browser):
    browser.get("https://example.com")
    assert "Example" in browser.title
✅ Best practice:

Put shared fixtures/hooks in conftest.py.

Never import conftest.py — PyTest auto-discovers it.

✅ What to say in interview
“I use conftest.py to keep all reusable fixtures, custom hooks, and plugins in one place.
This avoids duplication and makes the framework cleaner.”


'''