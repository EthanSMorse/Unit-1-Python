import datetime
from datetime import time

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""

current = datetime.datetime.now()
print(current)


"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

now = datetime.datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
date_time = now.strftime("%m/%d/%Y")
print(date_time)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""




"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""