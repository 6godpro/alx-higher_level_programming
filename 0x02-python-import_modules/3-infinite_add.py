#!/usr/bin/env python3
if __name__ == "__main__":
    """Prints the result of the addition of all arguments."""
    import sys

    sum = 0
    for n in sys.argv[1:]:
        sum += int(n)
    print("{}".format(sum))
