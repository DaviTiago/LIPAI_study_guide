"""Lesson 01: Introduction to Object-Oriented Programming (OOP)"""

# In this lesson, we will explore the basics of Object-Oriented Programming (OOP) in Python.
# OOP is a programming paradigm that uses "objects" to represent data and methods to manipulate that data.

# Key concepts of OOP:
# - Classes: Blueprints for creating objects.
# - Objects: Instances of classes.
# - Attributes: Data stored in an object.
# - Methods: Functions that operate on an object.
# - Inheritance: Mechanism to create a new class from an existing class.

# -----------------------------------------------
# Part 1 - Without OOP (using dictionaries)
rectangle1 = {
    "width": 5,
    "height": 10
}

rectangle2 = {
    "width": 3,
    "height": 6
}


def calculate_area(rectangle):
    return rectangle["width"] * rectangle["height"]


def calculate_perimeter(rectangle):
    return 2 * (rectangle["width"] + rectangle["height"])


print("Without OOP:")
print(f"Area of rectangle1: {calculate_area(rectangle1)}")
print(f"Perimeter of rectangle1: {calculate_perimeter(rectangle1)}")
print(f"Area of rectangle2: {calculate_area(rectangle2)}")
print(f"Perimeter of rectangle2: {calculate_perimeter(rectangle2)}")
print("------------------------------------------------")

# -----------------------------------------------
# Part 2 - With OOP (using classes and objects)

# Define a class called Rectangle
# Class has attributes: width and height
# Class has methods: calculate_area and calculate_perimeter (Functions that operate on the object's data)
# This allows us to encapsulate the data and behavior related to rectangles in a single entity.

class Rectangle:
    # Constructor to initialize width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Method to calculate the area
    def calculate_area(self):
        return self.width * self.height

    # Method to calculate the perimeter
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


# Create instances (objects) of the Rectangle class
rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(3, 6)

print("With OOP:")
print(f"Area of rectangle1: {rectangle1.calculate_area()}")
print(f"Perimeter of rectangle1: {rectangle1.calculate_perimeter()}")
print(f"Area of rectangle2: {rectangle2.calculate_area()}")
print(f"Perimeter of rectangle2: {rectangle2.calculate_perimeter()}")
