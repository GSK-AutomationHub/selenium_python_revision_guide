'''
 Question 3: Write a Python list comprehension that flattens a 2D list (list of lists) into a single 1D list.
Example:
Input: [[1, 2], [3, 4], [5, 6]]
Output: [1, 2, 3, 4, 5, 6]
'''

def get_1D_list_from_2D(input_list):
    output_list = []
    for item in input_list:
        output_list.extend(item)
    print(output_list)
    # [element for sublist in list_of_lists for element in sublist]
    return [item for nested_list in input_list for item in nested_list]

result = get_1D_list_from_2D([[1, 2], [3, 4], [5, 6]])
print(result)