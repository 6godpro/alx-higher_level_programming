#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string."""
    if isinstance(my_string, str):
        new_string = ''
        for ch in my_string:
            if ch in "cC":
                continue
            new_string += ch
        return new_string
