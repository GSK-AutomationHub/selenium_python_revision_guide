'''
✅ Q4️⃣ — How do you handle multiple windows or browser tabs in Selenium?
📌 Brief Info
Modern web apps often open links in new tabs/windows (e.g., clicking ‘Help’ or ‘Terms & Conditions’).
Your test needs to:

Switch to the new window,

Perform actions,

Switch back to the main window.

Failing to switch = Selenium can’t find elements in the new tab.

📌 General Example
1️⃣ Get current window handle:

python
Copy
Edit
main_window = driver.current_window_handle
2️⃣ Click link → new window opens.

3️⃣ Get all windows:

python
Copy
Edit
all_windows = driver.window_handles
4️⃣ Switch to new one:

python
Copy
Edit
for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        break
5️⃣ Do stuff → then switch back:

python
Copy
Edit
driver.switch_to.window(main_window)
📌 Practical Automation Usage
✅ Example:
Test opens a product page → clicks “Write Review” → new tab opens.

python
Copy
Edit
main_window = driver.current_window_handle
driver.find_element(By.LINK_TEXT, "Write Review").click()

WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
for window in driver.window_handles:
    if window != main_window:
        driver.switch_to.window(window)
        break

# Perform actions in new window
driver.find_element(By.ID, "reviewText").send_keys("Great product!")

# Close new tab & return
driver.close()
driver.switch_to.window(main_window)
✅ Framework tip: Wrap in a helper:

python
Copy
Edit
def switch_to_new_window(self, main_handle):
    for handle in self.driver.window_handles:
        if handle != main_handle:
            self.driver.switch_to.window(handle)
            break

'''