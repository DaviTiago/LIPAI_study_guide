""" Lists """

# Lists are one of the most commonly used data types in Python.
# A list is a collection that is:
# - Ordered (elements have a defined index)
# - Mutable (can be changed)
# - Iterable (can be used in loops)
# - Allows duplicate values
# - Can hold elements of different data types
# - Can contain nested lists (lists inside lists)
# - Dynamically sized (can grow or shrink)

# Creating a list
names = ['Maria', 'Pedro', 'João']
print("Original list:", names)
print("Type:", type(names))

# Accessing elements by index
print("First name:", names[0])          # Maria
print("First two names:", names[0:2])   # Maria, Pedro
print("First two names (simplified):", names[:2])  # Maria, Pedro
print("From second name onwards:", names[1:])      # Pedro, João

# Modifying elements
names[0] = 'Maria da Silva'
names[1:] = ['Pedro da Silva', 'João Santos']
print("Modified list:", names)

# Getting the length of the list
size = len(names)
print("List size:", size)

# Adding elements to the list

# .append() - adds at the end
names.append('Marta Gomes')
print("After append:", names)

# .insert(index, element) - inserts at a specific position
names.insert(0, 'Guilherme Tavares')  # insert at the beginning
print("After insert at position 0:", names)

names.insert(2, 'Ana Lucia')          # insert at position 2
print("After insert at position 2:", names)

# .extend() - add multiple elements from another list
more_names = ['Kaio Silva', 'Carlos Gomes']
print("List size before extend:", len(names))
names.extend(more_names)
print("List size after extend:", len(names))
print("After extend:", names)

# Removing elements from the list

# .remove(value) - removes the first occurrence of the value
names.remove('Maria da Silva')
print("After remove:", names)

# del keyword - remove by index
del names[0]
print("After del [0]:", names)

# del can also be used to delete the entire list from memory
# del names

# .clear() - removes all elements from the list
# names.clear()
print("After clear (commented out):", names)

# Iterating over a list
print("Iterating with for-in:")
for name in names:
    print(name)

print("Iterating with index:")
for i in range(len(names)):
    print(f"Position {i}: {names[i]}")
