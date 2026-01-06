'''
How do you handle flaky tests in PyTest?
📌 Concept
👉 Flaky tests: Sometimes pass, sometimes fail → often due to:

Unstable environments (network, DB)

Timing/race conditions

External dependencies

✅ Solutions:

Use pytest-rerunfailures

Add waits or retries in fixtures (wisely!)

Fix root cause → flakiness = bad automation design

✅ Generic Example
pytest --reruns 2 --reruns-delay 5
✅ This reruns failed tests 2 times with a 5 second delay.

✅ Real Automation Example
API test with flaky third-party API:
import pytest
import requests

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_external_api():
    response = requests.get("https://unstable-api.com/status")
    assert response.status_code == 200
✅ You can mark an individual flaky test too!

✅ What to say in interview
“I handle flaky tests by fixing root causes first. If unavoidable (like unstable third-party APIs), I use pytest-rerunfailures to rerun failed tests automatically, reducing CI failures.”
'''