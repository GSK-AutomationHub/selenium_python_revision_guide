'''
Q2️⃣ — Explain different wait types and when to use them
Brief Info:
In UI automation, waits prevent flaky tests by giving the page enough time to load elements. Selenium provides:

Implicit Wait — sets a default wait time for all elements.

Explicit Wait — wait for a specific condition.

Fluent Wait — explicit wait with polling frequency & exception handling.

General Example:
python
Copy
Edit
# Implicit wait
driver.implicitly_wait(10)

# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "submit")))
Practical Automation Example:
In production frameworks:

Use explicit waits for elements that take time (like AJAX loads).

Keep implicit wait short or zero to avoid conflicts.

Implement custom wait_for_element helper in base class:

python
Copy
Edit
def wait_for_element(self, locator):
    wait = WebDriverWait(self.driver, 15)
    return wait.until(EC.visibility_of_element_located(locator))
'''