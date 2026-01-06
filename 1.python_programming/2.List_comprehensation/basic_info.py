''' list comprehension
- Concise way to create a new list, optionally filtering items with a condition
- Compact & readable, simple & faster
- used to write cleaner, more Pythonic code
- syntax [expression for item in iterable if condition]
'''

# Simple: Squares of numbers
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

#With a condition: Even numbers only
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4, 6]

#Equivalent using for-loop
# Same as:
evens = []
for x in numbers:
    if x % 2 == 0:
        evens.append(x)

# Practical QA Automation Example
users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": True}
]

# Get names of active users
active_users = [user_record['name'] for user_record in users if user_record['active']]
active_users_sorted = sorted(active_users,key=lambda x:x,reverse=True)
print(active_users_sorted)
print(active_users)  # ['Alice', 'Charlie']
