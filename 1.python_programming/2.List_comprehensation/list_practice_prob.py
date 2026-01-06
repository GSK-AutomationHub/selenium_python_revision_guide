# [Basic] Generate a list [0, 2, 4, 6, 8] using a list comprehension.
print( [num for num in range(10) if num % 2 ==0])

# [Filter] — get a list of numbers greater than 2.
nums = [1, 2, 3, 4, 5]
print([num for num in nums if num > 2 ])

# [Transform] - get a list with the length of each word.
words = ['python', 'code', 'AI']
print([len(word) for word in words])

# [Filter + Transform] — get the square of each even number.
nums = [1, 2, 3, 4, 5]
print([pow(num,2) for num in nums if num % 2 ==0])

# flatten it into [1, 2, 3, 4, 5, 6]
matrix = [[1, 2], [3, 4], [5, 6]]
print([item for sublist in matrix for item in sublist])