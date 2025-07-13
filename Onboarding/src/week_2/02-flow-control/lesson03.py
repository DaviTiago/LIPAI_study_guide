""" For Loop """

# A for loop is used to iterate over a collection of elements
# and repeat a block of code for each item in that collection.

languages = ['C', 'Python', 'Java', 'Rust']

# Accessing elements manually (not efficient)
print(languages[0])
print(languages[1])
print(languages[2])

# Using a for loop to iterate through the list
for language in languages:
    print(language.upper())  # Convert each language to uppercase

# Note: The behavior of the 'in' operator changes depending on the context
print('Java' in languages)  # Checks if 'Java' is in the list

# Calculating average without using a list
grade1 = 10.0
grade2 = 5.5
grade3 = 8.3
average = (grade1 + grade2 + grade3) / 3
print("Average (without list):", average)

# Using a list and for loop to calculate the average
grades = [10.0, 5.5, 8.3, 2.5]
total = 0.0
for grade in grades:
    total += grade  # total = total + grade
average = total / len(grades)
print("Average (with loop):", average)

# Using range() to generate sequences
# range(start, stop, step)

# Examples:
# range(10) → 0 to 9
# range(0, 10) → 0 to 9
# range(0, 10, 2) → even numbers from 0 to 8
# range(9, -1, -2) → odd numbers from 9 to 1 (in reverse)

values = range(9, -1, -2)
print("Range values:")
for value in values:
    print(value)

# Iterating using index (less common but sometimes useful)
for i in range(len(languages)):
    print(f"Language at index {i}:", languages[i])

# Preferred way: direct iteration
for language in languages:
    print("Language:", language)

# Iterating with a step (e.g., every 2 elements)
print("Languages with step of 2:")
for i in range(0, len(languages), 2):
    print(languages[i])
