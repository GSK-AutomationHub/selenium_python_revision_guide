'''
✅ Q7️⃣ — How do you download files using Selenium?
📌 Brief Info
Selenium can’t handle OS-level “Save File” dialogs — instead, you configure the browser to auto-download files to a specified location without showing the pop-up.
This is crucial for verifying that files are downloaded correctly during tests.

📌 General Example
✅ For Chrome:

python
Copy
Edit
from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": "/path/to/download",  # where to save
    "download.prompt_for_download": False,  # no pop-up
    "plugins.always_open_pdf_externally": True  # PDFs auto-download
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)
Then visit a page that triggers a download — the file gets saved silently.

📌 Practical Automation Usage
✅ Example:
You want to test that a “Download Report” button works:

python
Copy
Edit
download_dir = "/Users/qauser/Downloads/test_reports"
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

driver.get("https://example.com/reports")
driver.find_element(By.ID, "downloadBtn").click()

# Then verify file exists:
import os, time

file_name = "report.pdf"
file_path = os.path.join(download_dir, file_name)

# Wait for download to complete
time.sleep(5)
assert os.path.exists(file_path)
✅ Framework tip: Parameterize download dir for test isolation.
✅ Works similarly for Firefox — use FirefoxProfile.
'''