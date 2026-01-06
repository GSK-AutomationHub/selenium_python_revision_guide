'''
✅ Q1️⃣4️⃣ — How do you run Selenium tests headless?
📌 Brief Info
Headless mode = running browser in the background without opening a UI window.
Use cases:

Faster CI/CD builds.

Running on servers without display.

📌 General Example
✅ Headless Chrome:

python
Copy
Edit
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
✅ Headless Firefox:

python
Copy
Edit
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
📌 Practical Automation Usage
✅ Framework pattern:

Accept a flag from config or command line: headless=true

Pass --headless dynamically if needed:

python
Copy
Edit
if headless:
    options.add_argument("--headless")
✅ Best practice:

Some actions behave differently in headless mode (e.g., pop-ups, screenshots).

Always test your scripts both headless and headed at least once.

✅ CI/CD:

Headless is a must on cloud runners like Jenkins, GitHub Actions, Docker containers.


'''