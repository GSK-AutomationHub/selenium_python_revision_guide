''' How do you rerun failed tests in PyTest?

 - using plugin pytest-rerunfailures to rerun failed tests automatically
 — useful for flaky tests due to network/API flakiness.

# Generic Example
 - Install: pip install pytest-rerunfailures
 - Run with rerun: pytest --reruns 2
 - This will rerun failed tests up to 2 times.

# Real Automation Example
  => pytest tests/ --reruns 3 --reruns-delay 5
  => --reruns 3 → Rerun failed tests up to 3 times.
  => --reruns-delay 5 → Wait 5 seconds between reruns.

# Use case:
  - Unstable cloud infra or slow API server
  - here use of rerun prevents flaky failures from breaking CI.

✅ What to say in interview
“For flaky tests, I use pytest-rerunfailures to auto rerun failures
a few times before marking the test as failed. It helps stabilize CI runs.”
'''