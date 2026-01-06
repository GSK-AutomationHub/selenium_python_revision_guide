'''
Q8️⃣ — What is Page Object Model (POM) and its benefits?
📌 Brief Info
POM is a design pattern for organizing automation code:

Each web page = a Page class

Page class contains:

Locators

Page-specific actions/methods

Benefits:

Code reuse

Easy maintenance

Clear separation: locators + actions separate from test logic

📌 General Example
LoginPage.py

python
Copy
Edit
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
📌 Practical Automation Usage
✅ Example Test:

python
Copy
Edit
from pages.login_page import LoginPage

login_page = LoginPage(driver)
login_page.login("user1", "pass123")

# Then assert next page element
assert driver.find_element(By.ID, "welcome").is_displayed()
✅ Benefits in large projects:

Changing a locator? Update one place.

Test logic is clean & readable:

python
Copy
Edit
def test_valid_login(login_page):
    login_page.login("admin", "admin123")
✅ Industry standard: All major frameworks (Selenium-Python, Java, C#) use POM.
'''