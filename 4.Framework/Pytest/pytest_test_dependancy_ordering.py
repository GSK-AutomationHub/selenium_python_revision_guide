''' How do you handle test dependencies and ordering in PyTest?
✅ PyTest encourages independent tests
    - each test should stand alone so that order doesn’t matter.

✅ But if setup flow where one test’s result is reused & need to run tests in a specific order:
   - Use pytest-order plugin for explicit ordering.
   - Use fixtures or shared setup instead of chaining tests.
   - Avoid true test dependencies — use smart design.

# (A) Simple Generic Example
# Install pytest-order: pip install pytest-order
'''
# Example — run in a specific order:
import pytest

@pytest.mark.order(1)
def test_login():
    print("Login")

@pytest.mark.order(2)
def test_add_item():
    print("Add item")

@pytest.mark.order(3)
def test_checkout():
    print("Checkout")

# This runs: 1️⃣ test_login → 2️⃣ test_add_item → 3️⃣ test_checkout

# (B) Real Automation Project Example : Scenario: UI checkout flow:
# 1️⃣ test_login → 2️⃣ test_add_item → 3️⃣ test_checkout
# This needs to be tested in flow OR you use a session fixture so each step can be independent too.

# Example with pytest-order:
import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("driver")
class TestEcommerceFlow:

    @pytest.mark.order(1)
    def test_login(self):
        self.driver.get("https://example.com/login")
        # Do login actions here
        assert "Login" in self.driver.title

    @pytest.mark.order(2)
    def test_add_to_cart(self):
        # Assume already logged in
        self.driver.get("https://example.com/product/123")
        # Click Add to Cart
        assert "Product" in self.driver.title

    @pytest.mark.order(3)
    def test_checkout(self):
        # Go to checkout
        self.driver.get("https://example.com/checkout")
        assert "Checkout" in self.driver.title

''' 
# Key points: 
 - Use @pytest.mark.order to enforce order.
 - Use class-scoped driver so same session flows through steps.
# Practical Alternative:
 - Better practice: Use fixtures to log in or add product as setup 
 — then each test can run independently in any order!
'''

@pytest.fixture
def logged_in_driver():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")
    # login steps
    yield driver
    driver.quit()

def test_add_to_cart(logged_in_driver):
    logged_in_driver.get("https://example.com/product/123")
    assert "Product" in logged_in_driver.title

def test_checkout(logged_in_driver):
    logged_in_driver.get("https://example.com/checkout")
    assert "Checkout" in logged_in_driver.title

# This is cleaner and CI-friendly.

''' What to say in an interview:
“In PyTest, I prefer designing tests to be independent. 
But when ordering is needed, I use the pytest-order plugin to set explicit priorities.
For flows like login → add → checkout, I often use fixtures to handle preconditions 
so tests stay robust and can run in any order.”
'''