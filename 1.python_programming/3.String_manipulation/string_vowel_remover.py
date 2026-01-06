# Question 1: Write a Python function that takes a string and returns the string with vowels removed.
'''
1️⃣ "Hello World" → Expected: "Hll Wrld"
2️⃣ "Python Automation QA" → Expected: "Pythn tmtn Q"
3️⃣ "Interview Preparation" → Expected: "ntrvw Prprtn"
'''
print(dir('string'))

# my work
def the_vowel_remover(str,expected):
    modified_str = str
    vowel_list = ['a','e','i','o','u','A','E','I','O','U']
    for char in str:
        if char in vowel_list:
            modified_str = modified_str.replace(char, '')
    if modified_str.__eq__(expected):
        print(f"Original_String:{str}\nString_on_Vowel_Removal:{modified_str}")
        return True
    else:
        print(f"original string:{str}, post vowel removal:{modified_str}")
        return False

print(the_vowel_remover("Python Automation QA","Pythn tmtn Q"))

# ✔️ Good points:
# You handled both uppercase and lowercase vowels 👍
# You used replace() inside a loop — correct logic
# You added a check with expected output — good for quick verification
# # Clean print statements for clarity

# chatgpt suggestion
def chatgpt_vowel_remover_1(input_str, expected):
    vowels = 'aeiouAEIOU'
    modified_str = input_str
    for char in input_str:
        if char in vowels:
            modified_str = modified_str.replace(char, '')
    if modified_str == expected:
        print(f"Original_String: {input_str}\nString_on_Vowel_Removal: {modified_str}")
        return True
    else:
        print(f"Original_String: {input_str}\nString_on_Vowel_Removal: {modified_str}")
        return False

# Alternate (More Pythonic) version:
def chatgpt_vowel_remover_2(input_str, expected):
    vowels = 'aeiouAEIOU'
    modified_str = ''.join(char for char in input_str if char not in vowels)
    if modified_str == expected:
        print(f"Original_String: {input_str}\nString_on_Vowel_Removal: {modified_str}")
        return True
    else:
        print(f"Original_String: {input_str}\nString_on_Vowel_Removal: {modified_str}")
        return False


chatgpt_vowel_remover_2('Interview Preparation','ntrvw Prprtn')