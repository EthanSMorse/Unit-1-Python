'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

# The user inputs a number, and the conditional determines if it is greater than 10 and even.
num = int(input("Please input a number: "))
remainder = num % 2
if (remainder == 0 and num > 10):
    print("True")
else:
    print("False")

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

# The user inputs their age and student status, and based off of that the cost is determined.
age = int(input("How old are you? (Number form): "))
student = input("Are you a current student? (Yes or No): ")
if (age < 18 or student == "Yes"):
    print("You owe 10 dollars.")
else:
    print("You owe 20 dollars.")

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

# A pre-existing list of fruits is compared to a input from the user. If their input fruit is in the list, a confirmation is printed.
fruits = ["apple", "orange", "pineapple"]
fruit = input("Please input a fruit: ")
if (fruit in fruits):
    print("Yes, that fruit is in the list.")
else:
    print("No, that fruit is not in the list.")

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

# The user inputs a year, which is then divided by 4 and 100 individually. If there is a remainder in either situation, the code returns a false, saying its not both a leap year and century year.
year = int(input("Please input a valid year: "))
rem1 = year % 4
rem2 = year % 100
if (rem1 == 0 and rem2 == 0):
    print("This year is both a century year and leap year.")
else:
    print("This year is not both a century year and leap year.")

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

# The user inputs their package weight and their zone, which is then used to determine their cost.
weight = float(input("Please input the weight (in kg) of your package: "))
zone = input("Please input your zone (Zone A or Zone B): ")
if (zone == "Zone A"):
    cost = weight * 5
elif (zone == "Zone B"):
    cost = weight * 7
else:
    print ("Please input a valid zone")

if (cost == 0):
    print("Error. Please enter a valid weight.")
else:
    print("You owe " + str(cost) + " dollars.")

