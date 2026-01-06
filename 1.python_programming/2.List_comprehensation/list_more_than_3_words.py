'''
Write a Python list comprehension that extracts all words from a given sentence that have more than 3 letters.
Example:
Input: "Python list comprehension is powerful and concise"
Output: ['Python', 'list', 'comprehension', 'powerful', 'concise']
'''

def get_wod_with_more_than_3_words(input_string):
    word_list = input_string.split()
    temp_list = []
    print(word_list)
    for word in word_list:
        if len(word)>3:
            temp_list.append(word)
    print(temp_list)
    return [word for word in word_list if len(word) > 3]


result = get_wod_with_more_than_3_words("Python list comprehension is powerful and concise")
print(result)