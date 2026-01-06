#Using slicing (most common):
my_string = "BostonScientific"
reversed_string = my_string[::-1]
print(reversed_string)  # "citneicSnotsoB"
#Explanation: [::-1] means: start to end, step -1 → reverses the sequence.

# Using reversed() and join():
my_string = "BostonScientific"
reversed_string = ''.join(reversed(my_string))
print(reversed_string)  # "citneicSnotsoB"
#Explanation: reversed() returns an iterator → join() combines into a new string.

#Using a loop:
my_string = "BostonScientific"
reversed_string = ''
for char in my_string:
    reversed_string = char + reversed_string
print(reversed_string)  # "citneicSnotsoB"
# Explanation: Each character is added in front → builds reversed string step by step.