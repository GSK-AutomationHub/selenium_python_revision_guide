'''
List Comprehension — Question 1
Write a Python list comprehension that takes a list of numbers and returns a new list with only the even numbers squared.
Input: [1, 2, 3, 4, 5, 6]
Output: [4, 16, 36]
'''

def get_even_number_square(input_list):
    output_list = []
    for num in input_list:
        if num%2 == 0:
            output_list.append(num**2)
    return output_list

print(get_even_number_square([1, 2, 3, 4, 5, 6]))

def chatgpt_even_num_square(input_list):
    return [num**2 for num in input_list if num%2==0]
    # [<expression> for <item> in <iterable> if <condition>]

print(chatgpt_even_num_square([1, 2, 3, 4, 5, 6]))