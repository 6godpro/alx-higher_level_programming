#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value.)"""
    if isinstance(a_dictionary, dict) and len(a_dictionary) != 0:
        max = 0
        for k in a_dictionary:
            if a_dictionary[k] > max:
                key = k
                max = a_dictionary[k]
        return key
