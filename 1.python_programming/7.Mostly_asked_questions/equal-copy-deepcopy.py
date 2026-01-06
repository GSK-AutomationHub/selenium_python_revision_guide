import copy

print("------------------ scenario-1: Equality --------------")
mylist = [3,6,9,12,15,21]
print(mylist)
mylist_copy = mylist
print(mylist_copy)
print(id(mylist) == id(mylist_copy))
mylist.pop()
mylist.insert(3,24)
mylist[5] = 30
print(mylist_copy)
print(mylist)

print("------------------ scenario-2: shallow copy --------------")
mylist [4] = [1,2,3]
mylist_shallow_copied = mylist.copy()
print(mylist_shallow_copied)
print(mylist)
print(id(mylist) == id(mylist_shallow_copied))
mylist[4][1] = 12
mylist[5] = 21
print(mylist)
print(mylist_shallow_copied)

print("------------------ scenario-3: deep copy --------------")

mylist [4] = [12,14,15]
mylist_deep_copied = copy.deepcopy(mylist)
print(mylist)
print(mylist_deep_copied)
print(id(mylist) == id(mylist_deep_copied))
mylist[4][1] = 64
mylist[5] = 71
print(mylist)
print(mylist_deep_copied)