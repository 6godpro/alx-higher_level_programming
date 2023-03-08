#!/usr/bin/python3
def uppercase(strn):
    new_str = ''
    for c in strn:
        if (ord(c) >= 97) and (ord(c) <= 122):
            c = ord(c) - 32
            c = chr(c)
        new_str += c
    print(new_str)
