"""Lesson 02 - Function Arguments: Positional, Keyword, Default, and Unpacking"""

# A function is a block of code that performs a specific task.
# Arguments are the inputs we pass to a function to control its behavior.

# ---------------------------------------------
# 1. Positional Arguments
# Arguments passed in order


def add(a, b):
    return a + b


def divide(dividend, divisor):
    return dividend / divisor


print("Positional arguments:")
print("add(10.0, 3.5) =", add(10.0, 3.5))
print("add(2.0, 6.5) =", add(2.0, 6.5))
print("divide(10.0, 2.0) =", divide(10.0, 2.0))

# ---------------------------------------------
# 2. Keyword Arguments
# Arguments passed using the parameter name
print("\nKeyword arguments:")
print("add(a=3.0, b=6.2) =", add(a=3.0, b=6.2))
print("add(b=5.0, a=7.8) =", add(b=5.0, a=7.8))
print("divide(divisor=3.0, dividend=10.0) =",
      divide(divisor=3.0, dividend=10.0))

# ---------------------------------------------
# 3. Default Arguments
# If not provided, the default value is used


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print("\nDefault arguments:")
print(greet("João", "Hi"))
print(greet("Maria", "Good morning"))
print(greet("Pedro"))  # Uses default greeting
print(greet(greeting="Hey", name="Carla"))  # Keyword order doesn't matter
print(greet(name="Lucas"))  # Only name provided

# ---------------------------------------------
# 4. Unpacking Arguments
# Allows passing sequences or dictionaries as arguments using * and **

# Unpacking a tuple or list
numbers = (10.0, 5.5)
print("\nUnpacking list/tuple:")
print("add(*numbers) =", add(*numbers))  # Equivalent to add(10.0, 5.5)
print("add(numbers[0], numbers[1]) =", add(numbers[0], numbers[1]))

# Unpacking a dictionary
data = {
    "a": 10.2,
    "b": 5.3
}
print("\nUnpacking dictionary:")
print("add(**data) =", add(**data))  # Equivalent to add(a=10.2, b=5.3)

# ---------------------------------------------
# 5. Extra: Flexible greeting example


def custom_greeting(name, greeting="Hi"):
    return f"{greeting}, {name}!"


print("\nCustom greeting examples:")
print(custom_greeting("Alice"))  # Uses default greeting
print(custom_greeting("Alice", greeting="Welcome"))
print(custom_greeting(greeting="Hey there", name="Bob"))  # Keyword reordered
