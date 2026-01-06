''' What is the difference between is and == in Python?
=> '==' compares values (i.e., content).
=> 'is' compares identities (i.e., whether both point to the same object in memory).
'''
#Example:

a = [1, 2, 3]
b = [1, 2, 3]
c = b

print(a == b)  # True (content is same)
print(a is b)  # False (different memory locations)
print(c is b)  # True (same memory locations)

'''In Automation Context: We mostly use '==' & 'is' for following purpose
=> '==' to validate values from UI or API.
=> 'is' is used when identity matters However, 
   - in unit tests or memory-sensitive automation modules
   - like singleton implementations or config objects.
'''
print("------------------------------------------------------- ")
p=[3,6,9,12]
q=[3,6,9,12]
print(p == q)
print(p is q)
print(id(p), id(q))

s=t=[3,6,9,12,15]
print(s == t)
print(s is t)
print(id(s), id(t))