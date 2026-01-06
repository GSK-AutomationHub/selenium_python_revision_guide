'''
✅ Q9️⃣ — Page Factory vs Plain POM — differences & use case
📌 Brief Info
Page Factory is an enhanced POM:

Uses annotations (@FindBy in Java, @property or dynamic locators in Python).

Elements are initialized automatically.

Lazy initialization — elements located only when used.

In Python Selenium, Page Factory is often done via:

__init__ method to define locators.

@property to locate elements dynamically when called.

📌 General Example
With Plain POM:

python
Copy
Edit
self.login_button = (By.ID, "loginBtn")
driver.find_element(*self.login_button).click()
With Page Factory style (Python):

python
Copy
Edit
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def login_button(self):
        return self.driver.find_element(By.ID, "loginBtn")

    def click_login(self):
        self.login_button.click()
So login_button is always fresh.

📌 Practical Automation Usage
✅ When to use Page Factory:

When you want lazy initialization.

Prevents stale element exceptions.

Cleaner syntax for element interactions.

✅ In Python:
Use dynamic @property or helper methods instead of Java-like @FindBy.

✅ In Java:
Selenium provides @FindBy + PageFactory.initElements.

✅ Pro tip:
Use either — the goal is clean, maintainable POM, not strict Page Factory magic.
'''