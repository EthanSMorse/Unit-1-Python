"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

# The function finds the square of a number, and then assert makes sure that the values are correct.
def square (num1):
    return(num1 ** 2)
assert square (6) == 36
print (square (6))
try:
    assert square (8) == 63
except:
    print("There was an error.")
print (square (8))
print("")

"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""

# The function finds the area of a rectangle, and then assert makes sure that the values are correct.
def area (length, width):
    return (length * width)
assert area (5, 24) == 120
print (area (5, 24))
try:
    assert area (11, 11) == 111
except:
    print("There was an error.")
print (area (11, 11))
print("")

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

# The function converts celsius to fahrenheit, and then assert makes sure that the values are correct.
def fahrenheit (celsius):
    return ((celsius * 1.8) + 32)
assert fahrenheit (24) == 75.2
print (fahrenheit (24))
try:
    assert fahrenheit (92) == 197.5
except:
    print("There was an error.")
print (fahrenheit (92))
print("")

"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

# The function finds the average of a list of numbers, and then the assert makes sure the values are correct.
def average (numbers):
    total = sum(numbers)
    return total/len(numbers)
assert average([2, 4, 6, 8, 10]) == 6
print(average([2, 4, 6, 8, 10]))
try:
    assert average([1, 3, 5, 7, 9]) == 1597
except AssertionError:
    print("There was an error.")
print(average([1, 3, 5, 7, 9]))