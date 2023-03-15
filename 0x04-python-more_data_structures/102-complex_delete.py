#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    for k, v in a_dictionary.copy().items():
        if v == value:
            del a_dictionary[k]
    return a_dictionary
