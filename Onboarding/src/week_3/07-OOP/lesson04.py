"""Lesson 04 - OOP: Property"""

# In this lesson, we will explore the use of @property in Python classes.
# Properties allow us to:
# - Control access to instance attributes (encapsulation)
# - Add validation logic when getting or setting a value
# - Make methods behave like attributes (for cleaner and safer code)


class Rectangle:

    def __init__(self, width, height):
        # These will call the setter methods below
        self.width = width
        self.height = height

    # Getter for width
    @property
    def width(self):
        return self._width

    # Setter for width
    @width.setter
    def width(self, value):
        if value <= 0.0:
            raise ValueError("Width must be greater than zero.")
        self._width = value

    # Getter for height
    @property
    def height(self):
        return self._height

    # Setter for height
    @height.setter
    def height(self, value):
        if value <= 0.0:
            raise ValueError("Height must be greater than zero.")
        self._height = value


# Creating a Rectangle instance with valid dimensions
rectangle1 = Rectangle(5, 6)

# Using the property setters to change values
rectangle1.width = 7       # Calls width.setter
rectangle1.height = 10     # Calls height.setter

# Using the property getter
print("Width:", rectangle1.width)  # Calls width getter
print("Height:", rectangle1.height)
