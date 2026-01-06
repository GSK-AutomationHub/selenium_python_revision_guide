import string

''' Question 5: Write a Python function to replace all occurrences of a given word in a string with a new word.
Make it case-insensitive (e.g., replace “hello” and “Hello” both).

Example:
Input: "Hello world, hello Python world", old_word="hello", new_word="hi"
Output: "hi world, hi Python world"

Hints:
Convert string to lowercase temporarily OR
use re.sub() for case-insensitive replace.
Return the updated string.
'''


def replace_substring(input_string,old_word,new_word):
    word_list = input_string.lower().split()
    for index,word in enumerate(word_list):
        if word == old_word:
            word_list[index]=new_word
    new_string = ' '.join(word_list)
    print(new_string)

replace_substring("Hello world, hello Python world","hello","hi")
