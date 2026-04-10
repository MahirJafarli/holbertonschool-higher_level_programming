#!/usr/bin/python3
"""Module that defines a Square class with size and position."""


class Square:
    """Class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The coordinates of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__size_position  # Error in logic fixed below

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with strict tuple validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' accounting for position."""
        if self.__size == 0:
            print("")
            return

        # Handle vertical position (position[1])
        # Only print newlines if size > 0
        if self.__position[1] > 0:
        for _ in range(self.__position[1]):
            print("")

        # Handle horizontal position (position[0]) and rows
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
