''' lambda
 - an anonymous function in Python.
 - It’s defined with the lambda keyword instead of def.
 - can take any number of arguments but evaluate only one expression (no statements, loops, or complex blocks).
 - syntax:- variable = lambda arguments: expression
 - * lambda used as an argument to higher-order functions like map(), filter(), or sorted().
'''
'''
* lambda used as an argument to higher-order functions like map(), filter(), or sorted().
* lambda can help when sorting test data, filtering logs, or writing quick expressions in config scripts.
 e.g., quickly sorting API response by a nested field in a data-driven test.
'''

# simple example
# Normal function
def add(x, y):
    return x + y

# Lambda equivalent
add_lambda = lambda x, y: x + y

print(add(2, 3))        # 5
print(add_lambda(2, 3)) # 5

################# Practical Examples #################
numbers = [1, 2, 3, 4, 5, 6]

#With map()
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25, 36]

# With filter()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]

# With sorted() and key
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
# Sort by the second element
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # [(1, 'one'), (3, 'three'), (2, 'two')]
