'''
Inheritance in Python allows to create a new class that reuses, extends, or modifies
the behavior of an existing class.
- It’s a fundamental OOP principle: code reuse + hierarchy + polymorphism.
- In test automation, you might use inheritance to:
   - Share common test utilities
   - Create base page objects
   - Extend generic test classes for different modules
'''

'''
“In Python, I implement inheritance by defining a base class with common behavior and then creating derived classes
that extend or override it. In automation, I use inheritance for base page objects, shared test utilities, and 
to follow the DRY principle for maintainable frameworks.”
'''


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

class LoginPage(BasePage):
    def enter_username(self, username):
        self.driver.find_element_by_id("username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id("password").send_keys(password)

    def login(self):
        self.click(("id", "loginButton"))
# Here, LoginPage inherits common actions from BasePage — reuse and maintainability!