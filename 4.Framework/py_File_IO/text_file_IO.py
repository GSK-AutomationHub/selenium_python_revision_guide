'''
✅ Question:
“How would you handle file read/write in Python?”

📌 Core Conceptual Answer (what to say in an interview)
👉 Python provides easy file handling with the built-in open() function.
👉 Best practice is to use a with statement (context manager) to automatically handle closing the file — this prevents file handle leaks.

🗂️ Basic Syntax
Mode	Purpose
'r'	Read (default)
'w'	Write (overwrite)
'a'	Append
'rb'	Read binary
'wb'	Write binary

🧑‍💻 Examples
1️⃣ Reading a file
python
Copy
Edit
# Read entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Read line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
✅ with ensures the file is closed automatically when done.

2️⃣ Writing to a file
python
Copy
Edit
# Write mode ('w') — overwrites existing file
with open('output.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.\n")
3️⃣ Appending to a file
python
Copy
Edit
with open('output.txt', 'a') as file:
    file.write("This line is appended.\n")
📌 Why with is important
✅ Handles closing even if an exception occurs:

python
Copy
Edit
# ✅ Good: automatic cleanup
with open('file.txt', 'r') as f:
    data = f.read()

# ❌ Not ideal: must close manually
f = open('file.txt', 'r')
data = f.read()
f.close()
📌 Practical QA Automation Example
👉 Use file I/O to:

Read test data (CSV, JSON, config files)

Save logs or test reports

Capture API responses for debugging

Example — saving API response to file:

python
Copy
Edit
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

with open('api_response.json', 'w') as f:
    f.write(response.text)
✅ Summary to say in an interview:
“I use Python’s built-in open() with a with statement for safe and clean file handling.
I can read, write, or append text or binary files easily.
This is useful in automation to handle config files, test data, logs, and reports.”


'''