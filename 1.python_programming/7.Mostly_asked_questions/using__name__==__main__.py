'''
✅ Question:
“What is __name__ == "__main__" for?”

📌 Core Conceptual Answer (what to say in an interview)
👉 In Python, every .py file is a module.
👉 When you run a script directly, Python sets a special built-in variable __name__ to "__main__".
👉 When you import that file as a module, __name__ is set to the module’s name instead.

✅ So:
if __name__ == "__main__": lets you control which code runs only when the script is run directly, not when it’s imported elsewhere.

🧑‍💻 Simple Example
python
Copy
Edit
# my_module.py

def add(a, b):
    return a + b

if __name__ == "__main__":
    # This runs only if you run `python my_module.py`
    print(add(2, 3))
✅ When run directly:

lua
Copy
Edit
python my_module.py  --> Output: 5
✅ When imported:

python
Copy
Edit
# another_script.py
import my_module

print(my_module.add(4, 5))  # 9

# BUT my_module's print(add(2, 3)) does NOT run
📌 Why it’s important
✅ This pattern is very common for:

Running unit tests inside the same file.

Adding example usage or debug code.

Keeping reusable functions or classes separate from runtime code.

✅ Summary to say in an interview:
“__name__ == "__main__" checks whether a script is being run directly or imported as a module. It lets me write reusable modules and also include test/demo code that runs only when executing the script directly.”

🎓 In QA Automation
Use it to allow running a test file standalone for debugging.

Keep framework code importable without executing test runs automatically on import.


'''