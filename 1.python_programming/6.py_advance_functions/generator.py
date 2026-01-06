# Question: “What is a generator? How is it different from a list?”
'''
 Core Conceptual Answer (what to say in an interview)
 - A generator is a special kind of iterator in Python that lazily produces items one at a time,
 - only when you ask for them — instead of storing the entire sequence in memory like a list does.
 - This makes generators memory-efficient and perfect for working with large datasets, streaming data, or infinite sequences.

🗂️ How to create a generator
You can create a generator in two main ways:

Method	How
Generator function	Uses yield instead of return
Generator expression	Similar to list comprehension, but with () instead of []
'''

#Examples : Generator function with yield

def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # pause & return value
        count += 1

# Create generator object
counter = count_up_to(5)
print(next(counter))

for num in counter:
    print(num)  # 1 2 3 4 5

''' Key point:
 - yield turns a normal function into a generator.
 - It remembers state between calls — no need to store all numbers at once.
'''

# Generator expression

squares = (x**2 for x in range(1, 6))

print(next(squares))  # 1
print(next(squares))  # 4
print(list(squares))  # Remaining: [9, 16, 25]

'''
# Note: You can only iterate once — generators don’t store all results.

# Difference between generator and list
Feature 	List	                        Generator
Memory	    Stores all elements at once	    Produces one item at a time
Speed	    Fast access to all elements	    Lazy, computes on the fly
Reuse	    Can loop multiple times	        One-time use; must recreate
Syntax	    [] or list()	                yield function or ()

# Why are generators useful in QA Automation?, They’re handy when:
 - Reading big log files line by line.
 - Generating large test data streams.
 - Implementing infinite data feeds or data-driven tests without blowing up memory.

# Summary to say in an interview:
“A generator is a special iterator that produces values on demand using yield, 
so it’s memory-efficient compared to lists which store all data at once. 
I use generators when handling large or streaming data where I don’t want to load everything into memory.”
'''
