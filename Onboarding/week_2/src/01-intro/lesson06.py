"""Type Conversion"""
# Implicit and explicit type conversion in Python

# Implicit conversion (automatic)
num1 = 10  # int
num2 = 3.5  # float
result = num1 + num2  # int + float -> float
print(result, type(result))  # Output: 13.5 <class 'float'>

# Explicit conversion (manual)
num3 = 20  # int
num4 = 4.0  # float
result2 = num3 + int(num4)  # int + int -> int
print(result2, type(result2))  # Output: 24 <class 'int'>

# String conversion (type casting)
# sum = '15' + 10  # This would raise an error because '15' is a string
sum = float('15.3') + 10  # Convert string to float before adding
print(sum, type(sum))  # Output: 25.3 <class 'float'>

num_str = '12'
num_int = int(num_str)  # Convert string to int
print(num_int, type(num_int))  # Output: 12 <class 'int'>

# Converting a number to a string
name = 'Davi'
height = 1.75

# message = name + ' is ' + str(height) + ' meters tall.'
# Using f-string for better readability
message = f'{name} is {height} meters tall.'
print(message)  # Output: Davi is 1.75 meters tall.
