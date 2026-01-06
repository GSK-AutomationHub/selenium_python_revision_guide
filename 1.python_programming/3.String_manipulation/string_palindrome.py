#Question 2:
# Write a Python function that checks whether a given string is a palindrome,
# (reads the same backward as forward). Ignore case and spaces.
'''
"madam" → True
"Race car" → True
"Python" → False
'''

def if_palindrome(input_str):
    input_str = input_str.lower().replace(" ","")
    reverse_string = input_str[::-1]
    if input_str == reverse_string:
        print(f"string '{input_str}' is palindrome")
        return True
    else:
        print(f"string '{input_str}' is not palindrome")
        return False

if_palindrome('Race car')

'''
What’s working well:
 - You're correctly reversing the string using slicing: [::-1] ✔️
 - You're comparing the original with the reversed string ✔️
 - Logic is clean and readable ✔️
'''