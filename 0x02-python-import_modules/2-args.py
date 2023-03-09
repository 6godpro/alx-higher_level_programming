#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the number of and the list of its arguments."""
    import sys

    arg_size = len(sys.argv) - 1
    if arg_size == 0:
        print("{} arguments.".format(arg_size))
    elif arg_size == 1:
        print("{:d} argument:".format(arg_size))
    else:
        print("{:d} arguments:".format(arg_size))

    for i, arg in zip(range(len(sys.argv)), sys.argv):
        if i != 0:
            print("{}: {}".format(i, arg))
