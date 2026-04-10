#!/usr/bin/python3
"""Module that defines a Square class with a printing method."""


class Square:
    """Class representing a square."""

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square sides.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the current square area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#' to stdout.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
