'''
✅ Q1️⃣2️⃣ — How do you run tests in parallel?
📌 Brief Info
Parallel execution reduces total test time — multiple tests run at the same time instead of one after another.
This is critical for large test suites.

📌 General Example
✅ In pytest, use pytest-xdist:

bash
Copy
Edit
pytest -n 4  # run using 4 CPUs
📌 Practical Automation Usage
✅ Framework pattern:

Ensure tests are independent (no shared state).

Use separate driver instances per test:

python
Copy
Edit
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
✅ Cross-browser + parallel: Combine:

bash
Copy
Edit
pytest -n 2 --browser=chrome
pytest -n 2 --browser=firefox
✅ CI/CD best practice: Use parallel runners in Jenkins, GitHub Actions, or cloud grids for max speed.


'''