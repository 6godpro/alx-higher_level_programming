#!/usr/bin/python3
# 7-add_item.py
"""This script adds all the arguments to a list and saves them to a file."""


if __name__ == "__main__":
    import sys
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load("add_item.json")
    except OSError:
        items = []

    for i in range(1, len(sys.argv)):
        items.append(sys.argv[i])

    save(items, "add_item.json")
