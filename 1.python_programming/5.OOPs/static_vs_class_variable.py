'''
In Python: Static variable = Class variable.

In Python, “static variable” and “class variable” mean the same thing
— a variable shared by all instances, defined at the class level.

| Term                | Meaning                               | Python usage                 |
| ------------------- | ------------------------------------- | ---------------------------- |
| **Class variable**  | Shared across all instances           | ✔️ Official term             |
| **Static variable** | Informal term, same meaning in Python | ✔️ Common in other languages |

'''

class MyExample:
    class_variable = "I am a class variable"  # same as a static variable

    def __init__(self, value):
        self.instance_variable = value  # unique to each object

obj1 = MyExample(10)
obj2 = MyExample(20)

print(MyExample.class_variable)   # ✅ same for everyone
print(obj1.class_variable)        # ✅ same
print(obj2.class_variable)        # ✅ same

obj1.class_variable = "Changed by obj1"  # creates a new instance attribute for obj1 only!
print(obj1.class_variable)  # "Changed by obj1"
print(obj2.class_variable)  # still "I am a class variable"
print(MyExample.class_variable)  # still "I am a class variable"








'''
|                            | **Instance variable**            | **Class variable (aka static variable)**      |
| -------------------------- | -------------------------------- | --------------------------------------------- |
| **Defined in**             | `__init__` (or instance methods) | Directly inside the class, outside any method |
| **Belongs to**             | Each object                      | The class                                     |
| **Shared by all objects?** | ❌ No                             | ✅ Yes                                         |
| **Typical use**            | Object-specific data             | Common settings, constants                    |

'''