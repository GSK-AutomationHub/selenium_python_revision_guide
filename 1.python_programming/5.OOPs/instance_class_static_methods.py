'''
| Aspect                              | **Instance Method**             | **Class Method**                                      | **Static Method**                                  |
| ----------------------------------- | ------------------------------- | ----------------------------------------------------- | -------------------------------------------------- |
| **Decorator**                       | *None* (default)                | `@classmethod`                                        | `@staticmethod`                                    |
| **First parameter**                 | `self` (instance)               | `cls` (class)                                         | No default first parameter                         |
| **Can access instance attributes?** | ✅ Yes                           | ❌ No                                                  | ❌ No                                               |
| **Can access class attributes?**    | ✅ Yes                           | ✅ Yes                                                 | ❌ No                                               |
| **Typical use**                     | Operate on object-specific data | Operate on class-level data; alternative constructors | Utility/helper function logically grouped in class |
'''

class MyExample:
    class_name = "MyExampleClass"

    def __init__(self, value):
        self.value = value  # instance attribute

    # Instance Method
    def show_value(self):
        print(f"Instance Method: value = {self.value}")

    # Class Method
    @classmethod
    def show_class_name(cls):
        print(f"Class Method: class_name = {cls.class_name}")

    # Static Method
    @staticmethod
    def add(x, y):
        print(f"Static Method: sum = {x + y}")

# Example usage:
obj = MyExample(24)

# ✅ Instance method → uses `self`
obj.show_value()
# Output: Instance Method: value = 24

# ✅ Class method → uses `cls`
MyExample.show_class_name()
# Output: Class Method: class_name = MyExampleClass

# ✅ Static method → uses neither `self` nor `cls`
MyExample.add(10, 5)
# Output: Static Method: sum = 15
'''
| Method Type         | Example Use in QA                           | Why                                                                  |
| ------------------- | ------------------------------------------- | -------------------------------------------------------------------- |
| **Instance Method** | Execute steps for a specific test case      | Needs access to instance-level data, like test data or config.       |
| **Class Method**    | Create test objects with preset configs     | Needs to return an instance or change a class setting for all tests. |
| **Static Method**   | Utility: format test data, calculate values | No access to object/class needed — just a helper function.           |
'''

