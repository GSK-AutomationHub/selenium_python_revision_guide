from copy import deepcopy
from operator import indexOf

my_list = ['India', 'test match', 'ahmadabad', 'test case', 'mumbai', 'test scenario']

result = [word for word in my_list if word.startswith('test')]
print(result)


numbers = [1, 2, 3, 4, 5, 6]
transformed_list = ["Even" if num % 2 == 0 else "Odd" for num in
                    numbers]  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']
print(transformed_list)


my_list = ["a", "b", "a", "c", "b", "a"]
# Option 1: Using list comprehension with count() (less efficient for many items)
counts = [(x, my_list.count(x)) for x in sorted(set(my_list))]  # Output: [('a', 3), ('b', 2), ('c', 1)]
print(dict(counts))

# Option 2: Using collections.Counter (generally preferred)
from collections import Counter
counts = Counter(my_list)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})
print(dict(counts))

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
combinations = [(x, y) for x in list1 for y in
                list2]  # Output: [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]

numbers = range(20)
filtered_numbers = [x for x in numbers if x % 2 == 0 if x > 5]  # Output: [6, 8, 10, 12, 14, 16, 18]


print("---------------------------- removing duplicate from list ---------------------------------------")
my_list = [1,2,3,4,4,5,5,6,6,7,7,3,3,2]

unique_list = list(set(my_list))
print(unique_list)

print(list(dict.fromkeys(my_list)))

temp_list=[]
x = [temp_list.append(item) for item in my_list if item not in temp_list]
print(temp_list)

print("---------------------------- reversed string ---------------------------------------")

test_string = 'capgemini engineering'

reversed_str_1 = test_string[::-1]
print(reversed_str_1)

reversed_str_2 = ''
for char in test_string:
    reversed_str_2 = char + reversed_str_2
print(reversed_str_2)

reversed_str_3 = "".join(reversed(test_string))
print(reversed_str_3)

print("---------------------------- list comprehenstion 2nd large no ---------------------------------------")

x = [1,2,1,3,1,3,5,4,5,5,5,5,5,1,6,6,6,6,6,6,6,6,3,3,3,3,3,3,3,3]

y = [item for item in list(set(x)) if item != max(x)]
print(max(y))

print("---------------------------- list item with 2nd large count ---------------------------------------")

x = [1,2,1,3,1,3,5,4,5,5,5,5,5,1,6,6,6,6,6,6,6,6,3,3,3,3,3,3,3,3]

temp_dict = {}

for item in x:
    temp_dict[item] = x.count(item)

print(temp_dict)
temp_dict_values = list(temp_dict.values())
temp_dict_values.sort()
temp_dict_values.pop()
second_large_count = temp_dict_values[-1]
print(second_large_count)
for k,v in temp_dict.items():
    if v == second_large_count:
        print(k)

print("---------------------------- list comprehenstion to omit word less than 3 charac ---------------------------------------")
sample_string = "Python list comprehension is powerful and concise"

word_list = sample_string.split()
print(word_list)
result = [ word for word in word_list if len(word)>3]
print(result)

print("---------------------------- list comprehenstion nested list ---------------------------------------")
sample_list =  [[1, 2], [3, 4], [5, 6]]
#Output: [1, 2, 3, 4, 5, 6]

result = [item for nested_list in sample_list for item in nested_list]
print(result)

print("---------------------------- list comprehenstion nested list ---------------------------------------")
list_of_set = [{"metal","rock"},{"beetal","hard"},{"metallic","rockhard"},{"silver","poptop"}]

testing_list = [ tuple(item) for item in list_of_set]
print(testing_list)
result_list = [tuple[0] if indexOf(tuple,item) ==1 else tuple[1] for tuple in testing_list for item in tuple if item.startswith('metal')]
print(result_list)