#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""
    num = 0
    if isinstance(roman_string, str):
        roman_dict = {
                "I": 1, "V": 5, "X": 10,
                "L": 50, "C": 100, "D": 500,
                "M": 1000
        }
        for i, ch in zip(range(len(roman_string)), roman_string):
            if roman_dict.get(ch.upper(), 0) == 0:
                return 0
            if i < len(roman_string) - 1:
                next_ch = roman_string[i + 1]
            if i < len(roman_string) - 1 and \
                    roman_dict[ch.upper()] < roman_dict[next_ch.upper()]:
                num += -(roman_dict[ch.upper()])
            else:
                num += roman_dict[ch.upper()]
    return num
