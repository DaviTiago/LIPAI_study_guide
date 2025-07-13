"""Lesson 03 - *args and **kwargs: Advanced Function Arguments"""

# In this lesson, we'll explore advanced function arguments in Python:
# - *args: Variable number of positional arguments (as a tuple)
# - **kwargs: Variable number of keyword arguments (as a dictionary)
# - Unpacking arguments from sequences and mappings
# - Using *args and **kwargs together with default values

# ---------------------------------------------
# 1. *args (Variable Positional Arguments)


def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


print("1. Using *args (positional arguments):")
print("sum_numbers(1, 2, 3) =", sum_numbers(1, 2, 3))
print("sum_numbers(4, 5, 6, 7) =", sum_numbers(4, 5, 6, 7))

# *args allows us to pass any number of positional arguments.
# Inside the function, 'args' is a tuple.


def world_cup_titles(country, *years):
    print(f"{country} has won the World Cup {len(years)} times:")
    for year in years:
        print(f" - Year: {year}")


print("\nWorld Cup Titles:")
world_cup_titles("Brazil", 1958, 1962, 1970, 1994, 2002)

# ---------------------------------------------
# 2. **kwargs (Variable Keyword Arguments)


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print("\n2. Using **kwargs (keyword arguments):")
print_info(name="Alice", age=30, city="New York")

# **kwargs allows passing named arguments that are packed into a dictionary


def calculate_price(value, **kwargs):
    tax = kwargs.get("tax_percentage", 0)
    discount = kwargs.get("discount", 0)
    final_price = value + (value * tax / 100) - discount
    return final_price


print("\nCalculate final price with **kwargs:")
print("Price with tax 10% and discount 5:",
      calculate_price(100, tax_percentage=10, discount=5))
print("Price with tax only:", calculate_price(200, tax_percentage=15))
print("Price with discount only:", calculate_price(150, discount=20))
print("Price with no extras:", calculate_price(300))

# ---------------------------------------------
# 3. Using *args and **kwargs Together


def show_all(*args, **kwargs):
    print("Positional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)


print("\n3. Combining *args and **kwargs:")
show_all(1, 2, 3, name="Bob", age=25)

# ---------------------------------------------
# 4. Unpacking Arguments (when calling functions)


def multiply(a, b):
    return a * b


def display_user(name, age):
    print(f"Name: {name}, Age: {age}")


numbers = [3, 4]
user = {"name": "Charlie", "age": 28}

print("\n4. Unpacking arguments:")
print("multiply(*numbers):", multiply(*numbers))        # list unpacking
display_user(**user)                                    # dictionary unpacking

# ---------------------------------------------
# 5. *args and **kwargs with Default Parameters


def greet(name, greeting="Hello", *args, **kwargs):
    print(f"{greeting}, {name}!")
    if args:
        print("Extra positional arguments:", args)
    if kwargs:
        print("Extra keyword arguments:", kwargs)


print("\n5. *args and **kwargs with default values:")
greet("Alice", "Hi", 1, 2, 3, mood="happy", language="English")

# ---------------------------------------------
# 6. Summary
# - Use *args when you want to receive multiple positional arguments as a tuple.
# - Use **kwargs when you want to receive multiple named (keyword) arguments as a dictionary.
# - They provide flexibility when defining functions that need to handle a variety of inputs.
# - You can also use * and ** to unpack arguments when calling functions.


