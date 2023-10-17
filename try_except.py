# The first try statement covers the age error, giving an error message if the user inputs an invalid value.
try:
    age = int(input('Enter your age: '))
    if age <= 21:
         print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')
except:
    print("Error! Entered age is not valid. Please try again.")

# The second try statement does the same as the first, but for the favorite number.
try:
    faveNum = int(input('What is your favorite number: '))
    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
except:
    print("Error! Your favorite number is invalid. Please try again.")