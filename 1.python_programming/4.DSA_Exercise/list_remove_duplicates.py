'''
Problem:Write a Python function that removes duplicates but keeps the original order.
Example:
Input: [1, 2, 2, 3, 1, 4, 3]
Output: [1, 2, 3, 4]
'''

def remove_duplicates_from_list(input_list):
    return list(set(input_list))

#print(remove_duplicates_from_list([1, 2, 2, 3, 1, 4, 3]))
print(remove_duplicates_from_list([1, 2, 5, 10, 15, 25, 15, 10, 12, 12, 11, 10, 2, 3, 1, 4, 3]))

def chatgpt_remove_duplicates_from_list(input_list):
    seen = set()
    result = []
    for num in input_list:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

#print(chatgpt_remove_duplicates_from_list([1, 2, 2, 3, 1, 4, 3]))
print(remove_duplicates_from_list([1, 2, 5, 10, 15, 25, 15, 10, 12, 12, 11, 10, 2, 3, 1, 4, 3]))

def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))

#print(remove_duplicates_from_list([1, 2, 2, 3, 1, 4, 3]))
print(remove_duplicates([1, 2, 5, 10, 15, 25, 15, 10, 12, 12, 11, 10, 2, 3, 1, 4, 3]))