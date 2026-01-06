'''
Question 3: Write a Python function that counts how many times each word appears in a sentence.
Return the result as a dictionary. Ignore punctuation and case.

Example:
Input: "Hello hello world! This is a hello world example."
Output: {'hello': 3, 'world': 2, 'this': 1, 'is': 1, 'a': 1, 'example': 1}

Hints:
Convert to lowercase --> Remove punctuation (!, ., , etc.) -->
Split by spaces --> Count words into a dictionary
'''
import string
from fnmatch import translate


def word_counter(input_string):
    result = {}

    # string converted into lowercase
    input_string = input_string.lower()
    # deletes all punctuation & create a translation table
    cleaned_input_string = input_string.translate(input_string.maketrans('','',string.punctuation))

    # split into words
    word_list = cleaned_input_string.split()
    # create unique word set
    unique_word_set = set(word_list)

    # iterate through set & list to create result dict
    for word in unique_word_set:
        result[word] = word_list.count(word)
    return result

result = word_counter("Hello hello world! This is a hello world example.")
#print(result)



def chatgpt_word_counter(input_string):
    # 1. Lowercase
    input_string = input_string.lower()
    # 2. Remove punctuation
    # str.maketrans('', '', string.punctuation): deletes all punctuation & create a translation table
    #.translate(): uses this table to process the string.
    input_string = input_string.translate(str.maketrans('', '', string.punctuation))
    # 3. Split into words
    words = input_string.split()
    # 4. Count words
    result = {}
    unique_words = set(words)
    for word in unique_words:
        result[word] = words.count(word)
    return result

# result = word_counter("Hello hello world! This is a hello world example.")
# print(result)

from collections import Counter

def word_counter_3(input_string):
    input_string = input_string.lower()
    input_string = input_string.translate(str.maketrans('', '', string.punctuation))
    count = Counter(input_string.split())
    count_dict = dict(count)
    print(count_dict)

word_counter_3("Hello hello world! This is a hello world example.")