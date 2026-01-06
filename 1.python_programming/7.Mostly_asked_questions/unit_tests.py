'''
Where unit tests help a QA Automation Lead:
Sometimes you do write utility methods and helper libraries for your framework — for example:

A wrapper for an API client

A helper for DB calls

A custom logger

In such cases, you might use unit tests to verify these helper methods before using them in big E2E tests.
But this is a secondary focus.

✅ 1️⃣ Quick, practical brief on unit tests (in QA Automation context)
👉 Unit tests in Python check small, isolated units of code (like a single function or method).
They help ensure that low-level helper functions work correctly before you plug them into bigger workflows like UI tests, API tests, or end-to-end tests.

✅ For a QA Automation Lead, you might write unit tests for:

Custom utilities: e.g., an encryption/decryption helper.

API client methods: e.g., a wrapper for GET/POST calls.

Internal logic: e.g., a data parser used by multiple tests.

🔑 How to write unit tests
Python has a built-in unittest module, but for QA automation we often use pytest, which is simpler and more powerful.

Example: testing a helper function:

python
Copy
Edit
# my_utils.py
def add(x, y):
    return x + y
python
Copy
Edit
# test_my_utils.py
from my_utils import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
✅ Then run:

bash
Copy
Edit
pytest test_my_utils.py
Result: It checks add() independently — fast and reliable.

✅ When do I use unit vs integration vs automation tests?
Level	Purpose	Example
Unit test	Smallest piece of logic	Test one function: add()
Integration test	Test multiple parts together	Check DB query + API + data transformation
Automation test (E2E)	Test real user flow	Login → Add item → Checkout

👉 As a QA Automation Lead, you mostly write & maintain automation tests, but you might use unit tests for your framework’s helper modules to catch bugs early.

✅ Key point to say in interview:
“Unit tests help me verify my helper methods work as expected in isolation. I use pytest to write simple assertions. This ensures my automation framework remains robust and reusable.”
'''