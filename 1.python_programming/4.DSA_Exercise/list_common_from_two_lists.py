'''
Question 6: Write a Python function that takes two lists and returns a new list containing only the elements
that are common to both lists (no duplicates).
Example:
Input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: [3, 4]
'''

def get_common_items_from_lists(input_list1, input_list2):
    return list(set(input_list1) & set(input_list2))

print(get_common_items_from_lists([1, 2, 3, 4], [3, 4, 5, 6]))