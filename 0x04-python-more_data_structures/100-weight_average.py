#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers 
       tuple (<score>, <weight>)."""
    avg = 0
    if isinstance(my_list, list) and my_list != []:
        t_score, t_avg = 0, 0
        for tup in my_list:
            t_score += tup[0] * tup[1]
            t_avg += tup[1]
        avg = t_score / t_avg
    return avg
