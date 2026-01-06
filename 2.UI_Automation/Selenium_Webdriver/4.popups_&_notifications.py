'''
Q3 (Extended) — How do you handle ALL types of pop-ups & browser permission prompts in Selenium?
📌 Brief Info
Web apps can show:

JavaScript pop-ups (alerts, confirm, prompt)

Custom HTML modals

Browser permission pop-ups: Notifications, Geolocation

HTTP Basic Authentication pop-ups (username/password dialog)

Cookie consent banners

OS-level pop-ups (downloads, print dialog — Selenium can’t handle directly)

Each requires a different handling strategy:

JavaScript & HTML modals: Selenium directly.

Permissions & cookies: Use browser options, auto-allow or disable.

Authentication pop-ups: Embed credentials in URL or use Selenium’s support.

OS-level: Use workarounds or external tools.

📌 General Examples
✅ 1️⃣ JavaScript Alerts, Confirm, Prompt
As before:

python
Copy
Edit
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("value")  # For prompt
alert.accept() or alert.dismiss()
✅ 2️⃣ Custom HTML Pop-up
Locate and interact normally:

python
Copy
Edit
driver.find_element(By.ID, "closeModal").click()
✅ 3️⃣ Browser Notifications
Disable at driver startup:

python
Copy
Edit
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
✅ 4️⃣ Geolocation Pop-up
Auto-deny or auto-allow using browser profile:

python
Copy
Edit
options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.geolocation": 1  # 1=Allow, 2=Block
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)
✅ 5️⃣ Authentication Pop-up
Use username:password in the URL:

bash
Copy
Edit
https://username:password@yourdomain.com/securepage
Note: Some browsers block this now. For advanced auth, use requests or custom solutions (e.g., handle via API first).

✅ 6️⃣ Cookie Consent Banner
Locate the accept/reject button & click it:

python
Copy
Edit
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Accept All']"))
).click()
Alternatively, handle via JavaScript:

python
Copy
Edit
driver.execute_script("document.cookie = 'cookieConsent=true';")
✅ 7️⃣ OS-level Pop-ups (Downloads, Print Dialog)
Use ChromeOptions to auto-download files.

Use pyautogui or tools like AutoIT for file upload pop-ups (Windows file picker).

📌 Practical Automation Role Usage
✅ In a robust framework:

For notifications/geolocation: pre-configure driver with the right preferences.

For auth pop-ups: test via API if possible, or handle at URL level if allowed.

For cookie banners: create a reusable method in BasePage:

python
Copy
Edit
def handle_cookie_banner(self):
    try:
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Accept']"))
        ).click()
    except TimeoutException:
        pass  # No banner appeared
For HTML modals: treat like any other page element with explicit waits.

For downloads/uploads: set Chrome download directory and auto download preferences.

✅ Key Takeaway
👉 One solution does NOT fit all pop-ups!
👉 Use browser options for permissions.
👉 Use switch_to.alert for JavaScript alerts.
👉 Use locators for HTML modals and banners.
👉 For authentication/OS pop-ups, prefer config or external helpers.


'''