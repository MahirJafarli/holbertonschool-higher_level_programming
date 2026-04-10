#!/usr/bin/python3
"""Module defining a Square class with rich comparison operators."""


class Square:
    """Class representing a square."""

    def __init__(self, size=0):
        """Initialize the square with a size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with number validation (int or float)."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    # Rich Comparison Methods
    def __eq__(self, other):
        """Compare if two squares are equal in area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares are not equal in area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if one square is less than another in area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if one square is less than or equal to another in area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if one square is greater than another in area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if one square is greater than or equal to another in area."""
        return self.area() >= other.area()
