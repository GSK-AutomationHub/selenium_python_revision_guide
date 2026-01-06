'''
✅ Question:
“How would you handle logging in Python automation projects?”

📌 Core Conceptual Answer (what to say in an interview)
👉 In Python, we use the built-in logging module to:

Write logs to console and/or files.

Control log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).

Format log messages nicely.

Rotate logs if needed (via handlers).

✅ This helps debug tests, record failures, and analyze what happened during execution.

🧑‍💻 Basic Example
python
Copy
Edit
import logging

# 1️⃣ Basic config — log to console + file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("test.log"),
        logging.StreamHandler()
    ]
)

# 2️⃣ Log some messages
logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING")
logging.error("This is an ERROR")
logging.critical("This is CRITICAL")
✅ Creates test.log and shows same logs on console.

✅ In Automation Projects
Best practice	Example
Use logging instead of print()	More control, better timestamps
Configure a log file per test run	Easier to trace failures
Add context: test name, step info	Helps debugging
Rotate or archive logs	Prevent huge files

🗂️ Pytest integration tip
Many Pytest plugins (like pytest-html or pytest-logger) capture logs.

You can add a conftest.py fixture to configure logging globally.

Example conftest.py snippet:

python
Copy
Edit
import logging
import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("automation.log"),
            logging.StreamHandler()
        ]
    )
✅ This runs once per test session → consistent logs for the entire suite.

✅ Summary to say in an interview:
“I use Python’s logging module for structured, timestamped logs instead of print statements. I configure logs to write to both console and log files. In Pytest, I often use a session-scoped fixture to initialize logging for all tests. This makes debugging and reporting clear and professional.”
'''