# Create menu
starters = ["oysters", "calamari", "salmon tartare", "lobster soup", "grilled peppers"]
mains = ["lobster", "black cod", "tiger roll", "prawn gyoza", "sea bream"]
desserts = ["mango sorbet", "chocolate fondant", "assorted truffles", "cheesecake", "peach pie"]

# Display menu
print("Welcome, here is our menu.")
print("---Menu de la restaurant hoping you like fish---")
print("Starters:")
print(starters)
print("Mains:")
print(mains)
print("Desserts:")
print(desserts)

#Create order
order = []

#Take order
print("So what shall we have to start?:")
starter_choice = input()
order.append(starter_choice)
print("Fabulous choice. And for your main?:")
main_choice = input()
order.append(main_choice)
print("A personal favourite of mine! Will we be having dessert this evening?:")
dessert_choice = input()
order.append(dessert_choice)
print("Wonderful.")
print(order)
#Display order back
print("So to confirm, you will begin with the " + order[0] + " before moving on to the most stupendous " + order[1] + " before wrapping up with with a spot of " + order[2] + ". Have a wonderful evening")

