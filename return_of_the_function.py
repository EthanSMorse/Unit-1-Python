"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

# The function finds the square of a number.
def square (num1):
    return(num1 ** 2)
print (square (6))


"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""

# The function finds the area of a rectangle.
def area (length, width):
    return (length * width)
print (area (5, 24))

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

# The function converts celsius to fahrenheit.
def fahrenheit (celsius):
    return ((celsius * 1.8) + 30)
print (fahrenheit (24))

"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

# The function finds the average of a list of numbers.
def average (numbers):
    total = sum(numbers)
    return total/len(numbers)
print(average([2, 4, 6, 8, 10]))