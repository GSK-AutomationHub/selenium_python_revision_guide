
message = 'hello world'

print("------------ format string with .format() ------------------- ")
name = 'Pratap'
greeting = 'hello'
language = 'python'
greeting_message = "{}, {}. Welcome to world of {}!".format(greeting,name,language)
print(greeting_message)

print("------------ f string  ------------------- ")
greeting_message = f"{greeting}, {name}. Welcome to world of {language}!"
print(greeting_message)

print("------------ string validator  ------------------- ")
message='abc1234'
print(message.isdigit(),message.isalnum(),message.isalpha(),message.istitle(),message.isdecimal())
print(message.isascii(),message.isidentifier(),message.isnumeric(),message.islower(),message.isprintable())

print("------------ string strip() => remove spaces  ------------------- ")
message = '   new world   '
print(message)
print(message.lstrip())
print(message.rstrip())
print(message.strip())

print("------------ string index() => returns index of substring / character ------------------- ")
message = 'new world'
print(message.index('r'))

print("------------ string count() => returns no of time substring / character appeared ------------------- ")
message = 'new world'
print(message.count('new'))
print(message.count('p'))

print("------------ string find() => return index if present else -1 ------------------- ")
print(message.find('world'))
print(message.find('India'))

print("------------ string title() => print every 1st letter capital ------------------- ")
message = 'new world'
print(message.title())

print("------------ string capitalize => first letter capital ------------------- ")
print(message.capitalize())

print("------------ string swapcase() ------------------- ")
message = 'happy thoughts'
print(message.swapcase())
message = 'HAPPY THOUGHTS'
print(message.swapcase())

print("------------ string replace() ------------------- ")
message = message.replace('hello','new')
print(message)

print("------------ string split() => string to list ------------------- ")
list_of_string = message.split()
print(list_of_string )

print("------------ " ".join(list) => list to string ------------------- ")
back_to_string = " ".join(list_of_string)
print(back_to_string)

print("------------ string startswith(), endswith() ------------------- ")
message = 'happy thoughts'
print(message.startswith('happy'),message.endswith('thoughts'))
print(message.startswith('sad'), message.endswith('happy'))

print("------------ string casefold() ------------------- ")
message = 'HAPPY THOUGHTS'
print(message.casefold())

print("------------ string removeprefix() ------------------- ")
message = 'Mr.India'
new_msg = message.removeprefix('Mr.')
print(message, new_msg)

print("------------ string zfill() ------------------- ")
message = 'Mr.India'
new_msg = message.zfill(5)
print(new_msg)

print("------------ len() ------------------- ")
print(len(message))

print("------------ type() ------------------- ")
print(type(message))

print("------------ dir() ------------------- ")
print(dir(message))

print("------------ help() ------------------- ")
print(help(str.partition))