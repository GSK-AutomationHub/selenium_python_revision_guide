'''
Question 4: Write a Python list comprehension that takes a list of words and returns a new list containing
only the words that start with a vowel (a, e, i, o, u), converted to uppercase.
 Example:
Input: ['apple', 'banana', 'orange', 'umbrella', 'cat', 'owl']
Output: ['APPLE', 'ORANGE', 'UMBRELLA', 'OWL']
'''
def get_word_starting_with_vowel(input_list):
    #return [word.upper() for word in input_list if word[0] in ('a', 'e', 'i', 'o', 'u')]
    return [word.upper() for word in input_list if word[0].lower()  in 'aeiou']

print(get_word_starting_with_vowel(['apple', 'banana', 'orange', 'umbrella', 'cat', 'owl']))