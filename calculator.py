print("Welcome To My Calculator!")

print("")

while (1):

    num1 = float(input("Input your first number: "))
    num2 = float(input("Input your second number: "))

    print("")

    print("Select your operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Remainder")
    print("7. Exponential")

    print("")

    selection = int(input("Please enter the number of your desired operation: "))

    print("")

    if (selection == 1):
        print("Result: " + str(num1 + num2))
    elif (selection == 2):
        print("Result: " + str(num1 - num2))
    elif (selection == 3):
        print("Result: " + str(num1 * num2))
    elif (selection == 4):
        print("Result: " + str(num1 / num2))
    elif (selection == 5):
        print("Result: " + str(num1 // num2))
    elif (selection == 6):
        print("Result: " + str(num1 % num2))
    else:
        print("Result: " + str(num1 ** num2))

    print("")