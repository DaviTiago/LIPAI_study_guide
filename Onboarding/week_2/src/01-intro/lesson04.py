"""Variables, Constants, and Literals"""

# Variables are used to store data that can change during the execution of a program.
# Constants are used to store data that should not change.
# type inference
number = 10
print(number)
print(number, type(number))

number = 20
print(number)

# multiple assignment
name, age, address = 'Maria', 30, 'Rua A, 123'
print(name, age, address)

name = 'João'
age = 25
address = 'Rua B, 456'
print(name, age, address)

name1 = name2 = name3 = 'Maria'
print(name1, name2, name3)

name2 = 'Pedro'
print(name1, name2, name3)

# snake_case
id_employee = 12345
salary_Annual = 50000.0
print(id_employee, salary_Annual)

# Constants
# Uppercase - SNAKE_CASE
PI = 3.14
CRIMINAL_MAJORITY_AGE = 18

# Literals
age = 27
print(age)
print(27)

# Numeric literals
print(10, type(10))      # Integer literal
print(10.5, type(10.5))  # Float literal
print(-10, type(-10))    # Negative integer literal

# String literals
print('Hello, world!', type('Hello, world!')) # Single quotes
print("Hello, world!", type("Hello, world!")) # Double quotes
# Single quotes with double quotes inside
print('The moon is "beautiful".', type('The moon is "beautiful".'))

# Boolean literals
print(True, type(True))
print(False, type(False))

# None literal
print(None, type(None))


# Collection literals

# List literal
numbers = [1, 2, 3, 4, 5]
print(numbers, type(numbers))
print([1, 2, 3], type([1, 2, 3]))

# Tuple literal
emails = ('joao@email.com', 'maria@email.com')
print(emails, type(emails))
print((1, 2, 3), type((1, 2, 3)))

# Dictionary literal
student = {
    'name': 'Maria',
    'age': 30,
    'address': 'Rua A, 123'
}
print(student, type(student))
print({'key': 'value'}, type({'key': 'value'}))

# Set literal
names = {'Maria', 'João', 'Pedro', 'Maria'}
print(names, type(names))
print({1, 2, 3}, type({1, 2, 3}))
