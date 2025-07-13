"""Sets"""

# Sets are a built-in data type in Python that represent an unordered collection of unique elements.

# Characteristics of sets:
# - Unordered: no defined index or position
# - Mutable: you can add or remove elements
# - Iterable: can be used in loops (e.g., for-loops)
# - Do not allow duplicates
# - Can store elements of different data types

# Creating a set
fruits = {'apple', 'banana', 'cherry'}
print("Original set:", fruits)
print("Type:", type(fruits))

# Duplicates are automatically removed
numbers = {1, 5, 7, 4, 3, 3, 1}
print("Set with duplicates removed:", numbers)

# Iterating over a set
print("Iterating over 'numbers':")
for num in numbers:
    print(num)

# Membership testing
print("Is 2 in 'numbers'?", 2 in numbers)  # False
print("Is 1 in 'numbers'?", 1 in numbers)  # True

# Adding elements to a set
print("Fruits before add:", fruits)
fruits.add('orange')
print("Fruits after adding 'orange':", fruits)

# Adding a new number to 'numbers'
numbers.add(8)
print("Numbers after adding 8:", numbers)

# Combining sets with update()
other_numbers = {3, 4, 9, 11, 1, 5}
print("Other numbers:", other_numbers)

numbers.update(other_numbers)
print("Numbers after update with other_numbers:", numbers)

# Removing elements
# Removes 'banana' from the set
fruits.remove('banana')
print("Fruits after removing 'banana':", fruits)

# Removing a non-existing item using `discard()` avoids errors
fruits.discard('grape')  # Safe: does nothing if 'grape' is not in the set
print("Fruits after trying to discard 'grape':", fruits)

# Clearing all elements
# fruits.clear()
# print("Fruits after clear:", fruits)

# Set operations
print("Set operations:")
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Union:", set_a.union(set_b))         # {1, 2, 3, 4, 5}
print("Intersection:", set_a & set_b)       # {3}
print("Difference (A - B):", set_a - set_b)  # {1, 2}
print("Symmetric difference:", set_a ^ set_b)  # {1, 2, 4, 5}
