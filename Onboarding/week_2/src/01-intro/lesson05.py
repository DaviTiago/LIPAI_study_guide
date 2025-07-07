"""Data Types"""

# Numeric data types: int, float, complex

age = 20
weight = 70.5

print(age, type(age))  # int
print(weight, type(weight))  # float

# String data type
name = 'Pedro'
surname = "Silva"
full_name = name + ' ' + surname
print(full_name)  # str

product = 'Coca-Cola'

print(f'The client {full_name} bought {product}.')

print(name[0], name[1], name[2], name[3])
print(name[0:2])
print(name[0], name[-1])  # First and last character

print(name.upper())  # Convert to uppercase
print(name.lower())  # Convert to lowercase

print(1, 3, 7, 10, sep='-', end='\n')  # Print with hyphen separator

# Boolean data type
is_adult = True
is_minor = False
print(is_adult, type(is_adult))  # bool
print(is_minor, type(is_minor))  # bool

result = 10 < 3
print(result, type(result))  # bool

# List data type
fruits = ['apple', 'banana', 'cherry']
print(fruits)
print(fruits[0])  # Access first element
print(fruits[1:3])  # Access elements from index 1 to 2

fruits.append('orange')  # Add an element
fruits.remove('banana')  # Remove an element
print(fruits)
fruits[0] = 'kiwi'  # Modify an element
print(fruits)
print(len(fruits))  # Length of the list

# Tuple data type (immutable sequences)
codes = ('A001', 'B002', 'C003')
print(codes)
print(codes[0])  # Access first element
# codes[0] = 'D004'  # This will raise an error because tuples are immutable
print(len(codes))  # Length of the tuple

# Set data type (unordered collections of unique elements)
draw_result = {50, 10, 60, 45}
print(draw_result)
print(50 in draw_result)  # Check if an element is in the set
draw_result.add(70)  # Add an element
print(draw_result)
draw_result.remove(10)  # Remove an element
print(draw_result)

# Dictionary data type (key-value pairs)
employee = {
    'code': 'E001',
    'name': 'Alice',
    'salary': 5000.0
}

print(employee)
print(employee['name'])  # Access value by key
employee['salary'] = 5500.0  # Modify value by key
print(employee)
employee['department'] = 'HR'  # Add a new key-value pair
print(employee)
employee.pop('code')  # Remove a key-value pair
print(employee)

print(employee.keys())  # Get all keys
print(employee.values())  # Get all values
