'''
| ✅ Concept            | ✅ Generic Example                  | ✅ Real Automation Example       |
| -------------------- | ---------------------------------- | ------------------------------- |
| `setup` / `teardown` | `setup_method` / `teardown_method` | Selenium open/close browser     |
| Fixture              | `@pytest.fixture`                  | API client session              |
| Parametrize          | `@pytest.mark.parametrize`         | API test with multiple payloads |
| Parametrize fixture  | `@pytest.fixture(params=[...])`    | Cross-browser Selenium tests    |

'''

# Example: Parametrize a fixture

import pytest

@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_is_positive(number):
    assert number > 0
# This will run test_is_positive 3 times with number = 1, 2, and 3.

# Real Automation Project Example : Scenario: Run the same UI test on different browsers.

import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")
    yield driver
    driver.quit()

def test_homepage(browser):
    browser.get("https://example.com")
    assert "Example" in browser.title
#Same test runs once in Chrome and once in Firefox — very practical in cross-browser testing.