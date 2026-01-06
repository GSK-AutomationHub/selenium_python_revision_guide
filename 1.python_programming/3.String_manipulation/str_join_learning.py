
# vowel_list = ['a','e','i','o','u','A','E','I','O','U']
# vowels = ''.join(vowel_list)
# print(type(vowels),vowels)
input_str = 'interview Preparation'
modified_str = ''.join(char for char in input_str if char not in 'aeiouAEIOU')
print(input_str)
print(modified_str)
