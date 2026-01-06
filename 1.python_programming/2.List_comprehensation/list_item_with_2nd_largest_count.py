from  collections import Counter

x = [1,2,1,3,1,3,5,4,5,5,5,5,5,1,6,6,6,6,6,6,6,6,3,3,3,3,3,3,3,3]

# temp_dict = {}
#
# for item in x:
#     temp_dict[item] = x.count(item)

# print(temp_dict)

count = Counter(x)
dict_count = dict(count)
print(dict_count)


y = list(set(dict_count.values()))
y.sort()
y.pop()
z = y[-1]

for item,count in dict_count.items():
    if count == z:
        print(item)
