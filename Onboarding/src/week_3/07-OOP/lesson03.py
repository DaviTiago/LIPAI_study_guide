"""Lesson 03 - OOP: Instance and Class Methods"""

# In this lesson, we explore the difference between instance methods and class methods.
# - Instance methods operate on an instance of the class (using 'self').
# - Class methods operate on the class itself (using 'cls') and are often used to create instances in alternative ways.


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    @classmethod
    def build_from_list(cls, dimensions):
        """
        Class method that builds a Rectangle instance from a list [width, height].
        This is useful when dimensions are stored or received as a list.
        """
        return cls(dimensions[0], dimensions[1])

    @classmethod
    def from_string(cls, string):
        """
        Class method that builds a Rectangle instance from a string "width,height".
        This is useful when data comes from a text file or user input.
        """
        width, height = map(float, string.split(","))
        return cls(width, height)


# Creating Rectangle instances using different methods
rectangle1 = Rectangle(5, 10)                          # 
rectangle2 = Rectangle(3, 6)                           # 
rectangle3 = Rectangle.build_from_list([2, 4])         
rectangle4 = Rectangle.from_string("8.5, 12.9")


print(rectangle1.calculate_area())
print(rectangle2.calculate_area())
print(rectangle3.height, rectangle3.width, rectangle3.calculate_area())
print(f"Rectangle4 area: {rectangle4.calculate_area()}")

# Summary:
# Class methods like 'build_from_list' and 'from_string' allow us to create Rectangle objects
# from different data formats. This is a clean and reusable way to handle object creation,
# especially when the data is coming from external sources like files or user input.
