"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""

# I made the float variable, and then converted it into a integer using the int function.
# Then, I used print on both the original variable and a converted one.
myFloat = 4.5
print(myFloat)
print(int(myFloat))
print("")

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""

# I made an variable that would take tghe value of tghe users input.
# Then, using conditional statements, it would determine if the variable was greater, less than, or equal to 0.
# Lastly, it would print a statement based on what condition it fell under.
input_num = int(input("Please input a number: "))
if (input_num > 0):
    print("This number is positive.")
elif (input_num < 0):
    print("This number is negative.")
else:
    print("This  number is equal to 0")
print("")

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""

# First, I collect both a integer and a float.
# Then, I convert them both into floats, so they can actually be added.
# Lastly, I print their sum after adding them together.
input_num = float(input("Please input an integer: "))
input_float = float(input("Please input a float: "))
print(input_num + input_float)
print("")

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""

# First, I made a dictionary of both apples and oranges, assigning them both their own numbers.
# Then, I singled out the oranges, and printed the number assigned to it.
my_fruits = {
    "apples": 5,
    "oranges": 8
}
print(my_fruits["oranges"])
print("")

"""
TASK 5:

Create a string variable that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

# First, I made a string seperated by commas.
# Then, I converted the string into a list by specifying commas as delimiters.
# Lastly, I turned the list into a tuple using the tuple function.
my_string = "Boom, Blam, Bing, Bam, Bosh"
my_list = my_string.split(",")
print(tuple(my_list))