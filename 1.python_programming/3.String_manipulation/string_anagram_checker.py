''' Question 6: Anagram Checker
Write a Python function to check if two strings are anagrams of each other. Ignore spaces and case sensitivity.
Examples:
 - "listen" and "silent" → ✅ True
 - "Dormitory" and "dirty room" → ✅ True
 - "hello" and "world" → ❌ False
Hints:
 - Remove spaces.
 - Convert to lowercase.
 - Sort both strings and compare.
'''

def chatgpt_string_anagram_checker(input_string_1, input_string_2):
    # Remove spaces and lowercase
    s1 = input_string_1.replace(" ", "").lower()
    s2 = input_string_2.replace(" ", "").lower()

    # Sort letters
    if sorted(s1) == sorted(s2):
        print(f"strings '{input_string_1}' and '{input_string_2}' are anagrams")
        print(sorted(s1), sorted(s2))
        return True
    else:
        print(f"strings '{input_string_1}' and '{input_string_2}' are not anagrams")
        print(sorted(s1), sorted(s2))
        return False

chatgpt_string_anagram_checker('listen','silent')
chatgpt_string_anagram_checker('hello','world')