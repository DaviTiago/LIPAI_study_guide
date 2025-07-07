"""I/O"""
# Input and Output in Python
import os

# Standard output - sys.stdout
print('Hello, world!')  # Output to console
# Output to console with custom end character
print('Hello, world', end='!!!!!\n')
# Output to console with custom separator
print('Hello', 'world', sep=' - ', end='!!\n')

# Input from user
name = input('Enter your name: ')  # Get input from the user
age = input('Enter your age: ')  # Get input from the user
print(f'Hello {name}, you are {age} years old.')  # Display formatted output
print(type(name), type(age))  # Show the types of the variables

# Note: input() returns a string. Convert to int if numeric operations are needed.
# Example of converting input to integer
age = int(input('Enter your age (again): '))  # Get input and convert to int
print(f'Hello {name}, you are {age} years old.')  # Display output
print(type(name), type(age))  # Confirm types

# Conditional output
if age >= 18:
    print(f'{name}, you are an adult.')
else:
    print(f'{name}, you are a minor.')
