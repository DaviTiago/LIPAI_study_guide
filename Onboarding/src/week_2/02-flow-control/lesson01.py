""" Lesson 01 - Operators """

# Arithmetic Operators
a = 10
b = 3.5

print('Addition:', a + b)             # Output: 13.5
print('Subtraction:', a - b)          # Output: 6.5
print('Multiplication:', a * b)       # Output: 35.0
print('Division:', a / b)             # Output: 2.857...
print('Floor Division:', a // b)      # Output: 2.0
print('Modulus:', a % b)              # Output: 3.0
print('Exponentiation:', a ** 2)      # Output: 100

# Assignment Operators
x = 20
x += 5  # same as x = x + 5
print('Assignment result:', x)

# Comparison Operators
print('10 == 10:', 10 == 10)          # True
print('10 != 5:', 10 != 5)            # True
print('10 > 5:', 10 > 5)              # True
print('10 >= 10:', 10 >= 10)          # True
print('10 < 15:', 10 < 15)            # True
print('10 <= 10:', 10 <= 10)          # True

# Logical Operators
print('True and True:', True and True)
print('True and False:', True and False)
print('False or True:', False or True)
print('not False:', not False)

age = 18
has_id = True
print('Can enter club:', age >= 18 and has_id)

# Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print('x == z:', x == z)      # True (same content)
print('x is z:', x is z)      # False (different memory locations)
print('x is y:', x is y)      # True (same object)

# Membership Operators
phrase = 'You are awesome!'
print("'awesome' in phrase:", 'awesome' in phrase)  # True
print("'bad' in phrase:", 'bad' in phrase)          # False

numbers = [10, 20, 30]
print('20 in numbers:', 20 in numbers)              # True
print('40 not in numbers:', 40 not in numbers)      # True

person = {
    'name': 'Alice',
    'age': 25
}
print("'name' in person:", 'name' in person)        # True
# False (checks keys, not values)
print("'Alice' in person:", 'Alice' in person)

# Bitwise Operators (advanced usage)
a = 5   # binary: 0101
b = 3   # binary: 0011

print('Bitwise AND (a & b):', a & b)   # 1  (0001)
print('Bitwise OR (a | b):', a | b)    # 7  (0111)
print('Bitwise XOR (a ^ b):', a ^ b)   # 6  (0110)
print('Bitwise NOT (~a):', ~a)         # -6 (inverts bits)
