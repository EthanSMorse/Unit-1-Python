todo = []
while (1):
    app = input("Would you like to add, remove, or check todos? ")
    if (app == "add"):
        added = input("What would you like to add? ")
        todo.append (added)
        print(todo)
    elif (app == "remove"):
        remove = int(input("Which numbered item do you want to remove? "))
        del todo [remove - 1]
        print(todo)
    elif (app == "check"):
        print(todo)
    else:
        print("The command you input is invalid. Please try again.")
        continue
    
