#Magic number game

#Import Random

import random

# Set magic number
magic_number = random.randint(0,10)

# Game loop
print("Welcome traveller, I am the mystical Dr.Python, care to check your powers to foresee code? Guess the variable magic_number! I will give you three guesses.")

#Get guess
for guess in range(3):
    guess = int(input("To what number have I set the variable? Between 1-10: "))

#Check if correct and give result
    if guess == magic_number:
        print("Wow, that's correct! That's so statistically unlikely. Did I set the numbers too low? No bother, the house always wins...")
        break
    else:
        print("Incorrect! Look into the code and try again...")
else:
    print("Tough luck! You were not able to guess the variable! It was " + str(magic_number))
