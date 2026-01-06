'''
✅ Q6️⃣ — How do you upload a file using Selenium?
📌 Brief Info
Unlike OS pop-ups, file upload elements (<input type="file">) can be controlled directly in Selenium — no need for pyautogui or AutoIT.
Set file path to the input field.

📌 General Example
python
Copy
Edit
upload_input = driver.find_element(By.ID, "fileUpload")
upload_input.send_keys("/path/to/file.txt")
This simulates a user selecting a file.

📌 Practical Automation Usage
✅ Example:
A web form requires uploading a PDF resume.

python
Copy
Edit
# Locate file input element
file_input = driver.find_element(By.NAME, "resume")
# Provide local file path
file_input.send_keys("/Users/qauser/Downloads/resume.pdf")
✅ Framework tip:
In BasePage:

python
Copy
Edit
def upload_file(self, locator, file_path):
    self.driver.find_element(*locator).send_keys(file_path)
✅ Handling OS-level pop-up?

If the site uses a fancy button that triggers native dialog → find the hidden <input> or use AutoIT/pyautogui to handle the file dialog.

Better: check dev tools — usually there’s a hidden <input> behind a styled button.
'''