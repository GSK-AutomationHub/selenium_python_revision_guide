'''
custom exception : created by defining a new class that inherits from Exception or a subclass of it.
- They make errors more descriptive and domain-specific.
- They make logs and debugging clearer for your team
'''
'''
“I write custom exceptions by creating a new class that inherits from Exception. This helps me make my framework 
clearer and more maintainable — for example, I might raise a TestDataError for invalid test input, 
or an UnsupportedBrowserError if someone tries to run my framework with a browser we don’t support.”
'''
# Define custom exception
class InvalidInputError(Exception):
    """Custom exception for invalid inputs."""
    pass

# Use it
def process_input(data):
    if not isinstance(data, int):
        raise InvalidInputError("Input must be an integer!")

try:
    process_input("abc")
except InvalidInputError as e:
    print(f"Caught custom exception: {e}")

print("--------------------------------------------------------------------")

class UnsupportedBrowserError(Exception):
    pass

browser = "Safari"

try:
    if browser not in ["Chrome", "Firefox"]:
        raise UnsupportedBrowserError(f"{browser} is not supported!")
except UnsupportedBrowserError as e:
    print(e)

print("--------------------------------------------------------------------")

class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.age} -> {self.message}"

try:
    age = -5
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
except InvalidAgeError as e:
    print(e)
else:
    print(f"age entered is - {age}")
finally:
    print("execution completed")