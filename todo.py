# First, I set up a variable that would represent the todo list. It starts out empty because the user has to add things to it.
todo = []
# Next, the loop starts, signalling the beginning of the todo program. 
# The user inputs whatever it is they would like to do, and the coinciding conditional responds.
while (1):
    app = input("Would you like to add, remove, or check todos? ")
# If the user inputs 'add', then it will ask you what item you would like to add.
# Whatever they type in response will be put into the todo list.
    if (app == "add" or app == "Add"):
        added = input("What would you like to add? ")
        todo.append (added)
        print(todo)
# If the user inputs 'remove', then it will ask for the number of the item they would like to remove.
# Whatever number they type in will be subtracted by 1, because list indexes start at 0.
    elif (app == "remove" or app == "Remove"):
        remove = int(input("Which numbered item do you want to remove? "))
        del todo [remove - 1]
        print(todo)
# if the user inputs 'check',  the current list will be brought up.
    elif (app == "check" or app == "Check"):
        print(todo)
# Any answers other than this one will be seen as invalid.
    else:
        print("The command you input is invalid. Please try again.")
    
