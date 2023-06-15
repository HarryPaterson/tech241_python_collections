#List and Tuples

#Making a list in Python

shopping_list = ["egg","bacon","bananas","bread","haggis"]

print(shopping_list)

print(shopping_list[0])

#Changing an element of the list
shopping_list[4] = "orange juice"
print(shopping_list)

#List methods
shopping_list.append("butter")
print(shopping_list)

shopping_list.remove("butter")
print(shopping_list)

shopping_list.pop()
print(shopping_list)

#Mixed Data Type List
mixed_list = [ 1, 2, 3, "one", "two", "three"]
print(mixed_list[1:3])
print(mixed_list[::2])

#Tuples

essentials = ("milk","egg","bread")
essentials.append("toothpaste") #returns AttributeError: 'tuple' object has no attribute 'append'