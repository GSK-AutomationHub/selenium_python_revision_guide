'''
✅ Q5️⃣ — How do you take screenshots on test failure?
📌 Brief Info
Taking screenshots helps debug why a test failed — it shows the page state when the failure occurred.
It’s a standard best practice in robust automation frameworks.

📌 General Example
Capture and save:

python
Copy
Edit
driver.save_screenshot("screenshot.png")
or

python
Copy
Edit
driver.get_screenshot_as_file("error.png")
📌 Practical Automation Usage
✅ Example in pytest:
Use a fixture to auto-capture on failure:

python
Copy
Edit
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to get the report object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs['driver']  # Assuming driver fixture
        driver.save_screenshot(f"screenshots/{item.name}.png")
✅ Or in BasePage class:

python
Copy
Edit
def take_screenshot(self, file_name):
    self.driver.save_screenshot(file_name)
Call in your test:

try:
    assert driver.find_element(By.ID, "welcome").is_displayed()
except:
    driver.save_screenshot("error.png")
    raise
✅ Pro tip: Integrate with CI/CD to attach screenshots in Jenkins or Allure reports.
'''