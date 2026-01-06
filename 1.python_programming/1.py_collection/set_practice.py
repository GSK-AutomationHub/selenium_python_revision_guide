myset1 = {1, 3, 5,'india', 'welcome', True}
myset2 = {5, 3,6, 9, 'usa', 'python'}

print(len(myset1))
print(myset1)

for item in myset1:
    print(item,end=" ")

print('item present') if 'python' in myset1 else print('\nitem not present')

print(myset1 | myset2)
print(myset1 & myset2)
print(myset1 - myset2)
print(myset1 ^ myset2)

myset1.add('banana')
print(myset1)
myset2.update(['banana','mango','cherry'])
print(myset2)
myset2.remove('banana')
myset2.discard('kela')