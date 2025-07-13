"""Dictionaries"""

# Dictionaries are a built-in data type in Python that store data as key-value pairs.

# Characteristics of dictionaries:
# - Unordered: no fixed order (until Python 3.6, now insertion order is preserved)
# - Mutable: can be changed after creation
# - Iterable: can be used in loops
# - Keys must be unique and immutable (e.g., strings, numbers, tuples)
# - Values can be of any data type and may be duplicated

# Creating a dictionary
car = {
    'brand': 'Toyota',
    'model': 'Corolla',
    'year': 2020
}
print("Car dictionary:", car)
print("Type:", type(car))

# Accessing values using keys
print("Brand:", car['brand'])         # Direct access
print("Model (with get):", car.get('model'))  # Safe access

# Getting keys, values, and items
print("Keys:", car.keys())
print("Values:", car.values())
print("Key-value pairs:", car.items())

# Checking if a key exists
print("'color' in car?", 'color' in car)

# Adding a new key-value pair
car['color'] = 'Red'
print("After adding 'color':", car)

# Removing a key-value pair using pop
removed_brand = car.pop('brand')
print("Removed brand:", removed_brand)
print("After removing 'brand':", car)

print("---- Iterating over the dictionary ----")
# Iterating over keys
for key in car:
    print("Key:", key)

# Iterating over values
for value in car.values():
    print("Value:", value)

# Iterating over key-value pairs
for key, value in car.items():
    print(f"{key}: {value}")

# -----------------------------
# Working with a list of dictionaries

student1 = {
    'name': 'Alice',
    'age': 20,
    'major': 'Computer Science'
}

student2 = {
    'name': 'Bob',
    'age': 22,
    'major': 'Mathematics'
}

# Add new key-value pairs (grades)
student1['grades'] = [10.0, 9.5, 8.0]
student2['grades'] = [7.5, 8.0, 9.0]

# List of dictionaries
students = [student1, student2]

print("---- Students ----")
for student in students:
    print(f"Name: {student['name']}, Major: {student['major']}")
    for grade in student['grades']:
        print(f"  Grade: {grade}")

# -----------------------------
# Using dictionary methods for learning:

# Example: count how many students got at least one grade above 9
count_above_9 = 0
for student in students:
    if any(grade > 9 for grade in student['grades']):
        count_above_9 += 1
print(f"Students with a grade above 9: {count_above_9}")
