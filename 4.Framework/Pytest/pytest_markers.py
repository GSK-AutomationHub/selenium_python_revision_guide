'''
| Marker                                       | What it does                  |
| -------------------------------------------- | ----------------------------- |
| `@pytest.mark.skip`                          | Skip this test always         |
| `@pytest.mark.skipif(condition)`             | Skip if condition is true     |
| `@pytest.mark.xfail`                         | Mark test as expected to fail |
| Custom markers (`smoke`, `regression`, etc.) | For grouping                  |

'''

# (A) Simple Generic Example


@pytest.mark.smoke
def test_login():
    assert True

@pytest.mark.skip(reason="Feature under development")
def test_payment():
    assert True

@pytest.mark.xfail(reason="Known bug #123")
def test_profile_update():
    assert False  # This failure is expected

'''
Run only smoke tests: pytest -m smoke
smoke and regression are custom labels.
skip completely skips.
xfail treats failure as “expected”.
'''

#(B) Real Automation Project Example
# Scenario: Mark tests for different test suites in a real UI+API framework.

# 🔑 Fixture: UI driver for smoke UI tests
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# SMOKE UI test
@pytest.mark.smoke
def test_ui_homepage(browser):
    browser.get("https://example.com")
    assert "Example Domain" in browser.title

# REGRESSION API test
@pytest.mark.regression
def test_api_status():
    response = requests.get("https://api.example.com/status")
    assert response.status_code == 200

# CONDITIONAL skip: skip on Windows OS
import sys

@pytest.mark.skipif(sys.platform.startswith("win"), reason="Skip on Windows")
def test_unix_only_feature():
    assert True

# EXPECTED FAILURE: known bug
@pytest.mark.xfail(reason="Known bug: Issue #42")
def test_buggy_feature():
    assert False

'''How to run specific tests:
Command	                            What it does
pytest -m smoke	                    Run only smoke tests
pytest -m regression	            Run only regression tests
pytest -m "smoke or regression" 	Run both
pytest --maxfail=1	                Stop on first failure

#How to register custom markers properly
PyTest recommends registering custom markers in pytest.ini:
# pytest.ini
[pytest]
markers =
    smoke: quick smoke tests
    regression: detailed regression tests
This avoids warnings and improves maintainability.

# What to say in an interview:
“I use PyTest markers to organize tests into suites like smoke and regression. 
I also use skip and xfail to handle unstable or pending features. 
This lets me run subsets easily and integrate cleanly with CI/CD pipelines.”
'''