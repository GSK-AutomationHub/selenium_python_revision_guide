'''
What are Hooks in PyTest?
 - Hooks are special functions PyTest calls during different phases of the test lifecycle:
   - Collecting tests
   - Running tests
   - Reporting results
   - e.g. pytest_generate_test which uses metafunc, metafunc.fixturenames, metafunc.parametrize

What are Plugins in PyTest?
 - Plugins extend PyTest’s behavior — a plugin can:
   - Add new CLI options
   - Add or change hooks
   - Provide new fixtures
   - PyTest has built-in plugins: xdist, html, order, rerunfailures are all plugins!
'''

# Generic Example — Using a Hook
# Create a conftest.py to customize reports:

def pytest_runtest_setup(item):
    print(f"\n[Hook] About to run: {item.name}")

def pytest_runtest_teardown(item, nextitem):
    print(f"\n[Hook] Finished: {item.name}")

# These built-in hooks run before and after each test.

# Real Automation Example
# Use-case: Log test start/finish to a custom log file for audit.
# conftest.py

import logging

def pytest_configure(config):
    logging.basicConfig(filename='test.log', level=logging.INFO)

def pytest_runtest_setup(item):
    logging.info(f"START: {item.nodeid}")

def pytest_runtest_teardown(item, nextitem):
    logging.info(f"END: {item.nodeid}")

# This logs every test start/end to test.log.

'''
✅ What to say in interview
“PyTest hooks let me customize how tests are collected, run, and reported.
For example, I’ve used pytest_runtest_setup to add custom logging, 
and plugins like xdist and pytest-html to extend functionality.”
'''
