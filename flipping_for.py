"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""

# I set up a string that contains the alphabet, and then using a for loop, printed each letter individually.
string = "abcdefghijklmnopqrstuvwxyz"
for x in string:
    print (x)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""

# I set up a list of numbers and a variable, and then used a for loop to update the value of the variable by the sum of its intial value and list values.
numbers = [3, 5, 7, 11, 254]
sum = 0
for x in numbers:
    sum += x
print(sum)

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""

# I create a string which I then split into a list, by each space. Then, I use the len function to determine the amount of characters each word has.
sen = "I love dairy."
sen = sen.split(" ")
for x in sen:
    print (len(x))

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""

# I set up a dictionary with 4 sets of keys and values, and then printed each one.
diction = {
    "apple":1,
    "orange":2,
    "pineapple":27,
    "peach":3457
}
for x in diction:
    print(x)
# I notice that it onlyt prints the keys, not the values for said keys. I thought it would print both.