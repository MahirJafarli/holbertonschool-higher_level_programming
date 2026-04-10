#!/usr/bin/python3
"""Square generation module for Python project 0x06
"""


class Square:
    """Class defined for square generation."""

    def __init__(self, size=0):
        """Initialize the square using the public setter to ensure validation."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size with validation for numbers (int/float) >= 0."""
        if not isinstance(value, (int, float)):
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculates area of square."""
        return self.__size * self.__size

    # --- Rich Comparisons ---

    def __lt__(self, other):
        """Less than comparison."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Equal comparison."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparison."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison."""
        return self.area() >= other.area()
