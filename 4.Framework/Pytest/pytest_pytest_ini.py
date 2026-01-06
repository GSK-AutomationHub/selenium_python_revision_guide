'''
# What is pytest.ini — how to use it?
 - pytest.ini is PyTest’s configuration file. It stores:
   - Custom markers (to avoid warnings)
   - Base test paths
   - Addopts (default CLI flags)
   - Logging settings

# Generic Example : pytest.ini:
[pytest]
markers =
    smoke: quick health check
    regression: detailed tests

addopts = --maxfail=2 --disable-warnings

==> markers → declare custom tags
==> addopts → default CLI flags (here: fail fast after 2 fails)

# Real Automation Example: Structure:
project/
 ├── tests/
 ├── reports/
 ├── pytest.ini

pytest.ini:
[pytest]
markers =
    smoke: smoke tests for quick check
    regression: full regression suite
addopts = -v --html=reports/result.html --self-contained-html
testpaths = tests

==> This runs all tests in tests/, generates a report, and uses verbose mode by default.

✅ What to say in interview
“I use pytest.ini to define custom markers, set default CLI options like reports and verbosity,
and control which folders to collect tests from. It keeps the project consistent and easy to run.”

'''