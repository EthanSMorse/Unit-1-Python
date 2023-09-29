"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""

# 
num1 = 1
while (num1 <= 10):
    print (num1)
    num1 += 1

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""


num2 = 10
while (num2 >= 1):
    print (num2)
    num2 -= 1

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""




"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""


password = "BellyButton42"
guess = ""
while (guess != password):
    guess = input("Please guess a password: ")
    print(guess)
    if (guess == password):
        print("You guessed correctly!")
    else:
        print("You didnt guess correctly. Try again!")

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""





"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""


pref = int(input("How many numbers of the sequence do you want? "))
fib1 = 0
fib2 = 1
counter = 0
print(fib1)
print(fib2)
while (counter + 2 < pref):
    fib2 = fib1
    fib2 = (fib1 + fib2)
    fib1 = (fib1 + fib2)
    print(fib1)
    counter += 1