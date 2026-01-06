'''
Brief Info:
Modern web applications show various pop-ups:
1️⃣ JavaScript Alerts — Simple message + OK
2️⃣ Confirmation Alerts — Message + OK & Cancel
3️⃣ Prompt Alerts — Message + Text input + OK/Cancel
4️⃣ Browser pop-ups — OS-level (like download dialog) — Selenium can’t handle these directly.
5️⃣ HTML pop-ups / Modals — Custom dialogs built with HTML/CSS/JS — handled like normal web elements.

Q3️⃣ — How do you handle alerts in Selenium?
Brief Info:
Web apps often show JavaScript alerts or pop-ups for confirmation. If you don’t handle them, Selenium throws UnhandledAlertException or tests hang.
General Examples:
✅ 1) Simple Alert
alert = driver.switch_to.alert
print(alert.text)
alert.accept()  # Click OK

✅ 2) Confirmation Alert
alert = driver.switch_to.alert
print(alert.text)
alert.accept()  # Click OK
# or
alert.dismiss()  # Click Cancel

✅ 3) Prompt Alert (input text)
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("Sample input")  # Type into prompt
alert.accept()

Practical Automation Example:
In real tests: After clicking a ‘Delete’ button, confirm alert:
delete_button.click()
alert = driver.switch_to.alert
assert "Are you sure" in alert.text
alert.accept()  # Confirm deletion
Wrap in try-except for robustness:
try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
except TimeoutException:
    print("No alert appeared.")
'''
print("------------------------------ pop-ups ---------------------------------------")

'''
Q3️⃣ — How do you handle pop-ups in Selenium?

✅ 4) HTML Pop-up (Modal)
Inspect and handle as normal web elements:
modal_close = driver.find_element(By.XPATH, "//button[text()='Close']")
modal_close.click()
✅ 5) Browser Pop-up (OS Dialog)
Selenium alone cannot handle OS-level pop-ups (like file download pop-ups). Solutions:

Use ChromeOptions to auto-download files.

Use tools like AutoIT or Robot in Java, or Python’s pyautogui.

Practical Automation Usage:
🔹 In your test framework:
Always wrap alert handling in try-except + explicit wait for robustness:

python
Copy
Edit
try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
except TimeoutException:
    print("No alert appeared.")
For HTML modals (like Bootstrap modals, pop-up login forms):
# Wait until modal is visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginModal")))
driver.find_element(By.ID, "closeModal").click()
For download pop-ups:

Use ChromeOptions:
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": "/path/to/download"}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)
✅ Key Takeaway:
👉 Always check what type of pop-up you’re dealing with!
👉 JavaScript pop-ups → switch_to.alert
👉 HTML modals → locate elements as normal
👉 OS pop-ups → use browser capabilities or external tools

'''