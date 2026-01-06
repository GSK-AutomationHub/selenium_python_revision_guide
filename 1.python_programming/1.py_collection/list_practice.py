courses = ['science','physics','maths']
print(courses)

print("-------------------- list.remove()  ---------------------- ")
courses.remove('science')
print(courses)

print("-------------------- list.copy()  ---------------------- ")
courses_copy = courses.copy()
print(courses)
print(courses_copy)
print(id(courses) == id(courses_copy))

print("-------------------- list.insert()  ---------------------- ")
courses.insert(0,'chemistry')
print(courses)

print("-------------------- list.append()  ---------------------- ")
courses.append('physics')
print(courses)

print("-------------------- list.count()  ---------------------- ")
print(courses.count('physics'))

print("-------------------- list.index()  ---------------------- ")
print(courses.index('physics'))

print("-------------------- list.append() & list.extend() ---------------------- ")
new_courses = ['music','english', 'drawing']
courses.append(new_courses)
print(courses)
courses.pop()
courses.extend(new_courses)
print(courses)

print("-------------------- list.reverse() ---------------------- ")
print(courses)
courses.reverse()
print(courses)

print("-------------------- list.sort() ---------------------- ")
print(courses)
courses.sort()
print(courses)

print("-------------------- new_list = list(reversed(list)) ---------------------- ")
print(courses)
reversed_courses = reversed(courses)
print(list(reversed_courses))

print("-------------------- new_list = sorted(list)) ---------------------- ")
print(courses)
sorted_courses = sorted(courses,reverse=True)
print(sorted_courses)

print("-------------------- new_list = sorted(list)) ---------------------- ")
print(courses)

