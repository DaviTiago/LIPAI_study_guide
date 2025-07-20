"""Lesson 02 - OOP: Class and Instance Attributes"""

# The Person class has:
# - A class attribute: species (shared by all instances)
# - Instance attributes: name, email (unique for each instance)


class Person:
    # Class attribute
    species = "Human"

    def __init__(self, name, email):
        # Instance attributes
        self.name = name
        self.email = email


# Creating instances of the Person class
person1 = Person("Alice", "alice@email.com")
person2 = Person("Bob", "bob@email.com")

# Overriding the class attribute for person1 by creating an instance attribute
person1.species = "Alien"

# Outputs
print("Person 1:")
print("  Name:", person1.name)
print("  Email:", person1.email)
print("  Species (instance attribute):", person1.species)

print("\nPerson 2:")
print("  Name:", person2.name)
print("  Email:", person2.email)
print("  Species (class attribute):", person2.species)

print("\nClass attribute 'species':", Person.species)
print("Person 1 species (class attribute):", person1.__class__.species)
print("Person 2 species (class attribute):", person2.__class__.species)