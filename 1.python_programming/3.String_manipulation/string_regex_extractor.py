import string
'''Question 7: Extract all numbers from a string. 
Write a Python function to extract all numbers (integers and decimals) from a given string 
and return them as a list of floats.

Examples:
Input: "The order IDs are 45, 78.9 and 1024."  
Output: [45.0, 78.9, 1024.0]

Input: "No numbers here!"  
Output: []
'''

def extract_regex(input_string):
    str_list = input_string.replace(',','').split()
    return [ float(word) for word in str_list if word[0] in '0 1 2 3 4 5 6 7 8 9'.split() ]

print(extract_regex("The order IDs are 45, 78.9 and 1024"))

print("---------------------------------------------------------------------")

input_string= "The order IDs are 45, 78.9 and 1024."
Output: [45.0, 78.9, 1024.0]

input_string_list = input_string.lower().replace(',','').split()

x = [float(word) for word in input_string_list if word[0] in '0123456789']
print(x)