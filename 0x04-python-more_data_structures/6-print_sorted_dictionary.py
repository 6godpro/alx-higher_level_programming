#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys."""
    for ele in sorted(a_dictionary):
        print(f"{ele}: {a_dictionary[ele]}")
