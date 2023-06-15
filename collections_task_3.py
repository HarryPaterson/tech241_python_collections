# Define the dictionary
story = {
    "start": "In the city of Sparta, there was a DevOps engineer bitten by a cosmic space serpent",
    "middle": "Sparta had long been overrun by long wait times for passports due to a labour shortage in the home office, until the arrival of THE HUMAN PYTHON",
    "end": "The Human Python, with their new found ability to code, solved this issue and always followed was was considered best practice."
}

# Print the entire dictionary
print(story)

# Print the type of the dictionary
print(type(story))

# Print only the keys
print(story.keys())

# Print only the values
print(story.values())

# Print the individual values using the keys
print(story["start"])
print(story["middle"])
print(story["end"])

# Add a new key-value pair
story["epilogue"] = "The Human Python will return in 2 Human 2 Python Summer 2024"

# Print the updated dictionary
print(story)

