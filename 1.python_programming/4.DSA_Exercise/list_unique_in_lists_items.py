'''
Problem: Write a Python function that returns the elements that are unique to each list
(i.e. items that are in one list OR the other but NOT both).
Example:
Input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: [1, 2, 5, 6]
'''

def get_unique_items_from_lists(input_list1, input_list2):
    print(list(set(input_list1) ^ set(input_list2)))

get_unique_items_from_lists([1, 2, 3, 4], [3, 4, 5, 6])