''' map() , filter(), sorted()
 - Built-in higher-order functions in Python
 - map() applies a function to each item in an iterable and returns a new iterable of the results.
 - filter() keeps only the items that match a condition (where the function returns True).
 - since they returns iterator — so you usually wrap them with list() if you want a list
'''

#  map() example: square every number in a list:
numbers = [1, 2, 3, 4, 5]
# Using map + lambda
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]
#Equivalent with list comprehension:
squares = [x**2 for x in numbers]

# filter() example: only even numbers from list
numbers = [1, 2, 3, 4, 5, 6]
# Using filter + lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]
# Equivalent with list comprehension:
evens = [x for x in numbers if x % 2 == 0]

# sorted() example: only even numbers from list
from operator import itemgetter
numbers = [(1,'one'),(2,'two'),(3,'three')]
# Using sorted + lambda
sorted_tuple = list(sorted(numbers, key=lambda x:x[1],reverse=True))
sorted_tuple_itemgetter = list(sorted(numbers, key=itemgetter(0)))
print(sorted_tuple)
print(sorted_tuple_itemgetter)

'''
# When to use 
Function	Best for
map()	    When you need to transform every item in a list or other iterable.
filter()	When you need to keep only certain items based on a condition.
'''
# Practical QA Automation Example
# You call an API that returns a list of users and you want to get just the emails of active users:
users = [
    {"name": "Alice", "email": "alice@example.com", "active": True},
    {"name": "Bob", "email": "bob@example.com", "active": False},
    {"name": "Charlie", "email": "charlie@example.com", "active": True}
]

# Filter active users
active_users = filter(lambda u: u['active'], users)

# Map to emails
emails = list(map(lambda u: u['email'], active_users))

print(emails)  # ['alice@example.com', 'charlie@example.com']

a = [10, 20, 4, 6, 7]
b = [10, 20, 4, 60, 70]

def get_common_items_if_lists(list1,list2):
    return (list(set(list1) & set(list2)))

print(get_common_items_if_lists(a,b))

b_square = list(map(lambda x:  x**2,b))
print(b_square)

b_square_filtered = list(filter(lambda x:x>1000,b_square))
print(b_square_filtered)

c = [(4,16),(70,4900),(60,3600),(10,100),(20,400) ]
c_sorted = list(sorted(c, key=lambda c:c[0]))
print(c_sorted)

orders = [101, 102, 103, 104, 102, 105, 101]

result_1 = [ item for item in set(orders) if orders.count(item)>1]
result_2 = list(filter(lambda x: orders.count(x)>1 ,set(orders)))

print(result_1)
print(result_2)

'''Summary to say in an interview:
“
map() can be used to apply a transformation to every element in an iterable, &
filter() to keep only elements that match a condition. They’re very handy for clean, 
functional-style code in data processing or test data preparation.”
'''

