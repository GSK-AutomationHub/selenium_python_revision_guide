'''
problem: Write a Python function to find the first non-repeating character in a string.
Return None if all characters repeat.
Example:
Input: "stress" , "aabbcc"
Output: 't',  None
'''

def get_non_repeating_char_in_string(input_string):
    input_string = input_string.replace(' ','').lower()
    for char in input_string:
        if input_string.count(char) == 1:
            return char
    return None

print(get_non_repeating_char_in_string("stress"))
print(get_non_repeating_char_in_string("aabbcc"))

from collections import Counter
def get_non_repeating_char_in_string_counter(input_string):
    input_string = input_string.replace(' ', '').lower()
    counts = Counter(input_string)
    for char in input_string:
        if counts[char] == 1:
            return char
    return None

print(get_non_repeating_char_in_string_counter("stress"))  # t
print(get_non_repeating_char_in_string_counter("aabbcc"))  # None
