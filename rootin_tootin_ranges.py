"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""

# Counts from 1 to 10
for x in range(1, 11):
    print(x)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""

# Counts from 900 to 1000 in increments of 10
for x in range(900, 1001, 10):
    print(x)

"""
Exercise 3:
Write a program that counts from 1-100 by 9
"""

# Code counts from 1 to 99 in increments of 9
for x in range(0, 101, 9):
    print(x)

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""

# Adds every number from 1 to 10
sum = 0
for x in range(1, 11):
    sum += x
print(sum)

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5

for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()

# The first loop keps a count of the iterations, the second adds a star for each iteration done.