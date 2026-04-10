#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Class representing a square."""

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size
