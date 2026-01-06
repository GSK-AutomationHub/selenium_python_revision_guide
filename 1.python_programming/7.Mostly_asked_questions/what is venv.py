'''
✅ Question:
“How do you use virtual environments in Python projects?”

📌 Core Conceptual Answer (what to say in an interview)
👉 A virtual environment is an isolated Python workspace:

It has its own Python interpreter and its own installed packages, separate from the system Python or other projects.

This prevents dependency conflicts and makes projects portable and reproducible.

✅ So, each project can have exactly the dependencies it needs — no clashes!

🗂️ How to create and use one
1️⃣ Create a virtual environment
bash
Copy
Edit
# On Linux/Mac
python3 -m venv venv_name

# On Windows
python -m venv venv_name
✅ Common convention: name it venv or .venv.

2️⃣ Activate it
bash
Copy
Edit
# Linux/Mac
source venv_name/bin/activate

# Windows (cmd)
venv_name\Scripts\activate

# Windows (PowerShell)
venv_name\Scripts\Activate.ps1
3️⃣ Install packages

Once activated, use pip as usual — it installs to the virtual environment only, not globally:
pip install requests pytest selenium

4️⃣ Deactivate when done
deactivate
🧩 Typical workflow in a QA automation project

# 1️⃣ Create env
python -m venv venv

# 2️⃣ Activate
source venv/bin/activate  # Linux/Mac
# OR venv\Scripts\activate  # Windows

# 3️⃣ Install test libraries
pip install pytest requests selenium behave

# 4️⃣ Save requirements
pip freeze > requirements.txt

# 5️⃣ Later, recreate the same env elsewhere:
# python -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt
✅ Why it’s useful
Benefits	Examples
Isolates dependencies	Different projects can use different versions of the same library
Easier deployment	requirements.txt locks exact versions
Prevents conflicts	No more “it works on my machine”
Cleaner	No need for sudo pip install globally

✅ Summary to say in an interview:
“I always use virtual environments to isolate my project dependencies. I create one with python -m venv, activate it, install required packages locally, and freeze dependencies in requirements.txt. This keeps my automation framework portable and conflict-free.”

✅ Bonus tip for real projects
👉 Many teams use venv, but tools like pipenv or poetry offer extra features for managing virtual environments + dependencies together — worth exploring!
'''