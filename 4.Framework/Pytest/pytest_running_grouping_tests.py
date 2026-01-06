'''  How do you run selected tests in PyTest?
# we can run  selected tests in PyTest
By file name
By node ID (test name)
By markers (-m)
By test name substring (keyword -k)

# Generic Example
    # Run specific test file:
      => pytest tests/test_login.py

    # Run specific test method in file:
      => pytest tests/test_login.py::test_valid_login

    # Run all tests with marker:
      => pytest -m smoke

    # Run tests with name substring:
      => pytest -k "login"

# Real Automation Example

    # Run only smoke tests:
      => pytest tests/ -m smoke

    # Run all regression tests:
      => pytest tests/ -m regression

    # Run only test_checkout in the e-commerce suite:
      => pytest tests/test_checkout.py::TestCheckoutFlow::test_successful_payment

# Pro tip: Combine with parallel run, reporting, or reruns:
      => pytest tests/ -m smoke -n auto --reruns 2 --html=reports/result.html

✅ What to say in interview
“I run specific tests by file, class, function name, marker, or name substring using -k.
This makes debugging and focused runs easy.”
'''