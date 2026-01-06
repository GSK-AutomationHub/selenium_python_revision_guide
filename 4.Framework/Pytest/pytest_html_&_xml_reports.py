'''
How do you generate HTML or JUnit reports in PyTest?
 - For HTML reports, the popular plugin is pytest-html.
 - For machine-readable reports (for CI/CD), the built-in --junitxml flag is widely used.

# (A) Simple Generic Example
    # Generate a HTML report
        # Install the plugin : pip install pytest-html
        # Run tests and create HTML report : pytest --html=report.html
        # This generates report.html in your project folder

    # What is a self-contained HTML report?
        # regular HTML report (--html=report.html) may reference separate CSS/JS files →
        so if you email it, people might see broken formatting unless they have the extra files.
        # A self-contained HTML report means:
            # All CSS, JS, images, styles are embedded directly inside the single .html file.
            # So you can share just the file — it works perfectly standalone.
            # we can email the report, upload it to a portal, or archive it without missing assets.

    # How to generate a self-contained HTML report
        # pytest --html=report.html --self-contained-html

    # Generate a JUnit XML report
        # Built-in: no extra plugin needed
        # Run tests: pytest --junitxml=report.xml
        # CI tools like Jenkins can parse this report.xml and show results.

# (B) Real Automation Project Example
 Example structure:
tests/
  ├── test_ui.py
  ├── test_api.py

Run from root:
pytest tests/ --html=report.html --self-contained-html --junitxml=reports/result.xml
✅ tests/ → your folder with tests
✅ reports/ → output folder for reports

test_ui.py:
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.smoke
def test_homepage(browser):
    browser.get("https://example.com")
    assert "Example Domain" in browser.title
test_api.py:

import requests

@pytest.mark.regression
def test_api_status():
    response = requests.get("https://api.example.com/status")
    assert response.status_code == 200

# What you gain:
Report	        Use case
HTML	        Human-friendly: share with QA/PM
JUnit XML	    Machine-friendly: plug into Jenkins, Bamboo, GitLab CI, etc.

# Pro Tip: Combine both
pytest tests/ --html=report.html --self-contained-html --junitxml=reports/result.xml

# What to say in an interview:
“For reporting, I use pytest-html to generate clear HTML reports for stakeholders,
and --junitxml to generate machine-readable XML reports for CI/CD tools.
This helps track test results, failures, and trends across builds.”
'''