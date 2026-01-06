'''
 Problem: Write a Python function that takes a list of integers and returns
 the maximum and minimum numbers as a tuple (max, min).
Example:
Input: [2, 5, 1, 8, 3]
Output: (8, 1)
'''

def max_min_from_list(input_list):
    return (max(input_list),min(input_list))

print(max_min_from_list([2, 5, 1, 8, 3]))


def max_min_from_list_DSA(input_list):
    max_num = min_num = input_list[0]

    for num in input_list[1:]:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return (max_num, min_num)

print(max_min_from_list_DSA([2, 5, 1, 8, 3]))