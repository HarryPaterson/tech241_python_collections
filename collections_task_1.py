# Making a list of cool things
cool_things = ["super computer", "jet pack", "hangout spot", "yacht", "mansion for mum"]

# Print the list and check its type
print(cool_things)
print(type(cool_things))

# Print the list's first element
print(cool_things[0])

# Print the list's second element
print(cool_things[1])

# Print the list's last element using negative indexing
print(cool_things[-1])

# Replace the first item in the list
cool_things[0] = "wellness retreat"
print(cool_things)

# Replace another item in the list and print the list
cool_things[1] = "electric bike"
print(cool_things)

# Add a new item to the list, print the list
cool_things.append("barnet fc")
print(cool_things)

# Remove an item from the list, print the list
cool_things.remove("hangout spot")
print(cool_things)

# Remove the last item from the list without specifying what it is
cool_things.pop()
print(cool_things)

