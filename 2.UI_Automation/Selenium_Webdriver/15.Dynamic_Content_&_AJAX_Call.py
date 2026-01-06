'''
✅ Q1️⃣3️⃣ — How do you handle AJAX and dynamic content in Selenium?
📌 Brief Info
AJAX (Asynchronous JavaScript And XML) updates parts of a web page without reloading the whole page.
If your script tries to interact before the dynamic content is fully loaded, you get ElementNotFound or StaleElementReferenceException.

👉 Solution: Explicit Waits + smart locators.

📌 General Example
Wait for an element’s presence or visibility:

python
Copy
Edit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "result")))
📌 Practical Automation Usage
✅ Example:
A search box shows suggestions dynamically:

python
Copy
Edit
driver.find_element(By.ID, "searchInput").send_keys("laptop")

# Wait for suggestions to appear
wait = WebDriverWait(driver, 10)
suggestion = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//li[contains(text(),'Laptop')]"))
)
suggestion.click()
✅ Best practices:

Use EC.invisibility_of_element to wait for loaders/spinners to disappear.

Wrap waits in BasePage helpers:

python
Copy
Edit
def wait_for_loader_to_disappear(self):
    WebDriverWait(self.driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "loader"))
    )
✅ Advanced: For highly dynamic pages, use WebDriverWait with polling or even FluentWait (Java).


'''