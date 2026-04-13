#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().

    Args:
        value: Can be any type (integer, string, etc.)

    Returns:
        True if value has been correctly printed (is an integer).
        False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
