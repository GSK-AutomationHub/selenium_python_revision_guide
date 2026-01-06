'''
# What is an Allure Report?
 - Allure is a popular, beautiful reporting framework
 - richer than pytest-html:
    - Shows test steps, screenshots, logs, attachments.
    - Has a neat web dashboard.
    - Integrates with CI/CD.

# Why people use it:
 - It’s great for BBD-style or step-based tests.
 - It supports rich attachments: screenshots, videos, logs.

# How to generate an Allure report for PyTest
    # Install the plugin & CLI:
        pip install allure-pytest
    # Also install Allure commandline (depends on OS)
        npm install -g allure-commandline
    # Run your tests & save results to a folder:
        pytest --alluredir=allure-results
        ✅ This does NOT generate a report yet — it creates raw JSON/XML files in allure-results/.
    # Generate the report HTML from those results:
        allure serve allure-results --clean -o allure-report
        ✅ Now, allure-report/ has the fancy HTML dashboard.

# Allure report shows following details
 - Test steps
 - Parameters
 - Screenshots
 - History trends (if configured)
 - Graphs and breakdowns

| Report                                                        | How to generate                                   |
| ------------------------------------------------------------- | ------------------------------------------------- |
| ✅ **Self-contained HTML**                                    | `pytest --html=report.html --self-contained-html` |
| ✅ **Allure Report**                                          |                                                   |
| 1️⃣ `pytest --alluredir=allure-results`                        |   npm install -g allure-commandline                                             |
| 2️⃣ `allure serve allure-results -o allure-report --clean`    |                                                   |
| 3️⃣ `allure open allure-report`                               |                                                   |


✅ What to say in an interview:
“For quick, shareable reports, I use pytest-html with the --self-contained-html flag so the file works standalone.
For richer reports with test steps and attachments, I use Allure — it generates an interactive dashboard
that’s CI-friendly and shows test trends over time.”
'''

# Write a test with Allure steps & attachments
'''        
Key parts:
@allure.title → custom test name
@allure.description → detailed info
allure.step() → logical steps in report
allure.attach() → attach text, screenshots, files
'''
import allure
import requests

@allure.title("Check API Status")
@allure.description("This checks the status of the public API")
def test_api_status():
    with allure.step("Send GET request to API"):
        response = requests.get("https://api.example.com/status")
        allure.attach(response.text, name="API Response", attachment_type=allure.attachment_type.TEXT)
        assert response.status_code == 200

# Real Automation Example: UI Test with screenshot attachment
from selenium import webdriver

def take_screenshot(driver, name="screenshot"):
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

def test_homepage():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    take_screenshot(driver, "Homepage")
    assert "Example Domain" in driver.title
    driver.quit()

'''
# Run + Generate + Serve:
 - pip install allure-pytest
 - npm install -g allure-commandline
 - pytest --alluredir=allure-results
 - allure serve allure-results -o allure-report --clean
 - allure open allure-report
'''