'''
✅ Question:
“What is __init__.py and why is it used?”

📌 Core Conceptual Answer (what to say in an interview)
👉 In Python, __init__.py is a special file used to mark a directory as a Python package.

✅ Without __init__.py, Python won’t treat the folder as a package — so you can’t reliably import modules from it.

✅ It also controls what gets imported when you use import package_name or from package_name import *.

🗂️ How it works
Example directory structure:

css
Copy
Edit
my_project/
 ├── my_package/
 │    ├── __init__.py
 │    ├── module1.py
 │    ├── module2.py
 ├── main.py
✅ __init__.py makes my_package a package.
Now you can do:

python
Copy
Edit
from my_package import module1
or:

python
Copy
Edit
import my_package.module2
📌 What goes inside __init__.py
✅ It can be:

Empty → just to declare it’s a package.

Or contain initialization code, such as:

Importing frequently used functions/classes for convenience.

Setting up package-level variables.

Running package-specific setup.

Example:

python
Copy
Edit
# __init__.py
from .module1 import important_function

print("my_package is initialized!")
📌 Why it’s useful in real projects
✅ __init__.py helps:

Organize your framework into logical modules & packages.

Control what’s exposed as the package API.

Make your test framework or utility libraries reusable and importable.

✅ Summary to say in an interview:
“__init__.py marks a directory as a Python package so its modules can be imported. It can be empty or include initialization code and shortcuts for package-wide imports. It helps structure large projects or frameworks clearly.”


'''