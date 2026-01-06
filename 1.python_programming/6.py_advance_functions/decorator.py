'''
What is a decorator?
 - Special function in Python that adds extra functionality to an existing function or method
   without modifying its original code.

Why use decorators?
 - To follow DRY (Don’t Repeat Yourself) principle
 - useful in test automation frameworks for - logging, timing, authentication, retry logic.

How it works:
 - higher-order function → it takes a function as input, wraps it with extra code,
   and returns a new function.

Summary to say in interview:
A decorator is a powerful way in Python to wrap extra functionality around a function or method
without modifying its code. it can be used in test automation for things like logging, timing, retries,
or pre-checks — which makes the framework clean, reusable, and DRY.'''


#Example: A simple decorator that logs before and after a function
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, Boston Scientific!")

say_hello()
# @my_decorator  is just syntactic sugar → equivalent to:
# say_hello = my_decorator(say_hello)
print("------------------------------------------------------------------")

# Practical QA Automation example:
# A decorator used in test framework to automatically log start/end time for every test case:
import time

def log_test_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Running {func.__name__}...")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} finished in {end - start:.2f} seconds")
        return result
    return wrapper

@log_test_time
def test_sample_api():
    time.sleep(1)  # simulate test
    print("API test executed")

test_sample_api()

''' 
This shows:
Using *args and **kwargs to handle any function signature
Logging around the function run
Useful for test frameworks to measure test durations automatically.
'''