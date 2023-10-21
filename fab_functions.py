# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".

# Takes a name, and returns it in a statement.
def greet(name):
    return("Hello, " + name)
greet("Ethan")


# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.

# Takes 2 numbers and adds them together
def sum_numbers(a, b):
    return (a + b)
sum_numbers(2, 5)

# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.

# Finds the factorial of a given number.
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        return (fact = fact * i)
factorial(7)

# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.

#Takes a number, finds its remainder, and compares it with 0 to determine if it is even or odd.
def is_even(num):
    rem = (num % 2)
    if (rem == 0):
        return("True")
    else:
        return("False")
is_even(5)

# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.

# Takes a length and width, and multiplies them together.
def calculate_area(length, width):
    return(length * width)
calculate_area(5, 10)