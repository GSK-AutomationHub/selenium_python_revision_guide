import pytest
import allure
from allure_commons.types import AttachmentType

@pytest.fixture(autouse=True, scope="module")
def setup_and_teardown():
    print("launch the browser")
    print("access AUT in the browser")
    yield
    print("logout of application")
    print("quit the browser")

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
