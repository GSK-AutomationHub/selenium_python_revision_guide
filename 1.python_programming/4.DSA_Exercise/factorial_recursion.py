'''
Problem: Write a Python function to calculate the factorial of a given non-negative integer using recursion.
If the input is 0 or 1, return 1.
Example:
Input: 5
Output: 120  # because 5 * 4 * 3 * 2 * 1 = 120
'''

def factorial(n):
    # Base case: 0! and 1! = 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1

def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial_iterative(5))  # Output: 120