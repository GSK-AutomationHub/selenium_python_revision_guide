'''
✅ Q1️⃣1️⃣ — How do you do cross-browser testing in Selenium?
📌 Brief Info
Cross-browser testing ensures your web app works the same on:

Chrome, Firefox, Edge, Safari, etc.
Different browsers can render UI slightly differently — you catch those bugs early.

📌 General Example
In Python:

python
Copy
Edit
from selenium import webdriver

browser = "chrome"  # could be from config

if browser == "chrome":
    driver = webdriver.Chrome()
elif browser == "firefox":
    driver = webdriver.Firefox()
elif browser == "edge":
    driver = webdriver.Edge()

📌 Practical Automation Usage
✅ framework-pattern:

Accept browser name from:

Command line (pytest --browser=chrome)

Config file (config.ini or .env)

✅ Use a driver factory pattern:

python
Copy
Edit
class DriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            return webdriver.Chrome()
        elif browser == "firefox":
            return webdriver.Firefox()
        elif browser == "edge":
            return webdriver.Edge()
✅ Example:
Run same test on Chrome & Firefox:

bash
Copy
Edit
pytest --browser=chrome
pytest --browser=firefox
✅ Use Selenium Grid, BrowserStack, or Sauce Labs for large-scale cross-browser & cross-OS testing in cloud.
'''