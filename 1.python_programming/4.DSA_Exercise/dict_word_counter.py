'''
Question 5 : Write a Python function that counts how many times each word appears in a given string
and returns a dictionary.
Example:
Input: "hello world hello python world"
Output: {'hello': 2, 'world': 2, 'python': 1}
'''

def word_counter_func(input_string):
    word_counter = {}
    word_list = input_string.lower().split()
    unique_word_set = set(word_list)
    for word in unique_word_set:
        word_counter[word] = word_list.count(word)
    print(word_counter)

word_counter_func("hello world hello python world")

from collections import Counter

def chatgpt_word_counter_func(input_string):
    word_list = input_string.lower().split()
    word_counter = Counter(word_list)
    print(word_counter, dict(word_counter))

chatgpt_word_counter_func("hello world hello python world")


