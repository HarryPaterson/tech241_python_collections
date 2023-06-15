<h1 style="text-align: center;">Collections</h1>

### Contents
* Lists
* Tuples
* Dictionaries
* Sets
* Frozen Sets

### Lists

Lists are ordered, mutable collections that can store elements of different data types. Some key features of lists include:

- Elements can be accessed using indices.
- Elements can be added, removed, or modified.
- Lists can contain duplicate elements.
- Lists are defined using square brackets.

```
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
```
### Tuples

Tuples are ordered, immutable collections that can store elements of different data types. Some key features of tuples include:

* Elements can be accessed using indices.
* Tuples cannot be modified once created.
* Tuples can contain duplicate elements.
* Tuples are defined using parentheses.

```
essentials = ("milk","egg","bread")
essentials.append("toothpaste") #returns AttributeError: 'tuple' object has no attribute 'append'
```

### Dictionaries

Dictionaries are key-value pairs that store data as an unordered collection. Some key features of dictionaries include:

* Data is stored as key-value pairs.
* Elements are accessed using keys rather than indices.
* Keys are unique within a dictionary.
* Dictionaries are defined using curly braces and colons.

```
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
```

### Sets

Sets are unordered collections of unique elements. Some key features of sets include:

* Elements in a set are unique and unordered.
* Sets do not allow duplicate elements.
* Set operations like union, intersection, and difference can be performed.
* Sets are defined using curly braces or the set() function.

```
{} - list but unordered
car_parts = {"wheels","windows","exhaust","steering wheel"}
print(car_parts)

#add to a set
car_parts.add("doors")
print(car_parts)

#remove from a set
car_parts.remove("doors")
print(car_parts)
```
### Frozen Sets

Frozen sets are immutable versions of sets. Some key features of frozen sets include:

* Elements in a frozen set are unique and unordered.
* Frozen sets do not allow duplicate elements.
* Frozen sets cannot be modified once created, but they can be used as keys in dictionaries.
* Frozen sets are defined using the frozenset() function.

```
x = frozenset(["one","two","three","four"])
print(x)
```# tech241_python_collections
