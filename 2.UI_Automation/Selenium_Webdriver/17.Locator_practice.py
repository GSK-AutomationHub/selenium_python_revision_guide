'''
✅ Q1️⃣5️⃣ — What are the best practices for locators & framework maintainability?
📌 Brief Info
Bad locators = flaky tests.
Clean locators = stable, maintainable framework.

👉 Industry expects you to know how to write robust locators + organize them well.

📌 General Example
✅ Good practices:

Prefer ID or unique class names.

Use relative XPath over absolute.

Use contains(), starts-with(), text() for dynamic parts.

Use CSS selectors for speed:

python
Copy
Edit
driver.find_element(By.CSS_SELECTOR, "input[name='username']")
📌 Practical Automation Usage
✅ Framework structure:

Use POM: keep locators inside Page classes.

Name locators clearly:

python
Copy
Edit
self.username_input = (By.ID, "username")
✅ Reusability:

Avoid repeating locators in multiple tests.

Keep them in one place (Page classes or a separate Locators.py).

✅ Robust XPath:

python
Copy
Edit
# Bad: Absolute
/html/body/div[2]/div/form/input[1]

# Good: Relative
//form[@id='loginForm']//input[@name='username']
✅ Dynamic content:
Handle attribute changes using contains:

python
Copy
Edit
//button[contains(@id, 'submit')]
✅ Review regularly:

Use browser dev tools ($0 in console) to debug locators.

Avoid using Thread.sleep() for synchronization — use waits instead.

✅ 🎉 Selenium Section Complete!
You now have:
✔️ 15 robust, industry-relevant Selenium + UI Automation questions
✔️ Each with practical, real-world examples

'''