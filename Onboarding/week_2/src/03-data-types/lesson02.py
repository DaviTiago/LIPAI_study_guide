"""Tuples"""

# Tuples are collections very similar to lists, but they are immutable.
# This means once a tuple is created, it cannot be modified.
# Characteristics:
# - Ordered (elements have a defined index)
# - Immutable (cannot be changed)
# - Iterable (can be used in loops)
# - Allows duplicate values
# - Can contain different data types
# - Can contain nested tuples (tuples inside tuples)

# Creating a tuple
names = ('Maria', 'Pedro', 'João')
print("Original tuple:", names)
print("Type:", type(names))

# Accessing elements by index
print("First name:", names[0])            # Maria
print("First two names:", names[0:2])     # Maria, Pedro
print("First two names (shortcut):", names[:2])  # Maria, Pedro
print("From second name onward:", names[1:])     # Pedro, João

# Getting the length of the tuple
size = len(names)
print("Tuple size:", size)

# Tuples are immutable: elements cannot be added, removed, or modified.
# names[0] = 'Maria da Silva'  # ❌ This will raise a TypeError

# Iterating over a tuple using for-in
print("Iterating with for-in:")
for name in names:
    print("Name:", name)

# Iterating over a tuple using index
print("Iterating with index:")
for i in range(len(names)):
    print(f"Index {i}:", names[i])

# Creating another tuple (parentheses are optional for creation)
names2 = 'Ana', 'Lucia', 'Marcos'
print("Another tuple:", names2)
print("Type:", type(names2))

# Tuple unpacking
# This means assigning each element of a tuple to a variable
name1, name2, name3 = names2
print("Unpacked names:", name1, name2, name3)

# Concatenating tuples
all_names = names + names2
print("Concatenated tuple:", all_names)
print("Type of result:", type(all_names))
