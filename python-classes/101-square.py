#!/usr/bin/python3
"""Module defining a Square class with string representation."""


class Square:
    """Class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return square area."""
        return self.__size ** 2

    def __str__(self):
        """Define the string representation of the Square instance."""
        if self.__size == 0:
            return ""

        res = []
        # Add vertical offset
        for _ in range(self.__position[1]):
            res.append("")

        # Add horizontal offset and the square rows
        for _ in range(self.__size):
            res.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(res)

    def my_print(self):
        """Print the square using the __str__ logic."""
        print(self.__str__())
