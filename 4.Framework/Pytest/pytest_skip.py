'''
How do you skip or conditionally skip tests in PyTest?
 - Skip a test unconditionally (@pytest.mark.skip)
 - Skip it conditionally (@pytest.mark.skipif(<condition>, reason="..."))

✅ Useful for:
 - OS-specific tests
 - Feature not ready
 - Known limitations
 '''

#Generic Example

import pytest
import sys

@pytest.mark.skip(reason="Feature under development")
def test_payment():
    assert True

@pytest.mark.skipif(sys.platform.startswith("win"), reason="Skip on Windows")
def test_unix_feature():
    assert True

# Real Automation Example

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.skip(reason="Login page redesign in progress")
def test_login(browser):
    browser.get("https://example.com/login")
    assert "Login" in browser.title

@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requires Python 3.10+")
def test_api_new_feature():
    # API test for new feature that works only in latest version
    assert True

''' What to say in interview
I use @skip for tests that shouldn’t run for now, and 
@skipif for conditional cases like OS or Python version dependencies. 
This helps avoid false failures.
'''