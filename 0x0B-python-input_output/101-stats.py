#!/usr/bin/python3
# 101-stats.py
import sys


def print_stat(size, status_codes):
    """Displays the statistics since the beginning.

    Args:
        size (int): The file size.
        status_codes (dict): The status code key/value pair.
    """
    print("File size: {}".format(size))
    [print(f"{k}: {status_codes[k]}") for k in sorted(status_codes)]

if __name__ == "__main__":
    status_code = {}
    count = 0
    size = 0
    try:
        for line in sys.stdin:
            if count == 10:
                print_stat(size, status_code)
                count = 1
            else:
                count += 1

            line = line.split()
            try:
                status_code[line[-2]] += 1
            except KeyError:
                status_code[line[-2]] = 1

            size += int(line[-1])

        print_stat(size, status_code)

    except KeyboardInterrupt:
        print_stat(size, status_code)
