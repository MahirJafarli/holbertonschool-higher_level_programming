#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct: A pointer to the function to be executed.
        *args: Variable arguments to pass to the function.

    Returns:
        The result of the function if successful.
        None if an exception occurs, with the error printed to stderr.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
