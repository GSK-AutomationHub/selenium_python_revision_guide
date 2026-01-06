# Using set() (order not guaranteed):

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)  # Order may change: [1, 2, 3, 4, 5]

# Using dict.fromkeys() (preserves order):
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(dict.fromkeys(my_list))
print(unique_list)  # [1, 2, 3, 4, 5]

# Using a loop (preserves order + customizable logic):
my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_list = []
# for item in my_list:
#     if item not in unique_list:
#         unique_list.append(item)
[unique_list.append(item) for item in my_list if item not in unique_list]

print(unique_list)  # [1, 2, 3, 4, 5]


my_string = "BostonScientific"
reversed_string = "".join(reversed(my_string))
print(reversed_string)