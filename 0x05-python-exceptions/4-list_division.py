#!/usr/bin/python3
# 4-list_division.py


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.

    Args:
        my_list (list): First list.
        my_list (list): First list.
        list_length (int): Number of elements to divide.
    Return:
        A new list of length list_length - new_list
    """
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except (TypeError, ValueError):
            print("wrong type")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
