
class Webdrivermanager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            print("initialize browser instance")
            #from selenium import webdriver
            #options = webdriver.ChromeOptions()
            #options.add_argument("--headless")
            #cls._instance = webdriver.Chrome(options=options)
        return cls._instance

driver = Webdrivermanager()
driver.get("https://www.flipkart.com")

print('---------------------------------------------------------------------------------------')

class Singleton:
    _instance = None  # Class-level private variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Optional: Initialize instance attributes here if needed
            # cls._instance.value = "Initial Value"
        return cls._instance

    def __init__(self, value=None):
        # __init__ is called every time an instance is "created"
        # but the actual object is only created once by __new__
        if not hasattr(self, 'initialized'): # Prevent re-initialization on subsequent calls
            self.value = value
            self.initialized = True

# Creating instances
s1 = Singleton("First Instance")
s2 = Singleton("Second Instance") # This will return the same instance as s1

print(s1 is s2)  # Output: True (confirms they are the same object)
print(s1.value)  # Output: First Instance
print(s2.value)  # Output: First Instance (value was set by the first creation)

# Demonstrating state sharing
s1.value = "Updated Value"
print(s2.value) # Output: Updated Value