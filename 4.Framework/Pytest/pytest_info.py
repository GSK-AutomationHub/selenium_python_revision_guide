'''
✅ 1️⃣ What is PyTest? Why is it popular for QA Automation?
📌 Core Conceptual Answer (what to say in an interview)
👉 PyTest is a powerful, easy-to-use testing framework for Python — used for unit, integration, API, and UI automation tests.

✅ Key reasons why it’s popular:

Reason	What it means
1️⃣ Simplicity	Write tests as simple functions, no need to extend classes.
2️⃣ Auto discovery	Finds test files & test functions automatically (e.g., test_*.py, test_*).
3️⃣ Rich assertions	No need to write self.assertEqual() like unittest — just use plain assert.
4️⃣ Fixtures	Reusable setup/teardown for test data, browsers, API sessions.
5️⃣ Plugins	Tons of plugins: pytest-html for reports, pytest-xdist for parallel execution, pytest-mock for mocking, etc.
6️⃣ Easy to parametrize	Run same test with multiple data sets without loops.
7️⃣ Integrates well	Works smoothly with CI/CD tools, supports JUnit XML, HTML reports.

🧑‍💻 How it fits QA Automation
✅ You can test:

Python helper methods (unit testing)

REST APIs (with requests)

Web UIs (with selenium, playwright)

Data-driven tests

End-to-end workflows

🔑 What to say confidently:
“PyTest is my preferred framework for Python automation because it’s simple, powerful, and highly extensible. It has built-in support for fixtures, parametrization, plugins, and integrates very well with CI/CD pipelines — which makes it a robust choice for building scalable test frameworks.”

✅ Next in sequence:
👉 2️⃣ How to write a simple PyTest test?
📌 Core Conceptual Answer (what to say in an interview)
👉 PyTest lets you write tests as plain Python functions — no need for classes or special asserts.
👉 A test file usually:

Starts with test_ in the filename (e.g., test_example.py)

Contains test functions named test_*

✅ PyTest will auto-discover and run them.

🧑‍💻 Example: A simple test
python
Copy
Edit
# test_math.py

def test_addition():
    assert 2 + 3 == 5

def test_subtraction():
    assert 5 - 2 == 3
✅ Then, run in terminal:

bash
Copy
Edit
pytest test_math.py
PyTest output:

diff
Copy
Edit
=========================== test session starts ============================
collected 2 items

test_math.py ..                                                      [100%]

============================ 2 passed in 0.01s =============================
📌 Key points:
✅ No boilerplate:

No class needed.

No main needed.

Just write functions + plain assert.

✅ Readable failures:
If an assert fails, PyTest shows the expression and values:

java
Copy
Edit
>       assert 2 + 3 == 6
E       assert 5 == 6
✅ Works for any scale:
This style works for 1 test or thousands.

✅ Summary to say in an interview:
“In PyTest, tests are simple Python functions starting with test_. We use plain assert for validation. PyTest auto-discovers and runs them, giving clear failure messages — so writing, debugging, and maintaining tests is very easy.”

📌 How to run a specific test function in a module using PyTest
👉 You don’t always want to run all tests — PyTest makes it very easy to run:

A single test file

A single test class

A single test method

✅ Syntax:
bash
Copy
Edit
pytest <file_name>::<test_function_name>
✅ Example:

Suppose you have:

python
Copy
Edit
# test_math.py

def test_addition():
    assert 2 + 3 == 5

def test_subtraction():
    assert 5 - 2 == 3
To run only test_addition:

bash
Copy
Edit
pytest test_math.py::test_addition
✅ For a method inside a class:
Suppose:

python
Copy
Edit
# test_calc.py

class TestCalc:
    def test_add(self):
        assert 2 + 2 == 4

    def test_subtract(self):
        assert 5 - 2 == 3
Run only the test_subtract method:

bash
Copy
Edit
pytest test_calc.py::TestCalc::test_subtract
✅ Pro tip:
You can even run:

An entire test class:

bash
Copy
Edit
pytest test_calc.py::TestCalc
All test files matching a pattern:

bash
Copy
Edit
pytest tests/ --maxfail=1 --disable-warnings
✅ Why this is useful:
Debugging a flaky test → run just that one.

Developing a new test → run it repeatedly, not the whole suite.

Faster feedback during development.

✅ One-liner answer to say in interview:
“PyTest lets me run a specific test by using the syntax <file>::<function> or <file>::<class>::<method>.
This is very handy for debugging individual test cases without running the entire suite.”


'''