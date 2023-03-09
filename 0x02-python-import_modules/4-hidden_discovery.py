#!/usr/bin/python3
if __name__ == "__main__":
    """Prints all the names defined by the compiled module hidden_4.pyc"""
    import hidden_4

    for name in dir(hidden_4):
        if name[:2] != '__':
            print("{}".format(name))
