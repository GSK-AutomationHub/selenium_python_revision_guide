''' *args and **kwargs
 - In Python, *args and **kwargs are special syntaxes used in function definitions to handle variable numbers of arguments:
 - *args	Packs positional arguments into a tuple
 - **kwargs	Packs keyword arguments into a dictionary
 - They make functions flexible when we don’t know in advance how many arguments we’ll get.
'''

# How they work
# *args : Use when you want to accept any number of positional arguments.

def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))  # 6
print(add_numbers(5, 10, 15, 20))  # 50
# Here, args is a tuple: (1, 2, 3).

# **kwargs: Use when you want to accept any number of keyword arguments.

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=30, department="QA")
# Output:
# name: Alice
# age: 30
# department: QA
# Here, kwargs is a dictionary: {'name': 'Alice', 'age': 30, 'department': 'QA'}.

# Combined Example: You can use both in one function (order matters!):

def demo_function(arg1, *args, **kwargs):
    print(f"arg1: {arg1}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

demo_function(1, 2, 3, 4, name="Alice", age=30)
# Output:
# arg1: 1
# args: (2, 3, 4)
# kwargs: {'name': 'Alice', 'age': 30}

print(" ----------------------------------------------------------------------- ")
study_topics = ['physics','chemistry','maths','english','mechatronics']

student_info = {
    'student_name':'Rohit',
    'roll_no':'007',
    'college':'Boston University',
    'interest':'python programming'
}

def university_student_details(*args, **kwargs):
    return {'positional':args,'keyword':kwargs}

sr1 = university_student_details(*study_topics, **student_info )
print(sr1)
print(sr1.get('keyword')['college'])

sr2= university_student_details('maths','physics','english',
                                name='Ricky',roll_no='008',college='Boston University',interest='game application')
print(sr2)
student_subjects = sr2.get('positional')
student_details = sr2.get('keyword')
print(type(student_subjects),student_subjects)
print(type(student_details),student_details)

'''
# When do I use them in practice?
# Common uses:
 - When you write utility or wrapper functions that need to pass arguments flexibly.
 - When building decorators.
 - When creating generic APIs or test utilities
   e.g. utility that accept extra config without changing the function signature.

# Summary to say in an interview:
“*args allows me to pass a variable number of positional arguments as a tuple. 
**kwargs lets me pass a variable number of named arguments as a dictionary. 
Together, they make my functions more flexible and reusable 
— for example, in test utilities, decorators, or dynamic configuration.”
'''