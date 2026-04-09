#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    return {key: value * 2 for key, value in a_dictionary.items()}
