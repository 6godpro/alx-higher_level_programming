#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text indentating function."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of
       these characters: ., ? and :

    Args:
        text (str): Text to be indented.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        if text[i] == ' ' and text[i - 1] in ".:?":
            while i < len(text) and text[i] == ' ':
                if i == len(text) - 1:
                    return
                i += 1
        print(text[i], end="")
        if text[i] in ".:?":
            [print("") for i in range(2)]
        i += 1
