'''
8️⃣ How do you run tests in parallel in PyTest?
📌 Core Conceptual Answer (for interview)
👉 By default, PyTest runs tests sequentially (one after another).
👉 To run tests in parallel, you can use the popular plugin pytest-xdist, which adds options like:

-n <num> → Run tests in parallel using <num> CPU cores.

--dist=loadscope → Better load balancing for grouped tests.

✅ This:

Speeds up test execution

Uses multiple CPU cores

Great for large test suites

✅ (A) Simple Generic Example
✅ 1️⃣ Install xdist:
bash
Copy
Edit
pip install pytest-xdist
✅ 2️⃣ Run tests in parallel with 4 workers:
bash
Copy
Edit
pytest -n 4
👉 This splits your test functions across 4 worker processes.

✅ (B) Real Automation Project Example
👉 Scenario:
You have 50 UI + API tests and want to run them faster in your CI/CD pipeline using all available CPU cores.

✅ Example folder:
bash
Copy
Edit
tests/
 ├── test_ui.py   # 10 UI tests
 ├── test_api.py  # 40 API tests
✅ Command to run all tests in parallel:
bash
Copy
Edit
pytest -n auto --html=reports/result.html --self-contained-html
-n auto → Automatically picks the number of CPU cores.

Combine with reporting (--html + --self-contained-html).

✅ Practical tips:

✅ Use parallel for API tests, unit tests — they are stateless.

⚠️ For UI tests (Selenium), parallel can conflict if using the same browser profile or shared resource → use separate browsers per worker, or run only API tests in parallel.

📌 Advanced: How to balance groups smartly
👉 --dist=loadscope helps PyTest balance grouped tests together, useful for classes/modules.

bash
Copy
Edit
pytest -n 4 --dist=loadscope
✅ Example: All tests in a class run on the same worker → avoids breaking class fixtures.

✅ How to run parallel UI tests properly
👉 Example:

bash
Copy
Edit
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
⚠️ Must ensure:

Each worker launches its own browser instance.

Don’t reuse global drivers.

Avoid writing to shared files at the same time.

✅ What to say in an interview:
“To run PyTest tests in parallel, I use the pytest-xdist plugin.
I run pytest -n <num> to distribute tests across multiple CPU cores.
For complex suites, I use --dist=loadscope to keep related tests together.
For Selenium, I ensure each worker has an isolated browser instance to avoid conflicts.”
'''