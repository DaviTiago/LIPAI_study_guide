"""Lesson 05 - OOP: Special Methods"""

# In this lesson, we will explore special methods in Python classes.
# Special methods (also known as "magic methods" or "dunder methods", short for "double underscore")
# allow us to define how objects of a class interact with built-in functions and operators.

# Two common special methods:
# - __str__(self): Defines the "informal" or user-friendly string representation of an object.
#   It is called by functions like print() or str().
#
# - __repr__(self): Defines the "official" or developer-focused string representation.
#   It should return a string that can ideally recreate the object using eval().
#   Used in debugging, logs, and interactive interpreters like Jupyter or the Python REPL.


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    # __str__ returns a user-friendly description
    def __str__(self):
        return f"Rectangle: {self.width} cm x {self.height} cm"

    # __repr__ returns a string that can recreate the object
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


# Creating a Rectangle instance
rectangle1 = Rectangle(5, 10)

# Example: Using __str__ with print()
print(rectangle1)  # Outputs: Rectangle: 5 cm x 10 cm

# Example: __repr__ being used explicitly
print(repr(rectangle1))  # Outputs: Rectangle(5, 10)

# Using eval(repr(obj)) to recreate an object
rectangle2 = eval(repr(rectangle1))
print("Rectangle2 area:", rectangle2.calculate_area())

# Confirming the recreated object is a new instance
# False (they are different instances)
print("Same object?", rectangle1 is rectangle2)

# Using the walrus operator (assignment expression)
print(rect3 := Rectangle(8, 12))  # Uses __str__
