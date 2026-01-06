'''
Exception handling in Python:
 - Python uses try, except, else, and finally blocks to catch and manage errors gracefully.
 - This ensures program doesn’t crash unexpectedly and can handle failures properly

try:
    # Wrap risky code that may raise an exception
except SomeException as e:
    # Handle specific exceptions — best practice is to catch specific ones, not generic
else:
    # Runs only if no exception.
finally:
    # Runs no matter what (cleanup, closing resources)
    # Always runs — good for cleanup like closing files or database connections.
'''

def error_handling(num):
    try:
        result = 10 / num
    except ValueError:
        print("Invalid input! Please enter an integer.")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution complete.")

error_handling(2)

print("---------------------------------------------------------------------------")
try:
    x = {'roll_no':[1, 2, 3, 4], 'school':'abc school'}
    print(type(x))
    if len(x) != 3:
        raise ValueError("Invalid dict length")
except NameError:
    print('this is name error')
except ZeroDivisionError:
    print('zero division error')
except TypeError:
    print('Type Error')
except ValueError as e:
    print('Exception got handled - ',e)
else:
    print('tyr block executed successfully')
finally:
    print('try except test completed')

print("---------------------------------------------------------------------------")

class InvalidAgeError(Exception):
    pass

age = -5

try:
    if age < 0:
        raise InvalidAgeError("Age cannot be negative!")
except InvalidAgeError as e:
    print(e)

print("---------------------------------------------------------------------------")

from selenium.common.exceptions import NoSuchElementException

try:
    element = driver.find_element_by_id("username")
    element.send_keys("admin")
except NoSuchElementException:
    print("Element not found, taking screenshot...")
    driver.save_screenshot("error.png")
finally:
    driver.quit()


