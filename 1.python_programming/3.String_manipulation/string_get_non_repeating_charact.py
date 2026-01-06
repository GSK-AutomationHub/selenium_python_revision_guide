'''
Question 4: Write a Python function that finds the first non-repeating character in a string. Return it.
If all characters repeat, return None.
Example test cases:
"stress" → 't'
"aabbcc" → None
"teeter" → 'r'
'''

def get_non_repeating_character(input_string):
    temp_str = ''
    for i in input_string:
        if not input_string.count(i)>1:
            print(i)
            return i
        else:
            temp_str = temp_str + i
    if temp_str == input_string:
        print(temp_str)
        return None

# get_non_repeating_character('aabbcc')
# get_non_repeating_character('stress')

# Slightly cleaner version (using your style):

def chatgpt_get_non_repeating_character(input_string):
    for i in input_string:
        if input_string.count(i) == 1:
            print(i)
            return i
    return None

# Test cases
chatgpt_get_non_repeating_character('aabbcc')  # None
chatgpt_get_non_repeating_character('stress')  # t
chatgpt_get_non_repeating_character('teeter')  # r

