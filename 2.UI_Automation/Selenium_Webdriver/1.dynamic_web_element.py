'''
Q1️⃣ — How do you handle dynamic web elements in Selenium?
Brief Info:
Dynamic elements have changing attributes (like IDs or XPath) on each page load. If not handled, your locators will break. Robust locators and smart strategies are essential for stable automation.

General Example:
Suppose a login button has a dynamic ID like btn_123, btn_456. Instead of using By.ID("btn_123"), use XPath:

python
Copy
Edit
driver.find_element(By.XPATH, "//button[text()='Login']")
Or use partial match with contains:

python
Copy
Edit
driver.find_element(By.XPATH, "//button[contains(@id, 'btn_')]")
Practical Automation Example:
In a real project, you’d:

Prefer By.XPATH or By.CSS_SELECTOR with stable attributes (like text, class).

Use relative XPaths instead of absolute.

Example:

python
Copy
Edit
# Robust locator for dynamic 'Add to Cart' button
add_to_cart = driver.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]")
add_to_cart.click()
Maintain locators in your POM so updates are centralized.
'''