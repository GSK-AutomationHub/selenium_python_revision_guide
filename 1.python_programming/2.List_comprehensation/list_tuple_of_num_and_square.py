'''
Question 5
Write a Python list comprehension that returns a list of tuples where each tuple contains a number and its square,
but only for odd numbers in the given list.
Example:
Input: [1, 2, 3, 4, 5]
Output: [(1, 1), (3, 9), (5, 25)]
'''

def get_tuple_of_num_and_square(input_list):
    return [(num,num**2) for num in input_list if num%2!=0]

print(get_tuple_of_num_and_square([1, 2, 3, 4, 5]))