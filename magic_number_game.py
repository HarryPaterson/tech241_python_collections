#Magic number game

# Set magic number
magic_number = "7"

# Game loop
print("Welcome traveller, I am the mystical Dr.Python, care to check your powers to foresee code? Guess the variable magic_number! I will give you three guesses.")

#Get guess
for x in range(3):
    guess = input("To what number have I set the variable?: ")

#Check if correct and give result
    if guess == magic_number:
        print("Wow, that's correct! That's so statistically unlikely. Did I set the number too 13"
              "low? Do people just like the number 7? No bother, the house always wins...")
        break
    else:
        print("Incorrect! Look into the code and try again...")
else:
    print("Tough luck! You were not able to guess the code! My friend where are you going? 50p! It is not free...")
