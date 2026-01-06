
arr = [{"metal","rock"},{"beetal","hard"},{"metallic","rockhard"},{"silver","poptop"}]
temp_arr = []
for item in arr:
    temp_arr.append(tuple(item))

print(temp_arr)

x = [tuples[1] for tuples in temp_arr for item in tuples if item.startswith('metal')]
print(x)

# for tuples in temp_arr:
#     for item in tuples:
#         if item.startswith('metal'):
#             print(tuples[1])