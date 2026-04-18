#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    Prints an integer with "{:d}".format().

    Args:
        value: The value to print (can be any type).

    Returns:
        True if value was printed correctly as an integer.
        False otherwise, with an error message printed to stderr.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
