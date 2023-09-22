"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""

# I created a list with 4 items inside
list_a = ["bing", "bang", "bosh", "bipple"]
print(list_a)
print("")

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

# I added an item using the append command
list_a.append ("boom")
print(list_a)
print("")

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""

# I removed an item using the remove command
list_a.remove ("bipple")
print(list_a)
print("")

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

# I changed item 2 into a different item
list_a[2] = ("blam")
print(list_a)
print("")

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""

# I added 2 more items to the list using the append command
list_a.append("bingus")
list_a.append("brungle")
print(list)
print("")

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""

# I removed an item using its index number and the del command
del list_a[1]
print(list_a)
print("")

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""

# I created an new variable and gave it the values of the first 2 items in my list
listies = list_a[0:2]
print(listies)
print("")

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

# I made a second list with values from the first list, and then added it to the original list
list_1 = list_a[0]
list_2 = list_a[1]
list_b = [list_1, list_2]
list_c = (list_a + list_b)
print(list_c)
