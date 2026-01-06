'''
Problem: Write a Python function to return all duplicate numbers in a list.
Example:
Input: [1, 2, 3, 2, 4, 3, 5, 1]
Output: [1, 2, 3]
'''
from collections import Counter

def get_duplicate_list_items_1(input_list):
    duplicate_num_list = []
    unique_num_set = set(input_list)
    for num in unique_num_set:
        if input_list.count(num)>1:
            duplicate_num_list.append(num)
    return duplicate_num_list

print(get_duplicate_list_items_1([1, 2, 3, 2, 4, 3, 5, 1]))

def get_duplicate_list_items_2(input_list):
    return [num for num in set(input_list) if input_list.count(num)>1]

print(get_duplicate_list_items_2([1, 2, 3, 2, 4, 3, 5, 1]))

def get_duplicate_list_items_3(input_list):
    counts = Counter(input_list)
    #print(type(counts),counts)
    return [num for num, count in counts.items() if count > 1]

print(get_duplicate_list_items_3([1, 2, 3, 2, 4, 3, 5, 1]))