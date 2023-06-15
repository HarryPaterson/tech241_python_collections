#Dictionaries

#Key - Value pairs
#Key is name/reference, Value is the data stored

#Making a dictionary

student_1 = {
    "name" : "luke",
    "stream" : "devops",
    "completed_lessons" : 4,
    "completed_lesson_names" : ["variables", "git", "data_types", "collections"]
}
print(type(student_1))
#How to access parts of a dictionary

print(student_1["stream"])
print(student_1["completed_lesson_names"][0])

#Changing a value
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

student_1["completed_lesson_names"].remove("data_types")
print(student_1["completed_lesson_names"])

#Dictionary methods
print(student_1.values())
print(student_1.keys())