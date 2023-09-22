'''
TASK 1 Even or Odd
Determine if a number is even or odd.
'''

# The user inputs a number, which is then determined to be eveon  or odd by dividing by 2.
num1 = float(input("Please enter a number: "))
rem = num1 % 2
if (rem == 1):
    print ("This number is odd.")
else:
    print("This number is even.")
print("")

'''
TASK 2 Positive, Negative, or Zero:
Determine if a number is positive, negative, or zero.

EXTRA CREDIT: Tell the user if they did not enter a valid number
'''

# The user inputs a number, which is then compared to 1, 0, or -1 to determine if the number is negative, positive, or 0.
num2 = float(input("Please enter a number: "))
if (num2 >= 1):
    print("This number is positive")
elif (num2 <= -1):
    print("This number is negative")
elif (num2 == 0):
    print("This number is equal to 0")
else:
    print ("This number is invalid.")
print("")

'''
TASK 3: Largest of Three
Find and print the largest of three numbers.
'''

# The user inputs 3 numbers, which are then compared to each other in order to determine which is the highest number.
num3 = input("Please enter a number: ")
num4 = input("Please enter another number: ")
num5 = input("Please enter one last number: ")
if (float(num3 > num4 and num5)):
    print (num3 + " is the largest number.")
if (float(num4 > num3 and num5)):
    print(num4 + " is the largest number.")
else:
    print(num5 + " is the largest number.")
print("")

'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''

# The user inputs a year, which is then divided by four. If there is a remainder, it is not a leap year. If there isnt, it is a leap year.
days = int(input("Please enter a year: "))
rem2 = (days % 4)
if (rem2 >= 1):
    print("This year is not a leap year.")
else:
    print("This year is a leap year")
print("")

'''
TASK 5: Vowel or Consonant:
Identify if a character is a vowel or consonant.

EXTRA CREDIT: Tell the user if they did not enter a valid letter
'''

# The user inputs a letter, and then using conditionals it is determined whether the letter is a vowe, a consonant, or invalid.
letter = input("Please enter a letter: ")
if (letter == "a" or "e" or "i " or "o" or "u"):
    print("This letter is a vowel.")
elif (letter == "b" or "c" or "d" or "f" or "g" or "h" or "j" or "k" or "l" or "m" or "n" or "p" or "q" or "r" or "s" or "t" or "v" or "w" or  "x" or "y" or "z"):
    print("This letter is a consonant.")
else:
    print("This letter is invalid.")