'''
Question 4: Write a Python function that takes a list of tuples (name, age) and returns a new list sorted by:

1️⃣ Age in ascending order
2️⃣ If two people have the same age, sort them alphabetically by name
Example:
Input: [('John', 25), ('Alice', 22), ('Bob', 25), ('Diana', 20)]
Output: [('Diana', 20), ('Alice', 22), ('Bob', 25), ('John', 25)]
'''
from operator import itemgetter

def sort_key(x):
    return (x[1], x[0])

def sort_people_by_age_and_name(input_list):
    # Sort by age (x[1]), then by name (x[0]) if ages are same
    print(sorted(input_list, key=lambda x: (x[1], x[0])))
    print(sorted(input_list, key=itemgetter(1, 0)))
    print(sorted(input_list, key=sort_key))
    input_list.sort(key=itemgetter(1, 0))
    print(input_list)

people = [('John', 25), ('Alice', 22), ('Bob', 25), ('Diana', 20)]
print(sort_people_by_age_and_name(people))

'''
Explanation
sorted() returns a new sorted list.
key=lambda x: (x[1], x[0]) means:
 - Primary sort: x[1] → the age.
 - Secondary sort: x[0] → the name, if ages are equal.
This pattern (x[1], x[0]) is a tuple key, which Python sorts left-to-right
'''







